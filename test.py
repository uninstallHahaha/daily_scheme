import math
import requests
import os
import random
import re
import common
from datetime import date, datetime, timedelta
import datetime as _datetime

from wechatpy import WeChatClient, WeChatClientException
from wechatpy.client.api import WeChatMessage


def calc_to_end() -> int:
    today = _datetime.datetime.now()
    end = _datetime.datetime(2023, 10, 31)
    sub = (end - today).days
    return sub


if __name__ == "__main__":
    print("还剩 " + str(calc_to_end()) + " 天")
