from .download_info import DownloadInfo
import os
import json
from .map_util import MapUtil
from .bilibili_user import BilibiliUser
from .bilibili_album import BilibiliAlbum


class JsonParse():
    '''json配置解析器'''

    def __init__(self, file: str) -> None:
        '''初始化解析器
        file: json配置文件路径
        '''
        self.file = file

    def parse(self) -> DownloadInfo:
        '''解析配置文件并返回 DownloadInfo 对象'''
        download_info = DownloadInfo()
        # 检查 json 配置文件是否存在
        if not os.path.exists(self.file) or not os.path.isfile(self.file):
            raise Exception("error: file {} don't exist.".format(self.file))
        # 从配置文件读取信息
        jsonObj = None
        with open(file=self.file, mode='r') as fopen:
            jsonObj = json.load(fopen)
        if jsonObj is None:
            raise Exception(
                "error: json file {} parse fail.".format(self.file))
        if 'homeDir' in jsonObj and jsonObj['homeDir'] != '':
            download_info.home_dir = jsonObj['homeDir']
        if 'users' not in jsonObj or not isinstance(jsonObj['users'], list | tuple):
            raise Exception(
                "error: json file format error, don't have users node, or users node is not array.")
        if len(jsonObj['users']) == 0:
            raise Exception("error: json file format error, users is empty.")
        for user in jsonObj['users']:
            MapUtil.check_key_exists(user, 'id')
            MapUtil.check_key_exists(user, 'albums')
            uid: str = user['id']
            albums = user['albums']
            bilibili_user = BilibiliUser(uid)
            if not isinstance(albums, list | tuple):
                raise Exception(
                    "error: json file format error, albums node is not array.")
            for album in albums:
                if not isinstance(album, dict):
                    raise Exception("error: json file format error, albums node's element is not map.")
                MapUtil.check_key_exists(album, "id")
                bilibili_album = BilibiliAlbum(album['id'])
                if 'redoTimes' in album:
                    bilibili_album.redo_times = int(album['redoTimes'])
                bilibili_user.addAlbum(bilibili_album)
            download_info.add_user(bilibili_user)
        if 'apiRetryMax' in jsonObj:
            download_info.api_retry_max = int(jsonObj['apiRetryMax'])
        return download_info
