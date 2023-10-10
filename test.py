import math
import requests
import os
import random
import re
import common
from datetime import date, datetime, timedelta

from wechatpy import WeChatClient, WeChatClientException
from wechatpy.client.api import WeChatMessage

# 纪念日
start_date = "2000-01-01"

# 天气信息
weather = None

# 星期几
weekDay = None

# 扬州
city = 321000

# 东八区时间
nowtime = datetime.utcnow() + timedelta(hours=8)

# 今天的日期
today = datetime.strptime(str(nowtime.date()), "%Y-%m-%d")


# 获取当前日期为星期几
def get_week_day():
    week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    week_day = week_list[datetime.date(today).weekday()]
    return week_day


# 获取天气信息
def get_weather():
    if city is None:
        print("请设置城市")
        return None
    url = "https://restapi.amap.com/v3/weather/weatherInfo?key=4bfc5e9004be0d9809ae4b6055c62f1e&city={}&extensions=all".format(
        city
    )
    res = requests.get(url).json()
    if res["status"] != "1":
        return {"weather": "晴", "temp": 26, "humidity": 56}

    # 格式化查询到的数据
    todayWeather = res["forecasts"][0]["casts"][0]
    weather = {
        "weather": todayWeather["dayweather"],
        "temp": todayWeather["daytemp"],
        "humidity": 56,
    }
    return weather


# 纪念日正数
def get_memorial_days_count():
    if start_date is None:
        print("没有设置 START_DATE")
        return 0
    delta = today - datetime.strptime(start_date, "%Y-%m-%d")
    return delta.days


if __name__ == "__main__":
    params = common.GetParams()
    print(params)
