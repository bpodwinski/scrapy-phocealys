# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from prestashop.items import PrestashopItem
from scrapy.selector import Selector
from scrapy.http import Request


class prestashop(CrawlSpider):
    name = "prestabot"
    allowed_domains = ['www.phocealys.com']
    start_id_product = 1
    end_id_product = 1000

    def start_requests(self):
        for i in range(self.start_id_product, self.end_id_product):
            yield Request('https://www.phocealys.com/fr/index.php?controller=product&id_product=%d' % i,
            callback=self.parse_items)

    def parse_items(self, response):

        sel = Selector(response)

        item = PrestashopItem()

        item['url'] = response.url

        item['balise_title'] = sel.xpath('//title/text()').extract()

        item['balise_meta_description'] = sel.xpath(
            '/html/head/meta[@name="description"]/@content').extract()

        item['h1'] = sel.xpath('//h1/text()').extract()

        item['reference'] = sel.xpath(
            '//span[@itemprop="sku"]/text()').extract_first()

        item['description_courte'] = sel.xpath(
            '//div[@class="description_short"]//p/following-sibling::*[1]/text()').extract()

        item['description_longue'] = sel.xpath(
            '//div[contains(@class, "product-description")]//ul/li/text()').extract()

        # https://stackoverflow.com/questions/55969217/extracting-properties-table-from-the-product-dt-dd-with-scrapy-getting-list-i
        item['features'] = list()
        for prop in sel.xpath('//dl[@class="data-sheet"]/dt'):
            item['features'].append(
                {
                    'name': prop.xpath('normalize-space(./text())').extract(),
                    'value': prop.xpath('normalize-space(./following-sibling::dd/text())').extract(),
                }
            )

        item['prix_ht'] = sel.xpath(
            '//meta[@property="product:pretax_price:amount"]/@content').extract()

        item['prix_ttc'] = sel.xpath(
            '//meta[@property="product:price:amount"]/@content').extract()

        item['weight'] = sel.xpath(
            '//meta[@property="product:weight:value"]/@content').extract()

        item['images'] = sel.xpath(
            '//li[@class="thumb-container"]//img/@data-image-large-src').extract()

        item['main_image'] = sel.xpath(
            '//div[@class="images-container"]//div[@class="product-cover"]//img/@src').extract()

        yield item
