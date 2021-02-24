from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import LoginFrom, RegForm
from .models import Profile, Doctor, Patient

# Create your views here.


def login(request):
    if request.method == 'POST':
        login_form = LoginFrom(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)

            context = {'log_massage': request.GET.get('from'), 'massage': '登陆成功'}
            # return redirect(request.GET.get('from', reverse('home')))
            return render(request, 'home.html', context)
    else:
        login_form = LoginFrom()

    context = {}
    # context['page_title'] = '欢迎'
    context['login_form'] = login_form
    context['form_title'] = '登录'
    return render(request, 'user/login.html', context)


def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)  # 创建用户
            real_name = reg_form.cleaned_data['real_name']
            sex = reg_form.cleaned_data['sex']

            user.save()
            profile = Profile.objects.create(user=user, sex=sex,
                                             real_name=real_name)
            profile.save()

            identity = reg_form.cleaned_data['identity']
            if identity == '医生':
                doctor = Doctor.objects.create(user=user)
                doctor.save()
            else:
                patient = Patient.objects.create(user=user)
                patient.save()

            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return render(request, 'home.html', {'massage': '恭喜你已经成功注册啦，赶紧试试吧！'})
    else:
        reg_form = RegForm()

    context = {}
    context['reg_form'] = reg_form
    context['form_title'] = '注册'
    return render(request, 'user/register.html', context)


def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from', reverse('home')))
