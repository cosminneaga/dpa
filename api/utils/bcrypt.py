import bcrypt

class Hash:

    def make(self, password):
        bytes = password.encode('utf-8')
        encode = bcrypt.hashpw(bytes, bcrypt.gensalt())
        return encode.decode('utf-8')

    def compare(self, password, hash):
        passwordBytes = password.encode('utf-8')
        hashBytes = hash.encode('utf-8')
        return bcrypt.checkpw(passwordBytes, hashBytes)