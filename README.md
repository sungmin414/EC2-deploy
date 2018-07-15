# Nginx - uWSGI - Django

**Web Server** <-> **WSGI** <-> **Web Application**

## Requiremnets

### Packages

- Python (3.6)
- pipenv


### Secrets

#### `/secrets/base.json`

```json
{
  "SECRET_KEY": "<Django secret key>"
}
```

#### `/secrets/dev.json`

- PostgreSQL을 사용, DATABASES섹션의 설정이 필요

```json
{
    "DATABASES": {
    "default": {
      "ENGINE": "django.db.backends.postgresql",
      "HOST": "test.c7l5lbue7qm1.ap-northeast-2.rds.amazonaws.com",
      "PORT": 5432,
      "USER": "<user>",
      "PASSWORD": "<password>",
      "NAME": "<db name>"
      }
    }
}

```



## Installation

```
pipenv install
pipenv shell
cd app
./manage.py runserver
```

## Nginx

### 웹 서버 설정

```
/etc/nginx/nginx.conf
```

- `user`: nginx 프로세스를 실행할 유저
- `daemon`: `off`로 나타낼 시, background가 아닌 foreground프로세스로 실행
    - `nginx -g 'daemon off;'` <- 이것과 같은 효과가 됨
 
### 운영 가능한 가상서버 (Virtual host)

A, B, C, D, E 5개의 서버정보가 있다면, `sites-available`폴더에 들어있음


