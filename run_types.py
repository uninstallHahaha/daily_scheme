# 运行参数
class Params:
    def __init__(self):
        self.start_date = ""
        self.city = ""
        self.birthday = ""
        self.app_id = ""
        self.app_secret = ""
        self.user_ids = ""
        self.template_id = ""


# NewParams 创建参数实例
def NewParams(
    start_date, city, birthday, app_id, app_secret, user_ids, tempalate_id
) -> Params:
    ret = Params()
    ret.start_date = start_date
    ret.city = city
    ret.birthday = birthday
    ret.app_id = app_id
    ret.app_secret = app_secret
    ret.user_ids = user_ids
    ret.template_id = tempalate_id
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
