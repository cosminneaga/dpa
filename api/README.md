# Dpa Python API - Docker Python API

> Created with love in Python3.8

> Connected to a MongoDB server DPA will be able to store update data from different front-end projects added to this repo

## Dependencies

BCrypt -- encrypt passwords
- https://pypi.org/project/bcrypt/

BeatifulSoup4 & Soupieve -- web scrapers, HTML/CSS renderer
- https://pypi.org/project/beautifulsoup4/
- https://pypi.org/project/soupsieve/

Colorama -- colorful print
- https://pypi.org/project/colorama/

Flask -- development server
- https://flask.palletsprojects.com/en/2.2.x/

Flask-Restx -- Api Docs
- https://flask-restx.readthedocs.io/en/latest/

Gunicorn -- production server
- https://gunicorn.org/

Jinja2 -- Python in HTML
- https://pypi.org/project/Jinja2/

JsonSchema
- https://pypi.org/project/jsonschema/

py-console -- Colorful console print
- https://pypi.org/project/py-console/

PyJWT -- Json Web Token
- https://pypi.org/project/PyJWT/
- https://pyjwt.readthedocs.io/en/latest/

pymongo -- mongoDb
- https://pymongo.readthedocs.io/en/stable/

Python-DotENV -- env
- https://pypi.org/project/python-dotenv/

PyTZ -- datetime
- https://pypi.org/project/pytz/

TomLi
> I don't know waht use this library has and I don't care but will keep
- https://pypi.org/project/tomli/

Zipp
> I don't know waht use this library has and I don't care but will keep
- https://pypi.org/project/zipp/



## Setup commands
- `python -m venv ENV`
- `. ENV/Scripts/activate`
- `pip install -r requirements.txt`

## Server codes used
- 200 - OK
- 201 - Created
- 202 - Accepted
- 302 - Found
- 400 - Bad Request
- 401 - Unathorized
- 404 - Not Found

# Formatter
```bash
bash formatter.sh
```
```bash
docker compose exec dpa-api bash formatter.sh
```