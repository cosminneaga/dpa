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
docker compose exec blogger npm run lint:fix
```
```bash
docker compose exec blogger npm run prettier:fix
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
DPAbloggerINITuser2022
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
