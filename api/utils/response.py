from flask import abort, request


def response(message, data={}, code=200, status=True):

    if code == 200:
        return {
            'status': status,
            'message': message,
            'data': data,
        }
    elif code in (400, 404, 500, 401):
        abort(code, message)
