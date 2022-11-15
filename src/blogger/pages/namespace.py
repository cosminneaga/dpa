from flask_restx import Namespace, Resource
from flask import render_template, make_response

from utils.auth import protect_pages
from utils.env import env_val
from src.blogger.db.index import Database

api = Namespace('blogger pages', description='Blogger Pages')
headers = {'Content-type': 'text/html'}

@api.route('/')
class Index(Resource):

    def get(self):
        return make_response(render_template('blogger/index.html'), 200, headers)


@api.route('/panel')
class Panel(Resource, Database):

    def __init__(self, *args, **kwargs):
        Database.__init__(self)
        Resource.__init__(self, *args, **kwargs)
        self.secret = env_val('BLOGGER_JWT_SECRET')

    @protect_pages
    def get(self):
        self.initialise()
        return make_response(render_template('blogger/panel.html'), 200, headers)


@api.route('/blog')
class Blog(Resource):

    def get(self):
        return make_response(render_template('blogger/blog.html'), 200, headers)