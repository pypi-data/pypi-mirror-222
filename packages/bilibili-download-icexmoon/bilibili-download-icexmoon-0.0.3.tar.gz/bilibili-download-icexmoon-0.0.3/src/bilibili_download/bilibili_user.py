from .bilibili_album import BilibiliAlbum


class BilibiliUser():
    '''b站用户信息'''

    def __init__(self, id: str, albums: list[BilibiliAlbum] = []) -> None:
        '''初始化b站用户
        id: b站用户id
        '''
        self.id: str = id  # b站用户的uid
        self.albums = albums  # 包含的专辑

    def addAlbum(self, album: BilibiliAlbum) -> None:
        '''添加专辑
        album: b站专辑
        '''
        album.uid = self.id
        self.albums.append(album)
