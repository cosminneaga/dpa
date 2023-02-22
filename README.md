# Docker Python APIS

## Formatters

> **WARNING: Formatters must be runned everytime before uploading the code to CI!!!**

> If docker command will be used to format the code no dependecies are needed to be installed on local PC, otherwise check following links
> https://www.python.org/, https://pip.pypa.io/en/stable/installation/, https://pypi.org/project/autopep8/, https://nodejs.org/en/, https://nodejs.org/dist/v18.14.2/


### Awesome Docker way
#### API
```bash
docker compose exec dpa-api bash formatter.sh
```

#### Blogger
```bash
docker compose exec blogger npm run lint
```
```bash
docker compose exec blogger npm run prettier:check
```

### Complicated like fuck local way (_not recommended_)
#### API
- Install Python https://www.python.org/
- Install Pip https://pip.pypa.io/en/stable/installation/
  - Easiest way to install pip:
    - Copy code from https://bootstrap.pypa.io/get-pip.py and create a file in your PC
    - Run the file `python <file-name.py>`
- Install Autopep8 with the command `pip install autopep8`
  - Change Directory to Api root's folder `cd blogger`
  - Manual
    - Run the formatter `find -type f -name '*.py' ! -path '*/migrations/*' -exec autopep8 --in-place --aggressive --aggressive '{}' \;`
    - Run pycodestyle `find -type f -name '*.py' ! -path '*/migrations/*' -exec pycodestyle --first '{}' \;`
  - Using the bash script provided
    - Run `bash formatter.sh`

#### Blogger
- Install NodeJS ^v18 https://nodejs.org/en/ https://nodejs.org/dist/v18.14.2/
- `cd blogger`
- `npm install`
- `npm run lint`
- `npm run prettier:fix`

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

## Install Docker
> Check this repository to install Docker on Linux
https://github.com/cosminneaga/helpers/tree/main/bash_scripts

## Local Setup

**Download Docker**
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
| Backend          | `localhost:8080/hello`                             |
| Frontend Blogger | preview: `localhost`<br> dev: `localhost:3000`     |
