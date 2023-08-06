class BilibiliAlbum():
    '''b 站专辑'''

    def __init__(self, id: str, uid: str = '') -> None:
        '''
        id: b站专辑id
        uid: 所属的b站用户id
        '''
        self.id: str = id  # 专辑id
        self.uid: str = uid  # b站用户id
        self.redo_times: str = 10 # 尝试多次重复下载专辑的次数， 默认10次
