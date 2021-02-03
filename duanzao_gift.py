# /usr/bin/env python3.8
# coding:utf-8

"""
@file: duanzao_gift.py
@time: 2021/2/3 5:35 下午
@author:XF
"""
import json

import requests

url = 'http://testapi.ippzone.net/activity/forge_gift'

data = {
    "h_model": "iPhone 7",
    "h_ch": "appstore",
    "h_app": "zuiyou_lite",
    "h_ts": 1612345845614,
    "h_av": "5.4.9.005",
    "h_nt": 1,
    "h_did": "9dbf18975bcba62b24fd4da6087d46105b218b62",
    "h_m": 58706079,
    "h_pipi": "2.4.9.005",
    "h_os": 1330000,
    "token": "TbK9N-X7Q-NdE-GjF9zAlHRy1DhIn7HO7mvm63X8BXf8rSPE=",
    "userstatus": 2,
    "h_dt": 1,
    "mid": 58706079,
    "material": [{
        "gift_id": "283a28bd",
        "count": 1
    }],
    "target_gift_id": "283a28bd"
}

r = requests.post(url, json=data)
print(r.text)

# d = dict(r.text)
print(type(r.text))
# print(d)
