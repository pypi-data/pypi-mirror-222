# bilibili-download

## 介绍

本工具用于批量下载 B 站指定用户的专辑视频。

> 具体下载单个视频使用`you-get`工具，安装时会自动检测安装，如果出现问题也可以手动自行安装。

## 声明

本工具禁止用于商业用途。

## 安装

```bash
pip install bilibili-download-icexmoon
```

## 更新

```bash
pip install bilibili-download-icexmoon --upgrade
```

## 使用说明

需要定义一个下载用描述文件`download.json`。

文件格式为 json，格式如下：

```json
{
    "homeDir": "D:/workspace/bilibili/tests/download",
    "users": [
        {
            "id": "581567817",
            "albums": [
                {
                    "id": "1036613",
                    "redoTimes": 5
                },
                {
                    "id": "764241",
                    "redoTimes": 5
                }
            ]
        }
    ],
    "apiRetryMax": 50
}
```

其中元素的含义为：

- homeDir，下载视频保存的根目录，下载好的视频会按照专辑 id 作为子目录进行保存，默认为当前目录。
- users，待下载的用户信息。
- users.id，用户id
- users.albums，用户专辑信息
- albums.id，专辑id
- albums.redoTimes，专辑下载额外重试次数（接口有调用限制，单次下载部分视频会缺失），默认10
- apiRetryMax，接口调用重试最大次数，默认50

定义好后在 json 文件所在的目录执行：

```bash
bb-download
```

即可开始下载。

