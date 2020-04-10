# -*- coding: utf-8 -*-

# Scrapy settings for prestashop project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'prestashop'

SPIDER_MODULES = ['prestashop.spiders']
NEWSPIDER_MODULE = 'prestashop.spiders'

USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 1

#LOG_LEVEL = 'INFO'

FEED_FORMAT = 'csv'
FEED_EXPORT_ENCODING = 'utf-8'
FEED_URI = 'prestashop_products.csv'
FEED_EXPORTERS_BASE = {
    'csv': 'scrapy.exporters.CsvItemExporter',
}
