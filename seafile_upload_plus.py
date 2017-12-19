#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
import os

def main():
    """
    Get token
    """
    hostname = 'http://123.56.81.235:8000'
    username = 'maxiaohong@hundun.cn'
    password = '3754934'
    get_token_url = '{}/api2/auth-token/'.format(hostname)
    r = requests.post(get_token_url, data={'username': username, 'password': password})
    token = json.loads(r.content)['token']


    """
    Get version
    """
    version = '1.0.0'
    with open('config.gradle') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if 'baseApkVersionName' in line:
                version = line.split("'")[1]
    dir_name = 'v' + version + '_channel'


    """
    create dir
    """
    repo_id = 'fe10fc73-c32c-43d8-9ea0-364dd175a7cf'
    create_dir_url = '{}/api2/repos/{}/dir/?p=/Android_APK/{}'.format(hostname, repo_id, dir_name)
    requests.delete(create_dir_url, data={'operation': 'mkdir'}, headers={'Authorization': 'Token ' + token})
    requests.post(create_dir_url, data={'operation': 'mkdir'}, headers={'Authorization': 'Token ' + token})


    """
    Get upload link
    """
    upload_link_url = '{}/api2/repos/{}/upload-link/'.format(hostname, repo_id)
    r = requests.get(upload_link_url, headers={'Authorization': 'Token ' + token})
    upload_link = json.loads(r.content)


    """
    Upload file
    """
    url = upload_link
    path = "app/build/outputs/apk/debug"  # 文件夹目录
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    for file in files:  # 遍历文件夹
        print file
        if os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
            continue
        if not file.startswith('app'):
            continue
        filename = path + "/" + file
        with open(filename, 'rb') as f:
            requests.post(url, data={'filename': filename, 'parent_dir': '/Android_APK/jenkins'},
                          files={'file': f}, headers={'Authorization': 'Token ' + token})


if __name__ == '__main__':
    main()
