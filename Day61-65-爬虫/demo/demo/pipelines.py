# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
import openpyxl

from demo.items import DoubanItem

from itemadapter import ItemAdapter


class DemoPipeline:
    def process_item(self, item, spider):
        return item


class DoubanItemPipeLine(scrapy.Spider):
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.title = "Top250"
        self.sheet.append(("名称", "评分", "名言"))

    def process_item(self, item: DoubanItem, spider):
        self.sheet.append((item["title"], item["score"], item["motto"]))
        return item

    def close_spider(self, spider):
        self.wb.save("豆瓣电影数据.xlsx")
