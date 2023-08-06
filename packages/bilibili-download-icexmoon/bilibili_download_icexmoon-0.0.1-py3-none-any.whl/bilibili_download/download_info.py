import os
from .bilibili_user import BilibiliUser


class DownloadInfo():
    '''视频下载信息，用于为批量下载提供依据'''

    def __init__(self) -> None:
        self.home_dir: str = os.getcwd()  # 下载的主目录，默认为当前目录
        self.users: list[BilibiliUser] = []  # 待下载的用户列表
        self.api_retry_max: int = 50  # api 调用失败重试最大次数, 默认50次

    def add_user(self, user: BilibiliUser) -> None:
        '''添加b站用户
        user: 待下载视频的b站用户
        '''
        self.users.append(user)
