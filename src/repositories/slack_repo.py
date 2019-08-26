from pymongo import MongoClient
import datetime

from mappers.mongo_mapper import SlackRequestMongoMapper
from models.slack import SlackRequest

client = MongoClient('localhost', 27017)


class SenderRepository(MongoClient):
    db_client = MongoClient('localhost', 27017)

    def __init__(self, provide):
        super().__init__()
        self.provide = provide

    @classmethod
    def get_db(cls):
        return cls.db_client.jiraDB.slackRequests

    @classmethod
    def insert(cls, data: SlackRequest):
        cls.get_db().insert_one(SlackRequestMongoMapper.to_mongo(data))

# db = client.test_db
# collection = db.test_collection
