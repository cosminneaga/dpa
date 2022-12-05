from flask_restx import Namespace, Resource, abort
from flask import request, abort, render_template, make_response
import json

from utils.response import response
from utils.auth import protect, tokenize, detokenize
from utils.env import env_val
from .db.index import Database

from .model import user
from .model import blog

api = Namespace('blogger', description='Blogger API')

# -------------------------------- user model -------------------------------- #
UserModel = user.UserModel(api)
RegisterModel = UserModel.toRegisterModel()
LoginModel = UserModel.toLoginModel()

BlogModel = blog.BlogModel(api)
toBlogModel = BlogModel.toCreateBlog()

# @api.route('/')
# # @api.doc(responses={
# #     200: 'Data Fetched',
# #     400: 'Bad Request',
# #     404: 'Not Found',
# #     500: 'Server Error'
# # })
# class Index(Resource):
#     pass

Database().initialise()

        
@api.route('/register')
class Register(Resource, Database):

    def __init__(self, *args, **kwargs):
        Database.__init__(self)
        Resource.__init__(self, *args, **kwargs)

    @api.doc(description='Register route - creates a new user - returns "token"')
    @api.expect(RegisterModel)
    def put(self):

        user = self.createUser(api.payload)
        token = tokenize(user, env_val('BLOGGER_JWT_SECRET'))
        return response('Register', {
            'token': token
        })


@api.route('/login')
class Login(Resource, Database):

    def __init__(self, *args, **kwargs):
        Database.__init__(self)
        Resource.__init__(self, *args, **kwargs)

    @api.doc(description='Login route - returns "token"')
    @api.expect(LoginModel)
    def post(self):

        email = api.payload['email']
        password = api.payload['password']
        user = self.getUser(None, email, password)
        token = tokenize(user, env_val('BLOGGER_JWT_SECRET'))

        resp = make_response(response('Login', {
            'token': token,
            'user': user,
        }))
        resp.set_cookie('X-Access-Token', token)
        return resp


@api.route('/user/me')
class User(Resource, Database):
    
    def __init__(self, *args, **kargs):
        Database.__init__(self)
        self.secret = env_val('BLOGGER_JWT_SECRET')

    # desc: get current user
    # protected
    # 
    @protect
    @api.doc(security='api_key')
    def get(self):
        return response('User info', self.decoded)



@api.route('/blogs/<string:userId>')
class Blogs(Resource, Database):

    def __init__(self, *args, **kwargs):
        Database.__init__(self)


    def get(self, userId):
        return response('Blogs List', self.getBlogs(userId))



@api.route('/blog/<string:userId>/<string:blogId>')
class Blog(Resource, Database):

    def __init__(self, *args, **kwargs):
        Database.__init__(self)
        Resource.__init__(self, *args, **kwargs)
        self.secret = env_val('BLOGGER_JWT_SECRET')


    @api.doc(description='Get a single bloc')
    def get(self, userId, blogId):
        return response('Blog', self.getBlog(userId, blogId))

    @api.doc(description='Update an entire blog')
    @api.expect(toBlogModel)
    @protect
    def put(self, userId, blogId):
        blog = self.updateBlog(userId, blogId, api.payload)
        return response('Blog updated', blog)


    @api.doc('Delete a blog')
    @protect
    def delete(self, userId, blogId):
        blog = self.deleteBlog(userId, blogId)
        return response('Blog deleted')

    


@api.route('/blog/<string:userId>')
class BlogCreate(Resource, Database):

    def __init__(self, *args, **kwargs):
        Database.__init__(self)
        Resource.__init__(self, *args, **kwargs)
        self.secret = env_val('BLOGGER_JWT_SECRET')

    @api.doc(description='Create a new Blog', summary='heya')
    @api.expect(toBlogModel)
    @protect
    def post(self, userId):

        blog = self.createBlog(userId, api.payload)
        return response('Blog created', blog)
    

@api.route('/hello')
class Hello(Resource):
    def get(self):
        return response('Welcome from Blogger v1.0')