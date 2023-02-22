from flask_restx import Namespace, Resource, fields

from .models import Model


api = Namespace('example', description='Example API', ordered=True)

book_model = Model(api).toModel()
# print(book_model)


@api.route('/')
@api.response(200, 'Data Fetched')
@api.response(404, 'Not Found')
@api.response(400, 'Bad Request')
@api.response(500, 'Server Error')
class Data(Resource):

    def get(self):
        return {
            'hello': 1
        }

    def post(self):
        return {}

    def put(self):
        return {}

    def patch(self):
        return {}

    def delete(self):
        return {}


@api.route('/path_parameters/<string:name>', doc={
    'params': {
        'name': {
            'description': 'name field label',
            'required': True,
            'example': 'Cosmin',
            'value': 'Your name'
        },
    },
    'description': 'Here goes the route description',
    'deprecated': False
})
class WithPathParameters(Resource):

    def post(self, name):
        print(name)
        return {
            'data': name
        }


@api.route('/body', doc={
    'description': 'Here goes the route description',
    'deprecated': False
})
class WithBody(Resource):

    @api.expect(book_model)
    def post(self):
        print(api.payload)
        return api.payload
