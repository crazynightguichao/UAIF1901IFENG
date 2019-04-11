# -*- coding: utf-8 -*-
import scrapy
from ifengspider.items import IfengspiderItem



class IfengSpider(scrapy.Spider):
    name = 'ifeng'
    allowed_domains = ['news.ifeng.com']
    start_urls = ['http://news.ifeng.com/ipad']

    def parse(self, response):
        categorys = response.xpath("//ul[@class='clearfix']/li/a/text()").extract()
        links = response.xpath("//ul[@class='clearfix']/li/a/@href").extract()
        print(categorys,links)
        for category,link in zip(categorys,links):
            # # item = IfengspiderItem()        # 实例化 import IfengspiderItem
            # # item['category'] = category
            # # item['link'] = link
            # 记录  标题 以及 标题链接
            # category link
            data = {'category': category,'link':link}
            #请求分类页面
            yield scrapy.Request(link,meta={'data':data},callback=self.getNewList)
    def getNewList(self,response):
        data = response.meta['data']        # 通过meta得到item
        # print(item)
        category = data["category"]
        link = data["link"]
        titles = []
        conlinks = []
        if category == "国际":#
            titles += response.xpath("//div[@class ='juti_list']/h3/a/text()").extract()
            conlinks += response.xpath("//div[@class ='juti_list']/h3/a/@href").extract()
        if category == "即时":#
            titles += response.xpath("//div[@class='newsList']/ul/li/a/text()").extract()
            conlinks += response.xpath("//div[@class='newsList']/ul/li/a/@href").extract()
        if category == "大陆":#
            titles += response.xpath("//div[@class='juti_list']/h3/a/text()").extract()
            conlinks += response.xpath("//div[@class='juti_list']/h3/a/@href").extract()
        if category == "台湾":#
            titles += response.xpath("//div[@class='juti_list']/h3/a/text()").extract()
            conlinks += response.xpath("//div[@class='juti_list']/h3/a/@href").extract()
        if category == "社会":#
            titles += response.xpath("//div[@class='juti_list']/h3/a/text()").extract()
            conlinks += response.xpath("//div[@class='juti_list']/h3/a/@href").extract()
        if category == "专题":#
            titles += response.xpath("//ul[@class='clearfix']/li/a/text()").extract()
            conlinks += response.xpath("//ul[@class='clearfix']/li/a/@href").extract()
        if category == "排行":#
            titles += response.xpath("//td/h3/a/text()").extract()
            conlinks += response.xpath("//td/h3/a/@href").extract()

        if titles and conlinks:

            for title,conlink in zip(titles, conlinks):
                item = IfengspiderItem()
                item['category'] = category
                item['link'] = link
                item['title'] = title
                item['conlink'] = conlink
                # print(item)
                yield scrapy.Request(conlink, meta={'item': item}, callback=self.getNewCon)
    def getNewCon(self,response):
        item = response.meta['item']
        date = []
        author = []
        con = []


        if item['category'] == "国际":
            date += response.xpath("//p[@class='p_time']/span[1]/text()").extract()
            author += response.xpath("//span[@class='ss03']/a/text()").extract()
            con += response.xpath("//div[@id='artical_real']//text()").extract()
        if item['category'] == "即时":
            pass
        if item['category'] == "大陆":
            date += response.xpath("//p[@class='p_time']/span[1]/text()").extract()
            author += response.xpath("//span[@class='ss03']/a/text()").extract()
            con += response.xpath("//div[@id='artical_real']//text()").extract()
        if item['category'] == "台湾":
            date += response.xpath("//p[@class='p_time']/span[1]/text()").extract()
            author += response.xpath("//span[@class='ss03']/a/text()").extract()
            con += response.xpath("//div[@id='artical_real']//text()").extract()
        if item['category'] == "排行":
            date += response.xpath("//p[@class='p_time']/span[1]/text()").extract()
            author += response.xpath("//span[@class='ss03']/a/text()").extract()
            con += response.xpath("//div[@id='artical_real']//text()").extract()


        if date and author and con:
            item['con'] = con
            item['date'] = date
            item['author'] = author
        yield item
