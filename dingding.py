#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import sys
import os
headers = {'Content-Type': 'application/json;charset=utf-8'}
#api_url后跟告警机器人的webhook
api_url = "https://oapi.dingtalk.com/robot/send?access_token="
def msg(text):
   json_text= {
    "msgtype": "text",
    "text": {
        "content": text
    }
   }
   print(requests.post(api_url,json.dumps(json_text),headers=headers).content)
if __name__ == '__main__':
   text = sys.argv[1]
   msg(text)

