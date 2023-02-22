from flask import abort, request, render_template, Response
from utils.response import response
from .env import env_val
from jwt import encode, decode


def tokenize(data, secret):
    encoded = encode(data, secret, env_val('JWT_ALGORITHM'))
    return encoded


def detokenize(data, secret):
    decoded = decode(data, secret, env_val('JWT_ALGORITHM'))
    return decoded


# decorator function
def protect(function):
    def secure(self, *args, **kwargs):

        try:
            if 'X-Access-Token' not in request.headers:
                return response('Not Authorised', status=401)
            else:
                self.token = request.headers['X-Access-Token']
                self.decoded = decode(
                    self.token, self.secret, env_val('JWT_ALGORITHM'))
                self.isUser({
                    'email': self.decoded['email']
                }, 'if-exists')
        except Exception as e:
            abort(400, str(e))

        return function(self, *args, **kwargs)

    return secure


def protect_pages(function):
    def secure(self, *args, **kwargs):

        try:
            token = request.cookies.get('X-Access-Token')
            if not token:
                return Response(
                    render_template('401.html'),
                    mimetype='text/html',
                    status=401)
            else:
                self.token = token
                self.decoded = decode(
                    self.token, self.secret, env_val('JWT_ALGORITHM'))
                self.isUser({
                    'email': self.decoded['email']
                }, 'if-exists')

        except Exception as e:
            return Response(
                f'<h1>{str(e)}</h1>',
                mimetype='text/html',
                status=500)

        return function(self, *args, **kwargs)

    return secure
