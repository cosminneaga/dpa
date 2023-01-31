from email_validator import validate_email, EmailNotValidError


class Validator:

    def validate_email(self, string):

        try:
            validate_email(string).email
            return (True, string)

        except EmailNotValidError as e:
            raise Exception(str(e))
