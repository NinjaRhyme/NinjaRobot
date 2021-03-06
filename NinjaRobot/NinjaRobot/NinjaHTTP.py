﻿import urllib.parse
import urllib.request
import urllib.error
import http.cookiejar
import re
import json


class NinjaHTTP(object):
    def __init__(self):
        self.cookie = http.cookiejar.CookieJar()
        processor = urllib.request.HTTPCookieProcessor(self.cookie)
        opener = urllib.request.build_opener(processor)
        opener.addheaders = [
            ('Accept', '*/*'),
            ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'),
            ('Content-Type', 'application/x-www-form-urlencoded; charset=utf-8'),
        ]
        urllib.request.install_opener(opener)
        pass

    def get(self, url, timeout=120, **headers):
        try:
            req = urllib.request.Request(url, None, headers)
            response = urllib.request.urlopen(req, timeout=timeout)
            return response.read().decode("UTF-8")
        except Exception as e:
            print('Error:', e)

    def post(self, url, params={}, timeout=120, **headers):
        try:
            data = urllib.parse.urlencode(params)
            data = data.encode('UTF-8')
            req = urllib.request.Request(url, data, headers)
            response = urllib.request.urlopen(req, timeout=timeout)
            return response.read().decode("UTF-8")
        except Exception as e:
            print('Error:', e)

    def download(self, url, file_path):
        output = open(file_path, 'wb')
        output.write(urllib.request.urlopen(url).read())
        output.close()

    def get_cookie(self, key):
        for c in self.cookie:
          if c.name == key:
            return c.value
        return ''
