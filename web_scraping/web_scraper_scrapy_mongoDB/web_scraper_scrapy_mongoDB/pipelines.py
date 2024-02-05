# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from scrapy.utils.project import get_project_settings
from .items import WebScraperPokemonItem
from dataclasses import asdict

settings = get_project_settings()


class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings.get("MONGO_HOST"),
            settings.get("MONGO_PORT"),
        )

        db = connection[settings.get("MONGO_DB_NAME")]
        self.collection = db[settings["MONGODB_COLLECTION"]]

    def process_item(self, item, spider):
        if isinstance(item, WebScraperPokemonItem):
            self.collection.insert_one(dict(item))
        return item
