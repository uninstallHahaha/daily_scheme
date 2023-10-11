from datetime import date, datetime, timedelta
import math
from wechatpy import WeChatClient, WeChatClientException
from wechatpy.client.api import WeChatMessage
import requests
import os
import random
import re
import common
import run_types


if __name__ == "__main__":
    # 环境变量中获取变量
    params = common.GetParams()
    # 东八区时间
    nowtime = datetime.utcnow() + timedelta(hours=8)
    # 今天的日期
    today = datetime.strptime(str(nowtime.date()), "%Y-%m-%d")
    # 当前时间
    time = nowtime.strftime("%H:%M:%S")
    # 获取天气
    weather = common.GetWeather(params.city)
    # 获取天气提示语
    weatherTip = common.GetTipByWheather(weather=weather)
    # 彩虹屁
    words = "停一停, 该去蒸米了"
    # 星期几
    week_day = common.GetWeekDay(today=today)

    # 发送给微信接口的数据
    data = run_types.SendData()
    data.city = {"value": params.city, "color": common.get_random_color()}
    data.date = {
        "value": today.strftime("%Y年%m月%d日"),
        "color": common.get_random_color(),
    }
    data.time = {
        "value": time,
        "color": common.get_random_color(),
    }
    data.week_day = {"value": week_day, "color": common.get_random_color()}
    data.weather = {"value": weather.weather, "color": common.get_random_color()}
    data.humidity = {"value": weather.humidity, "color": common.get_random_color()}
    data.temperature = {
        "value": math.floor(weather.temp),
        "color": common.get_random_color(),
    }
    data.tip = {
        "value": weatherTip,
        "color": common.get_random_color(),
    }
    data.words = {"value": words, "color": common.get_random_color()}

    # weekup 模板
    weekup_template_id = "qcrKG1JKtpu-Edht28bb9-bNI6SewSFZ-7yBgoW6r_o"
    common.SendMsg(
        params.app_id, params.app_secret, weekup_template_id, params.user_ids, data
    )
