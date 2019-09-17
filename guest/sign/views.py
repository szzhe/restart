from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from sign.models import Event, Guest


def index(request):
    # return HttpResponse("Hello Django!")
    return render(request, 'index.html')


def login_action(request):
    if  request.method == "POST":
        username = request.POST.get("username", "") # ""可指定显示的默认值,如未设定则会提示Keyerror。 为GET请求时不会报错，返回None
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
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
    event_list = Event.objects.all()
    # username = request.COOKIES.get('user', '')  # 读取浏览器cookie
    username = request.session.get('user', '')
    return render(request, "event_manage.html", {"user": username, "events":event_list})

@login_required
def event_search(request):
    username = request.session.get('user', '')
    search_name = request.GET.get("name", "")
    search_name_bytes = search_name.encode(encoding="utf-8")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {"user": username, "events": event_list})

@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    return render(request, "guest_manage.html", {"user": username, "guests": guest_list})

@login_required
def guest_search(request):
    username = request.session.get('user', '')
    search_realname = request.GET.get('realname', '')
    search_realname_bytes = search_realname.encode(encoding="utf-8")
    guest_list = Guest.objects.filter(realname__contains=search_realname)
    return render(request, "guest_manage.html", {"user": username, "guests": guest_list})

@login_required
def logout_view(request):
    logout(request)
    response = HttpResponseRedirect('/index/')
    return response
