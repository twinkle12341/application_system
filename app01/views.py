from django.shortcuts import render, redirect

from app01.models import UserInfo


# Create your views here.


def login(request):
    """
    登陆界面
    """
    if request.method == "GET":
        return render(request, 'login.html')

    name = request.POST.get('name')
    password = request.POST.get('password')

    result = UserInfo.objects.filter(name=name, password=password).first()
    if result:
        request.session["info"] = result.name
        return redirect("/home_page/")
    else:
        return render(request, 'login.html', {'error': '用户名或密码错误'})


def home_page(request):
    # 判断用户是否已登录，未登录跳转登录界面
    info_dict = request.session.get('info')
    if not info_dict:
        return redirect('/login/')

    return render(request, 'home_page.html')