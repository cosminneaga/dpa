from flask import Flask, send_file
from flask_restx import Api, Resource
from utils.env import env_val
from flask_cors import CORS

from src.blogger.namespace import api as bloggerNS
from src.example.namespace import api as exampleNS


app = Flask(__name__)
CORS(app)
app.config['ENV'] = 'development'
RESTX_ERROR_404_HELP=False

authorizations = {
    'api_key': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'x-access-token'
    }
}
api = Api(
    app,
    authorizations=authorizations,
    security='api_key',
    version='1.0',
    title='Array of Python APIs',
    description='This is an array of Python APIs',
    doc='/docs' if app.config['ENV'] == 'development' else False,
    ordered=True,
)


api.add_namespace(bloggerNS, path='/api/blogger')
api.add_namespace(exampleNS, path='/api/example')


@api.route('/favicon.ico')
class Favicon(Resource):
    def get(self):
        return send_file('assets/img/api.png', mimetype='image/gif')

@api.route('/hello')
class Home(Resource):
    def get(self):
        return "Welcome to Array of APIS written in Python 3.8"


if __name__ == '__main__' and app.config['ENV'] == 'development':
    app.run(host='0.0.0.0', port=8080, debug=True)
else:
    app.run(host='0.0.0.0', port=8080, debug=False)
