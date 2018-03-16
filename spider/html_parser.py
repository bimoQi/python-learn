#!/usr/bin/env python3
# coding: utf-8
import re
from bs4 import BeautifulSoup

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        for link in soup.find_all('a', href=re.compile(r"/item/.+")):
            new_full_url = 'http://baike.baidu.com'+link['href']
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        result_data = {}
        result_data['url'] = page_url
        title_node = soup.find('dd', class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
        result_data['title'] = title_node.string
        discript_node = soup.find('div', class_ = 'lemma-summary')
        result_data['discript'] = discript_node.get_text("  ")

        return result_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data