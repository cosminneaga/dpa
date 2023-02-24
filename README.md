# Docker Python APIS

## Formatters

> **WARNING: Formatters must be runned everytime before uploading the code to CI!!!**

> If docker command will be used to format the code no dependencies are needed to be installed on local PC, otherwise check following links
> https://www.python.org/, https://pip.pypa.io/en/stable/installation/, https://pypi.org/project/autopep8/, https://nodejs.org/en/, https://nodejs.org/dist/v18.14.2/

### API
```bash
docker compose exec dpa-api bash formatter.sh
```

### Blogger
```bash
docker compose exec dpa-blogger npm run lint:fix
```
```bash
docker compose exec dpa-blogger npm run prettier:fix
```

## Links
- https://dpa.cosminneaga.dev/docs
- https://blogger.cosminneaga.dev/

## Credentials
### Blogger
- username:
```bash
blogger-init-user@gmail.com
```
- password:
```bash
DPA1blogger@INIT#user/2022
```

## Local Setup

**Install NodeJs ^v18**
https://nodejs.org/en/, https://nodejs.org/dist/v18.14.2/

**Download & Install Docker**
https://docs.docker.com/engine/install/

```bash
cp example.build_local.sh build_local.sh
```

**Uncomment following lines from file build_local.sh**

![local_build.png](./local_build.png)

```bash
bash build_local.sh
```


| Name             | Url                                                |
| ---------------- | -------------------------------------------------- |
| Database         | Compass<br>`mongodb://root:example@localhost:8100` |
| Backend          | `localhost:8080/docs`                              |
| Frontend Blogger | preview: `localhost:81`<br> dev: `localhost:1000`  |


# Dependecies Docs

## API

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

## Blogger

Vuetify
-   https://next.vuetifyjs.com/en/getting-started/installation/

Vue3 Toastify
-   https://github.com/jerrywu001/vue3-toastify

Quill
-   https://vueup.github.io/vue-quill/guide/installation.html#cdn
-   https://www.npmjs.com/package/quill
-   https://quilljs.com/docs/quickstart/

Vue Cookies
-   https://github.com/cmp-cc/vue-cookies#readme

PrismJs
-   https://prismjs.com/
-   https://dev.to/kevin_odongo35/add-prism-js-to-a-vue-application-3e9p

Kothing
-   https://github.com/kothing/kothing-Editor#install
-   https://kothing.github.io/editor/html/getting-started.html

Prism
-   https://prismjs.com/#supported-languages
-   https://medium.com/@alexgwebdev/beautiful-code-highlighter-as-vue-js-component-397ded532ef2

Axios
- https://axios-http.com/docs/intro

Pinia
- https://pinia.vuejs.org/

MDI Icons
- https://www.npmjs.com/package/@mdi/font

TypeScript
- https://www.typescriptlang.org/

Not used yet but nice to be included VueUse
- https://vueuse.org/