from dotenv import dotenv_values


def env_val(prop=None):
    if(prop):
        return dotenv_values('.env')[prop]
    else:
        return dotenv_values('.env')