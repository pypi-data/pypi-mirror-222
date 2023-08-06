from .json_parse import JsonParse
import os
import requests
import time
import subprocess
from .download_info import DownloadInfo
from .bilibili_album import BilibiliAlbum


class Main():
    def __init__(self):
        self.download_info: DownloadInfo = None
        self.headers = {
            'referer': 'https://www.bilibili.com/video/BV1J3411h7pm?spm_id_from=333.5.0.0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69'
        }

    def main(self):
        jp = JsonParse(os.getcwd()+'/download.json')
        self.download_info = jp.parse()
        if not os.path.exists(self.download_info.home_dir):
            os.mkdir(self.download_info.home_dir)
        for user in self.download_info.users:
            for album in user.albums:
                # 至少下载专辑1次
                self.scan_and_download_collector(album=album)
                # 如果设置了 redo，额外尝试 N 次
                for _ in range(0, album.redo_times):
                    self.scan_and_download_collector(album=album)

    def scan_and_download_collector(self, album: BilibiliAlbum, tryTimes=0):
        '''扫描并下载专辑'''
        pSize = 30  # 30
        maxPNum = 10  # 10
        mid = album.uid
        sid = album.id
        for pNum in range(1, maxPNum+1):
            maxTryTimes = self.download_info.api_retry_max  # 重试最大次数
            # 获取某一页的视频列表
            url = "https://api.bilibili.com/x/polymer/web-space/seasons_archives_list?mid={}&season_id={}&sort_reverse=false&page_num={}&page_size={}"
            url = url.format(mid, sid, pNum, pSize)
            print("request api [{}]".format(url))
            response: map = requests.get(url=url, headers=self.headers).json()
            time.sleep(2)
            if response['code'] == 0 and 'archives' in response['data']:
                vedioList: list = response['data']['archives']
                if len(vedioList) <= 0:
                    # 没有更多视频，结束扫描
                    print("no more vedioes, end scan.")
                    break
                # 下载视频列表
                print("find vedio list, include {} vedios, begin download.".format(
                    len(vedioList)))
                self.download_vedioList(vedioList, sid)
            else:
                # 获取视频列表出错，重试
                tryTimes += 1
                # 重试次数草果最大次数，失败
                if tryTimes >= maxTryTimes:
                    msg = "try times over max times, app exit."
                    print(msg)
                    raise Exception(msg)
                print("request api error, try again[{}]".format(tryTimes))
                self.scan_and_download_collector(album, tryTimes)

    def download_vedioList(self, vedioList: list, sid: str):
        '''下载视频列表
        vedioList: 视频列表
        sid: 专辑id
        '''
        for vedio in vedioList:
            self.download_vedio(vedio, sid)

    
    def download_vedio(self, vedio: map, sid: str):
        '''下载视频
        vedio: 视频信息
        sid: 所属专辑id
        '''
        bvid = vedio['bvid']
        title = vedio['title']
        download_dir = "{}/{}".format(self.download_info.home_dir, sid)
        path = download_dir
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        base_file = "{}/{}".format(download_dir, title)
        file1 = "{}.mp4".format(base_file)
        file2 = "{}.flv".format(base_file)
        if os.path.exists(file1) or os.path.exists(file2):
            # 本地已经存在该文件，不重复下载
            print("file {} is exsist, jump.".format(base_file))
            return
        # path = path.replace("\\", "\\\\")
        url = "https://www.bilibili.com/video/{}".format(bvid)
        # cmd = "you-get -o {} https://www.bilibili.com/video/{}".format(
        #     path, bvid)
        # print("exec you-get, cmd[{}]".format(cmd))
        # subprocess.call(cmd, shell=True)
        print("begin downlod vedio [{}]".format(url))
        result = subprocess.run(["you-get", "-o", path, url], shell=True)
        # print(result.stdout.decode("GBK"))
        time.sleep(5)