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


