from flask_restx import fields


class Model:

    def __init__(self, ns):
        self.__ns = ns

    def toModel(self):
        return self.__ns.model(
            'Example-Book',
            {
                'id': fields.Integer(),
                'title': fields.String(),
                'author': fields.String(),
                'date': fields.String(),
            }
        )