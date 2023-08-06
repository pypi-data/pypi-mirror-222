import copy
import logging
import subprocess

from . import plugins
from .downloader import download, check_url
from .engine import invert_dict, Plugin
from biliup.config import config
from .engine.event import Event, EventManager
from .uploader import upload

CHECK = 'check'
CHECK_UPLOAD = 'check_upload'
TO_MODIFY = 'to_modify'
DOWNLOAD = 'download'
UPLOAD = 'upload'
logger = logging.getLogger('biliup')


def create_event_manager():
    streamer_url = {k: v['url'] for k, v in config['streamers'].items()}
    inverted_index = invert_dict(streamer_url)
    urls = list(inverted_index.keys())
    pool1_size = config.get('pool1_size', 3)
    pool2_size = config.get('pool2_size', 3)
    # 初始化事件管理器
    app = EventManager(config, pool1_size=pool1_size, pool2_size=pool2_size)
    app.context['urls'] = urls
    app.context['url_status'] = dict.fromkeys(inverted_index, 0)
    app.context['url_upload_count'] = dict.fromkeys(inverted_index, 0)
    # 正在上传的文件 用于同时上传一个url的时候过滤掉正在上传的
    app.context['upload_filename'] = []
    app.context['checker'] = Plugin(plugins).sorted_checker(urls)
    app.context['inverted_index'] = inverted_index
    app.context['streamer_url'] = streamer_url
    return app


event_manager = create_event_manager()


@event_manager.register(DOWNLOAD, block='Asynchronous1')
def process(name, url):
    stream_info = {
        'name': name,
        'url': url,
    }
    url_status = event_manager.context['url_status']
    # 下载开始
    url_status[url] = 1
    try:
        kwargs: dict = config['streamers'][name].copy()
        kwargs.pop('url')
        suffix = kwargs.get('format')
        if suffix:
            kwargs['suffix'] = suffix
        stream_info = download(name, url, **kwargs)
    finally:
        # 下载结束
        url_status[url] = 0
        yield Event(UPLOAD, (stream_info,))


@event_manager.register(UPLOAD, block='Asynchronous2')
def process_upload(stream_info):
    url = stream_info['url']
    url_upload_count = event_manager.context['url_upload_count']
    # 上传开始
    url_upload_count[url] += 1
    try:
        upload(stream_info)
    finally:
        # 上传结束
        url_upload_count[url] -= 1


@event_manager.server()
class KernelFunc:
    def __init__(self, urls, url_status: dict, url_upload_count: dict, checker, inverted_index, streamer_url):
        self.urls = urls
        # 录制状态 0等待录制 1正在录制 2正在上传(废弃)
        self.url_status = url_status
        # 上传状态 0未上传 >=1正在上传
        self.url_upload_count = url_upload_count
        self.checker = checker
        self.inverted_index = inverted_index
        self.streamer_url = streamer_url

    @event_manager.register(CHECK, block='Asynchronous1')
    def singleton_check(self, platform):
        plugin = self.checker[platform]
        wait = config.get('checker_sleep', 15)
        for url in check_url(plugin, self.url_status, self.url_upload_count, secs=wait):
            yield Event(TO_MODIFY, args=(url,))

    @event_manager.register(TO_MODIFY)
    def modify(self, url):
        if not url:
            # ?????
            logger.debug('无人直播')
            return


        name = self.inverted_index[url]
        if config['streamers'].get(name, {}).get('preprocessor'):
            preprocessor(config['streamers'].get(name, {}).get('preprocessor'), f'{{"name": "{name}", "url": "{url}"}}')
        logger.debug(f'{name}刚刚开播，去下载')
        return Event(DOWNLOAD, args=(name, url))

    @event_manager.register(CHECK_UPLOAD)
    def free_upload(self):
        # 检测之前可能未上传的视频
        for title, urls in self.streamer_url.items():
            for url in urls:
                if self.url_status[url] == 1 or self.url_upload_count[url] > 0:
                    continue
                yield Event(UPLOAD, args=({'name': title, 'url': url},))

    def get_url_status(self):
        # 这里是为webui准备的
        # webui fix
        url_status = copy.deepcopy(self.url_status)

        # 上传的情况下修改status 2
        for url in self.url_upload_count:
            if self.url_upload_count[url] > 0:
                url_status[url] = 2

        return url_status


def preprocessor(processors, data):
    for processor in processors:
        if processor.get('run'):
            try:
                process_output = subprocess.check_output(
                    processor['run'], shell=True,
                    input=data,
                    stderr=subprocess.STDOUT, text=True)
                logger.info(process_output.rstrip())
            except subprocess.CalledProcessError as e:
                logger.exception(e.output)
                continue
