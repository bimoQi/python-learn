#!/usr/bin/env python
# coding: utf-8
import urllib3

class HtmlDownloader(object):

    def download(self, url, method = 'GET'):
        http = urllib3.PoolManager()
        respose = http.request(method, url)
        if respose.status != 200:
            return None
        return respose.data
