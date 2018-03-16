#!/usr/bin/env python
# coding: utf-8
import url_manager
import html_downloader
import html_parser
import html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('crawl %d: %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 100:
                    break

                count = count + 1
            except Exception as e:
                print('crawl failed:', e)

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/item/%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80/18752941'
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)
