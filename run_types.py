from json import JSONEncoder


# 运行参数
class Params:
    def __init__(self):
        self.city = ""
        self.app_id = ""
        self.app_secret = ""
        self.user_ids = ""


# NewParams 创建参数实例
def NewParams(
    user_ids,
) -> Params:
    ret = Params()
    ret.city = "321000"
    ret.app_id = "wx214addf2ecd34f2b"
    ret.app_secret = "1263507cdb5443517923113db1480788"
    ret.user_ids = user_ids
    return ret


# WeatherModal 天气信息
class WeatherModal:
    def __init__(self):
        self.weather = ""
        self.temp = 0
        self.humidity = 0


# SendData 发送消息使用的数据
class SendData:
    def __init__(self):
        self.city = ""
        self.date = ""
        self.time = ""
        self.week_day = ""
        self.weather = ""
        self.humidity = ""
        self.temperature = ""
        self.tip = ""
        self.words = ""
        self.to_end = 0

    def keys(self):
        return (
            "city",
            "date",
            "time",
            "week_day",
            "weather",
            "humidity",
            "temperature",
            "tip",
            "words",
            "to_end",
        )

    def __getitem__(self, item):
        return getattr(self, item)


class SendDataEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
