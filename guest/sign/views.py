from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    # return HttpResponse("Hello Django!")
    return render(request, 'index.html')


def login_action(request):
    if  request.method == "POST":
        username = request.POST.get("username", "") # ""可指定显示的默认值,如未设定则会提示Keyerror。 为GET请求时不会报错，返回None
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        print("is",user)
        if user is not None:
            login(request, user)  # 登录
            request.session['user'] = username
            # response.set_cookie('user', username, 3600)  # 添加浏览器cookie
            response = HttpResponseRedirect("/event_manage/")
            return response
        else:
            return render(request, "index.html", {'error': "username or password error!!"})
    else:
        return render(request, "index.html", {'error': "username or password error!"})


@login_required
def event_manage(request):
    # username = request.COOKIES.get('user', '')  # 读取浏览器cookie
    username = request.session.get('user', '')
    return render(request, "event_manage.html", {"user": username})

def logout_view(request):
    logout(request)
