from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.models import User
from comment.forms import Search_Comment
from .forms import LoginFrom, RegForm, docRegForm, changeDocInfoForm
from .models import Profile, Doctor, Patient, Department


# Create your views here.


def login(request):
    if request.method == 'POST':
        login_form = LoginFrom(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            messages.error(request, '登陆成功！')
            context = {'log_massage': '登陆成功!',
                       'Search_Comment': Search_Comment()}
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

            # identity = reg_form.cleaned_data['identity']
            # if identity == '医生':
            #     doctor = Doctor.objects.create(user=user)
            #     doctor.save()
            # else:
            #     patient = Patient.objects.create(user=user)
            #     patient.save()

            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return render(request, 'home.html', {'massage': '恭喜你已经成功注册啦，赶紧试试吧！',
                                                 'Search_Comment': Search_Comment()})
    else:
        reg_form = RegForm()

    context = {}
    context['reg_form'] = reg_form
    context['form_title'] = '患者注册'
    return render(request, 'user/register.html', context)


def docRegister(request):
    if request.method == 'POST':
        reg_form = docRegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            password = reg_form.cleaned_data['password']
            email = reg_form.cleaned_data['email']

            user = User.objects.create_user(username, email, password)  # 创建用户
            real_name = reg_form.cleaned_data['real_name']
            sex = reg_form.cleaned_data['sex']

            user.save()
            profile = Profile.objects.create(user=user, sex=sex,
                                             real_name=real_name, is_doc=True)
            department = reg_form.cleaned_data['department']
            department0 = Department.objects.get(Department_name=department)
            doc = Doctor.objects.create(user=user, department=department0)

            doc.save()
            profile.save()
            user = auth.authenticate(username=username, password =password)
            auth.login(request, user)
            return render(request, 'home.html', {'massage': '恭喜你已经成功注册啦，赶紧试试吧！',
                                                 'Search_Comment': Search_Comment()})
    else:
        reg_form = docRegForm()

    context = {}
    context['reg_form'] = reg_form
    context['form_title'] = '医生身份注册'
    return render(request, 'user/docRegister.html', context)


def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from', reverse('home')))


def changeDocInfo(request):
    if not request.user.is_authenticated:
        login_form = LoginFrom()

        context = {'login_form': login_form, 'form_title': '登录'}
        messages.error(request, '请先登录！')
        return render(request, 'user/login.html', context)
    if request.method == 'POST':
        changeDocForm = changeDocInfoForm(request.POST)
        if changeDocForm.is_valid():
            user = request.user
            department = changeDocForm.cleaned_data['department']
            department0 = Department.objects.get(Department_name=department)

            doc = Doctor.objects.get(user=user)
            doc.department = department0
            doc.save()
            messages.error(request, '科室已更改为' + department)


    else:
        changeDocForm = changeDocInfoForm(request.POST)

    context = {}
    # context['page_title'] = '欢迎'
    context['change_doc_info_form'] = changeDocForm
    context['form_title'] = '更改部门'

    return render(request, 'user/changeDocInfo.html', context)









