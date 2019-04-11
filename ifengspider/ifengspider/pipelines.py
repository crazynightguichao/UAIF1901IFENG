# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class IfengspiderPipeline(object):
#     def process_item(self, item, spider):
#         # print(item['title'],item['conlink'])
#         return item
# 保存数据
class IfengspiderPipeline:
    def process_item(self,item,spider):
        with open('ifeng.txt','a',encoding="utf-8") as f:
            f.write("%s %s"%(item['category'],item['link']))
            f.write("\n")
            f.write("%s %s" % (item['title'], item['conlink']))
            f.write("\n")
            f.write("%s %s %s" % (item['date'], item['author'], item['con']))
            f.write("\n")
        return item