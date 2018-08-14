# -*- coding: utf-8 -*-
import scrapy


class BadbitcoinSpider(scrapy.Spider):
    name = 'badbitcoin'
    allowed_domains = ['badbitcoin.org']
    start_urls = ['http://badbitcoin.org/']

    def parse(self, response):
        pass
