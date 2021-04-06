from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegisterForm


def index(request):
    return HttpResponse("hello")


def admin_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form_r = form.save()
            form_r.is_admin = True
            form_r.set_password(form_r.password)
            form_r.save()
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/admin_register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active and user.is_user:
                login(request, user)
                return HttpResponse("hello User")
            elif user.is_active and user.is_admin:
                login(request, user)
                return HttpResponse("hello admin")
            else:
                return HttpResponse('no active user')
        else:
            return HttpResponse('no user present')
    else:
        return render(request, 'accounts/admin_login.html', {})