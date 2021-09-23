# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

#  pymongo импортируем внутрь файла pipelines.py
from pymongo import MongoClient

class BookparserPipeline:
# создаём конструктор внутри обработчика
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client['books0921']  # Меняем имя <--

# настраиваем постобработку
    def process_item(self, item, spider):
# разделяем данные с разных пауков по разным веткам скрипта
        if spider.name == 'labirint':  # Меняем имя <--
            pass
# разделяем данные с разных пауков по коллекциям и добавляем в разные БД
        collection = self.mongo_base[spider.name]
        # assert isinstance(collection, object)
        collection.insert_one(item)
        return item
