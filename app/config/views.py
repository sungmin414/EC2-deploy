from django.shortcuts import render


def index(request):
    # TEMPLATE설정에 app/templates폴더 추가
    # template폴더에 'index.html'추가

    # STATICFILES_DIRS에 app/static폴더 추가
    # static폴더에 BOOTSTRAP CSS파일 (css/bootstrap.css)추가

    # index.html에서 {% static %}태그를 사용해서
    # head태그 내의 link태그에 css/bootstrap.css를 불러오기
    return render(request, 'index.html')