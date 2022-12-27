from flask_restx import fields

class UserModel:

    def __init__(self, ns):
        self.__ns = ns

    def toRegisterModel(self):
        return self.__ns.model(
            'Register', {
                'first_name': fields.String('FirstName'),
                'last_name': fields.String('LastName'),
                'email': fields.String('user@gmail.com'),
                'password': fields.String('password')
            }
        )

    def toLoginModel(self):
        return self.__ns.model(
            'Login', {
                'email': fields.String('user@gmail.com'),
                'password': fields.String('password')
            }
        )