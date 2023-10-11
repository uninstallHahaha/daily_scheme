import os
import run_types
import math
import requests
import random
import re
import json
from datetime import date, datetime, timedelta
from wechatpy import WeChatClient, WeChatClientException
from wechatpy.client.api import WeChatMessage


# GetParams 从环境变量中获取变量
def GetParams() -> run_types.Params:
    user_ids = os.getenv("USER_ID", "").split("\n")

    if not user_ids:
        print("请设置 USER_ID, 若存在多个 ID 用回车分开")
        exit(422)

    return run_types.NewParams(
        user_ids=user_ids,
    )


# 获取天气信息, 高德天气: https://lbs.amap.com/api/webservice/guide/api/weatherinfo/#t1
def GetWeather(city: str) -> run_types.WeatherModal:
    if city is None:
        print("请设置城市")
        return None
    url = "https://restapi.amap.com/v3/weather/weatherInfo?key=4bfc5e9004be0d9809ae4b6055c62f1e&city={}&extensions=all".format(
        city
    )
    res = requests.get(url).json()
    if res["status"] != "1":
        weather = run_types.WeatherModal()
        weather.weather = "晴"
        weather.temp = 26
        weather.humidity = 56
        return weather

    # 格式化查询到的数据
    todayWeather = res["forecasts"][0]["casts"][0]
    weather = run_types.WeatherModal()
    weather.weather = todayWeather["dayweather"]
    weather.temp = int(todayWeather["daytemp"])
    weather.humidity = 56
    return weather


# 获取天气提示语
def GetTipByWheather(weather: run_types.WeatherModal) -> str:
    w = weather.weather
    t = math.floor(weather.temp)
    tip = ""
    if t >= 26 and t <= 18 and ("多云" in w or "晴" in w):
        m = datetime.datetime.today().month
        emoji = "🍉" if m > 4 and m < 10 else "⛄️"
        return "天气不错, 祝你一天愉快 " + emoji
    if "雨" in w:
        return "🌧️ 现在在下雨, 出门记得带伞哦"
    if "晴" in w:
        return "🌞 现在是晴天, 出门记得防晒哦"
    return "✨ 又是想你的一天"


# 彩虹屁 接口不稳定，所以失败的话会重新调用，直到成功
def GetWords() -> str:
    words = requests.get("https://api.shadiao.pro/du")
    if words.status_code != 200:
        return GetWords()
    return words.json()["data"]["text"]


# 获取当前日期为星期几
def GetWeekDay(today):
    week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    week_day = week_list[datetime.date(today).weekday()]
    return week_day


# 随机颜色
def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


# 发送消息
def SendMsg(
    app_id: str,
    app_secret: str,
    template_id: str,
    user_ids: slice,
    data: run_types.SendData,
):
    # 实例转 dict
    data = dict(data)

    try:
        client = WeChatClient(app_id, app_secret)
    except WeChatClientException as e:
        print("微信获取 token 失败，请检查 APP_ID 和 APP_SECRET, 或当日调用量是否已达到微信限制。")
        exit(502)

    wm = WeChatMessage(client)
    count = 0
    try:
        for user_id in user_ids:
            print("正在发送给 %s, 数据如下: %s" % (user_id, data))
            res = wm.send_template(user_id, template_id, data)
            count += 1
    except WeChatClientException as e:
        print("微信端返回错误：%s。错误代码: %d" % (e.errmsg, e.errcode))
        exit(502)

    print("发送了" + str(count) + "条消息")
