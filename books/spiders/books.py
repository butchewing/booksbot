# -*- coding: utf-8 -*-
from urllib.parse import urlsplit
import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = [
        'http://books.toscrape.com/',
    ]

    def parse(self, response):
        for book_url in response.css("article.product_pod > h3 > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(book_url), callback=self.parse_book_page)
        next_page = response.css("li.next > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_book_page(self, response):
        item = {}

        item['url'] = response.url
        item['slug'] = urlsplit(response.url).path
        item['directories'] = ', '.join([x for x in urlsplit(response.url).path.split('/')[1:]]),
        item['title'] = response.xpath('//title/text()').extract()
        item['h1'] = response.xpath('//h1//text()').extract()
        item['h2'] = response.xpath('//h2//text()').extract()
        item['h3'] = response.xpath('//h3//text()').extract()
        item['h4'] = response.xpath('//h4//text()').extract()
        item['description'] = response.xpath("//meta[@name='description']/@content")[0].extract()
        item['img_links'] = 0
        item['img_alt_tags'] = 0
        item['img_count'] = 0
#        item['link_urls'] = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "btTextLeft", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "bt_bb_wrapper", " " ))]//a/@href').extract() 
#        item['link_text'] = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "btTextLeft", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "bt_bb_wrapper", " " ))]//a/text()').extract()
#        item['link_count'] = len(item['link_urls'])        
        item['load_time'] = response.meta['download_latency']
        item['status_code'] = response.status 
        
        product = response.css("div.product_main")
        item["title"] = product.css("h1 ::text").extract_first()
        item['category'] = response.xpath(
            "//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()"
        ).extract_first()
        item['description'] = response.xpath(
            "//div[@id='product_description']/following-sibling::p/text()"
        ).extract_first()
        item['price'] = response.css('p.price_color ::text').extract_first()
        yield item
