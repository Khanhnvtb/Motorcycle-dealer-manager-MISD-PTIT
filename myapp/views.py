from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Đăng nhập thành công")
            return redirect('/')
        else:
            messages.error(request, 'Tài khoản hoặc mật khẩu không chính xác')
            return redirect('login')
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')
