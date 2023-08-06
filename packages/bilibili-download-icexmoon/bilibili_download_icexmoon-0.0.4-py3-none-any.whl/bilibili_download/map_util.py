class MapUtil():
    def __init__(self) -> None:
        pass

    @classmethod
    def check_key_exists(cls, map_var: map, key: str, error_msg:str='') -> None:
        if error_msg == '':
            error_msg = "error: map require key {}, but not exist.".format(key)
        if map_var is None:
            raise Exception("erorr: map obj is None.")
        if key not in map_var:
            raise Exception(error_msg)
