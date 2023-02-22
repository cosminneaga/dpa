from py_console import console
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


class DB:

    def __init__(self, host, name, username, password):
        self.host = host
        self.name = name
        self.username = username
        self.password = password
        self.client = MongoClient(
            self.host,
            username=self.username,
            password=self.password,
        )

    def test_connection(self):
        try:
            self.client.server_info()
            console.success(
                'Solid connection with "{}" DB! - '.format(self.name) + self.host)

        except ServerSelectionTimeoutError:
            console.error(
                'Server has not been connected to "{}" DB! Please restart the server! - '.format(
                    self.name) + self.host)

    def seed(self, collection, data):
        try:
            console.warn(
                'Collection "{}" seed commenced! DB "{}"'.format(
                    collection, self.name))

            self.database = self.client[self.name]
            self.collection = self.database[collection]
            self.collection.insert_many(data)

            console.warn(
                'Collection "{}" seed completed! DB "{}"'.format(
                    collection, self.name))
        except Exception as e:
            console.error(e)
