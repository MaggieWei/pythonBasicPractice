from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    return render(request, "index.html")


# 处理登录请求
def login_action(request):
    if request.method == "POST":
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登录
        # if username == "awin" and password == '123456':
        #     # return HttpResponseRedirect('/event_manage/')
            response = HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user', username, 3600)  # 添加浏览器cookie,set_cookie(Cookie名， 用户名，
            # # Cookie保留时间）
            request.session['user'] = username  # 将session信息记录到浏览器
            return response
        else:
            return render(request, "index.html", {'error': "用户名或者密码不正确"})


# 发布会管理
@login_required  # 若想限制某个视图需要登录才能查看，只需要在这个函数的前面加上@login_required装饰就可
def event_manage(request):
    event_list = Event.objects.all()
    # username = request.COOKIES.get('user', '')  # 读取浏览器cookie
    username = request.session.get('user', '')  # 读取浏览器session
    return render(request, "event_manage.html", {'user': username, 'events': event_list})

# 嘉宾管理
@login_required  # 若想限制某个视图需要登录才能查看，只需要在这个函数的前面加上@login_required装饰就可
def guest_manage(request):
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page取得不是整数，取第一页的数据
        contacts = paginator.page(1)
    except PageNotAnInteger:
        # 如果页码不在范围内，取最后一页
        contacts = paginator.page(paginator.num_pages)
    # username = request.COOKIES.get('user', '')  # 读取浏览器cookie
    username = request.session.get('user', '')  # 读取浏览器session
    return render(request, "guest_manage.html", {'user': username, 'guests': contacts})


@login_required
def search_name(request):
    username = request.session.get('user', '')  # 读取浏览器session
    search_name = request.GET.get('name', "")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {'user': username, 'events': event_list})

# 签到页面
@login_required
def sign_index(request, eid):
    event = get_object_or_404(Event, id=eid)
    return render(request, 'sign_index.html', {"event": event})


@login_required
def sign_index_action(request, eid):
    event = get_object_or_404(Event, id=eid)
    phone = request.POST.get("phone", "")
    print(phone)
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': '查无此号码.'})

    result = Guest.objects.filter(phone=phone, event_id=eid)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': '发布会id或手机号错误.'})

    result = Guest.objects.get(phone=phone, event_id=eid)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event, 'hint': '该用户已经签到'})
    else:
        Guest.objects.filter(phone=phone, event_id=eid).update(sign='1')
        return render(request, 'sign_index.html', {'event': event, 'hint': '签到成功', 'guest': result})


@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response
