#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ./seafile_upload_plus.py


import urllib
import urllib2
import json
import sys

"""
Get token
"""
hostname = 'http://123.56.81.235:8000'
username = 'maxiaohong@hundun.cn'
password = '3754934'
get_token_url = '{}/api2/auth-token/'.format(hostname)
data = urllib.urlencode({'username': username, 'password': password})
request = urllib2.Request(get_token_url, data)
response = urllib2.urlopen(request)
_js_py = json.load(response)
token = _js_py['token']
response.close()

"""
Get upload link
"""

# repo_id = sys.argv[1]
repo_id = 'fe10fc73-c32c-43d8-9ea0-364dd175a7cf'
upload_link_url = '{}/api2/repos/{}/upload-link/'.format(hostname, repo_id)
get_upload_link = urllib2.Request(upload_link_url)
get_upload_link.add_header('Authorization', 'Token ' + token)
response_upload_link = urllib2.urlopen(get_upload_link)
upload_link = json.load(response_upload_link)
response_upload_link.close()

"""
Upload file
"""

import requests
import os

# filename = sys.argv[2]
url = upload_link
path = "app/build/outputs/apk/debug"  # 文件夹目录
files = os.listdir(path)  # 得到文件夹下的所有文件名称
s = []
for file in files:  # 遍历文件夹
    print file
    if os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
        continue
    if not file.startswith('app'):
        continue
    filename = path + "/" + file
    files = {'file': open(filename, 'rb')}
    r = requests.post(
        url, data={'filename': filename, 'parent_dir': '/Android_APK/jenkins'},
        files=files, headers={'Authorization': 'Token ' + token})
    files['file'].close()




# files = {'file': open(filename, 'rb')}
# r = requests.post(
#     url, data={'filename': filename, 'parent_dir': '/Android_APK/jenkins'},
#     files=files, headers={'Authorization': 'Token ' + token})
# files['file'].close()
