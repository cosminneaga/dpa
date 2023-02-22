# Docker Python APIS

## Formatters

> If docker command will be used to format the code no dependecies are needed to be installed on local PC, otherwise check following links
> https://www.python.org/, https://pip.pypa.io/en/stable/installation/, https://pypi.org/project/autopep8/, https://nodejs.org/en/, https://nodejs.org/dist/v18.14.2/


### Awesome Docker way
#### API
- `docker compose exec dpa-api bash formatter.sh`

#### Blogger
- `docker compose exec blogger npm run lint`
- `docker compose exec blogger npm run prettier:check`

### Hard like fuck local way
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
- Blogger
- - username: blogger-init-user@gmail.com
- - password: DPAbloggerINITuser2022

## Install Docker
> Check this repository to install Docker on Linux
https://github.com/cosminneaga/helpers/tree/main/bash_scripts

## Local Setup

1. `bash build.sh`
2. `cd frontend/blogger` `npm install` `npm run dev`


| Name             | Url                                                |
| ---------------- | -------------------------------------------------- |
| Database         | Compass<br>`mongodb://root:example@localhost:8100` |
| Backend          | `localhost:8080/hello`                             |
| Frontend Blogger | preview: `localhost`<br> dev: `localhost:3000`     |
