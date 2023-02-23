import json
import jwt
import datetime
from flask import abort
from bson.objectid import ObjectId
from py_console import console

from utils.error import UserNotFound, ApiKeyError, UserExists, NotFound
from utils.env import env_val
from utils.db import DB
from utils.valid import Validator
from utils.generator import StrGenerator
from utils.bcrypt import Hash


class Database(DB, Validator):

    def __init__(self):

        self.uri = self.dbPort = self.dbHost = None
        self.db_name = 'blogger'
        self.col_users = 'users'
        self.collection_blog_name = 'blog'

        self.username = env_val('BLOGGER_MONGO_DB_USERNAME')
        self.password = env_val('BLOGGER_MONGO_DB_PASSWORD')

        if env_val('APP_ENV') == 'development':
            # self.uri=env_val('BLOGGER_MONGO_URI_DEV')
            self.dbPort = env_val('BLOGGER_MONGO_PORT_DEV')
            self.dbHost = env_val('BLOGGER_MONGO_HOST_DEV')
        else:
            self.uri = env_val('BLOGGER_MONGO_URI_PROD')
            self.dbPort = env_val('BLOGGER_MONGO_PORT_PROD')
            self.dbHost = env_val('BLOGGER_MONGO_HOST_PROD')

        DB.__init__(
            self,
            self.dbHost,
            self.db_name,
            self.username,
            self.password)
        Validator.__init__(self)

        self.database = self.client[self.db_name]
        self.users = self.database['users']

    def initAppUser(self):
        try:
            if (self.users.count_documents({}) ==
                    0 and env_val('APP_ENV') == 'development'):
                f = open('src/blogger/db/default/user.json')
                default_user = json.loads(f.read())
                self.createUser(default_user)
        except Exception as e:
            console.error(str(e))

    def getUser(self, id=None, email=None, password=None):
        try:
            user = None
            if id:
                user = self.users.find_one({
                    "_id": ObjectId(id)
                })
            else:
                user = self.users.find_one({
                    "email": email
                })

                if user:
                    if not Hash().compare(password, user['password']):
                        user = None

            if not user:
                raise UserNotFound('User not found!')

            user['_id'] = str(user['_id'])

            return user
        except Exception as e:
            abort(400, str(e))

    def isUser(self, obj, stage='if-no-exists'):
        user = self.users.find_one(obj)

        if user and stage == 'if-no-exists':
            raise UserExists(
                'Email address already in use! Hence user has not been created...')
        elif not user and stage == 'if-exists':
            raise UserNotFound('User has not been found!')

    def createUser(self, data):
        try:

            self.validate_email(data['email'])
            self.isUser({
                'email': data['email']
            })

            # encrypt password
            data['password'] = Hash().make(data['password'])

            # generate external access_token
            data['access_token'] = self.generateExternalDataAccessToken()

            user = self.users.insert_one(data)
            return self.getUser(email=data['email'], password=data['password'])

        except Exception as e:
            abort(400, str(e))
            # raise UserNotFound(400, str(e))

    def getBlogs(self, userId):
        try:

            self.isUser({
                '_id': ObjectId(userId)
            }, 'if-exists')
            data = []
            collection = self.database['blog.' + userId]
            blogs = collection.find()
            for blog in blogs:
                blog['_id'] = str(blog['_id'])
                data.append(blog)

            return data

        except Exception as e:
            abort(400, str(e))

    def getBlog(self, userId, blogId):
        try:

            self.isUser({
                '_id': ObjectId(userId)
            }, 'if-exists')
            collection = self.database['blog.' + userId]
            blog = collection.find_one({
                '_id': ObjectId(blogId)
            })
            if not blog:
                raise NotFound('Blog has not been found!')

            blog['_id'] = str(blog['_id'])
            return blog

        except Exception as e:
            abort(404, str(e))

    def createBlog(self, userId, blogData):
        try:

            self.isUser({
                '_id': ObjectId(userId)
            }, 'if-exists')

            blogData['created_at'] = str(datetime.datetime.utcnow())
            blogData['updated_at'] = str(datetime.datetime.utcnow())

            collection = self.database['blog.' + userId]
            insert = collection.insert_one(blogData)
            _id = insert.inserted_id
            extract = collection.find_one({
                '_id': _id
            })
            extract['_id'] = str(extract['_id'])
            return extract

        except Exception as e:
            abort(400, str(e))

    def updateBlog(self, userId, blogId, blogData):
        try:

            self.isUser({
                '_id': ObjectId(userId)
            }, 'if-exists')

            blogData['updated_at'] = str(datetime.datetime.utcnow())

            collection = self.database['blog.' + userId]
            update = collection.update_one({
                '_id': ObjectId(blogId)
            }, {
                '$set': blogData
            })
            extract = collection.find_one({
                '_id': ObjectId(blogId)
            })
            extract['_id'] = str(extract['_id'])
            return extract

        except Exception as e:
            abort(400, str(e))

    def deleteBlog(self, userId, blogId):
        try:

            self.isUser({
                '_id': ObjectId(userId)
            }, 'if-exists')
            collection = self.database['blog.' + userId]
            collection.delete_one({
                '_id': ObjectId(blogId)
            })
            return True

        except Exception as e:
            abort(400, str(e))

    def generateExternalDataAccessToken(self):
        try:

            accessTokens = []
            for user in self.users.find():
                accessTokens.append(user['access_token'])

            return StrGenerator.generateRandomUniqueStrings(50, accessTokens)

        except Exception as e:
            abort(500, str(e))

    def getBlogsByAccessToken(self, accessToken):
        try:
            user = self.users.find_one({
                'access_token': accessToken
            })

            return self.getBlogs(str(user['_id']))

        except Exception as e:
            abort(500, str(e))

    def getBlogByAccessToken(self, accessToken, blogId):
        try:
            user = self.users.find_one({
                'access_token': accessToken
            })

            return self.getBlog(str(user['_id']), blogId)

        except Exception as e:
            abort(500, str(e))


db = Database()
db.test_connection()

# db.getBlog('62cee48f5856f9d3aa38be3f', '62cee48f5856f9d3aa38be40')
# db.getBlogs('62cee48f5856f9d3aa38be3f')
# print(db.getUser('62cdb61f0e5a20f143d933a9'))
# print(db.getUser(None, 'user@gmail.com', 'password'))

# db.generateExternalDataAccessToken()
