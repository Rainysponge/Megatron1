import os
import pandas as pd
from django.shortcuts import render
from django.contrib import messages
from Megatron import settings
from user.forms import LoginFrom
from .models import firstFileContent
from t.models import *
from .forms import describeFrom


# from Megatron.settings import BASE_DIR


# Create your views here.

def uploadFileInit(request):
    describe_form = describeFrom()
    content = {'describe_form': describe_form, 'form_title': '信息上传'}
    # context['page_title'] = '欢迎'
    return render(request, 'fileTest/uploadFIleTest.html', content)


def uploadFileTest_result(request):
    # context = {}

    describe_form = describeFrom()
    context = {'describe_form': describe_form, 'form_title': '信息上传'}
    # return_to = reverse('upload_data')
    if request.method == 'POST':
        filename = request.FILES.get('file', '')
        if os.path.exists(settings.UPLOAD_ROOT + "/" + filename.name):
            messages.error(request, '文件已经存在，请不要重复导入！')
            return render(request, "fileTest/uploadFIleTest.html", context)
        if filename:
            excel_type = filename.name.split('.')[1]

            # 上传文件格式限制
            if excel_type in ['xlsx', 'xls']:
                # 如果文件夹不存在，创建upload文件夹
                if not os.path.exists(settings.UPLOAD_ROOT):
                    os.makedirs(settings.UPLOAD_ROOT)
                try:
                    # 循环二进制写入
                    with open(settings.UPLOAD_ROOT + "/" + filename.name, 'wb') as f:
                        for i in filename.readlines():
                            f.write(i)
                    request.session['file_root'] = '../upload' + '/' + filename.name
                    # with open(settings.UPLOAD_ROOT + "/" + filename.name, 'wb') as f:
                    df = pd.read_excel(settings.UPLOAD_ROOT + "/" + filename.name)  # 这个会直接默认读取到这个Excel的第一个表单
                    # data = df.head()  # 默认读取前5行的数据
                    # for i in range(len(df)):
                    #     tmp = firstFileContent.objects.create(firstField=df['firstField'][i],
                    #                                           secondField=df['secondField'][i])
                    #     tmp.save()
                    for i in range(len(df)):
                        tmp = result.objects.create(result_id=df['result_id'][i],
                                                    patient_id=df['patient_id'][i],
                                                    result_comment=df['result_comment'][i],
                                                    enabled=df['enabled'][i],
                                                    deleted=df['deleted'][i],
                                                    created_time=df['created_time'][i],
                                                    updated_time=df['updated_time'][i])
                        tmp.save()

                    messages.success(request, '数据导入成功')

                except Exception as e:
                    messages.error(request, '数据读入失败:' + str(e))
            else:
                messages.error(request, '文件类型错误')

        else:
            messages.error(request, '上传文件不能为空')

    return render(request, "fileTest/uploadFIleTest.html", context)


def uploadFileTest_patient(request):
    context = {}
    context['flag'] = ''
    # return_to = reverse('upload_data')
    if request.method == 'POST':
        filename = request.FILES.get('file', '')
        if os.path.exists(settings.UPLOAD_ROOT + "/" + filename.name):
            messages.error(request, '文件已经存在，请不要重复导入！')
            return render(request, "fileTest/uploadFIleTest.html", context)
        if filename:
            excel_type = filename.name.split('.')[1]

            # 上传文件格式限制
            if excel_type in ['xlsx', 'xls']:
                # 如果文件夹不存在，创建upload文件夹
                if not os.path.exists(settings.UPLOAD_ROOT):
                    os.makedirs(settings.UPLOAD_ROOT)
                try:
                    # 循环二进制写入
                    with open(settings.UPLOAD_ROOT + "/" + filename.name, 'wb') as f:
                        for i in filename.readlines():
                            f.write(i)
                    request.session['file_root'] = '../upload' + '/' + filename.name
                    # with open(settings.UPLOAD_ROOT + "/" + filename.name, 'wb') as f:
                    df = pd.read_excel(settings.UPLOAD_ROOT + "/" + filename.name)  # 这个会直接默认读取到这个Excel的第一个表单
                    # data = df.head()  # 默认读取前5行的数据
                    # for i in range(len(df)):
                    #     tmp = firstFileContent.objects.create(firstField=df['firstField'][i],
                    #                                           secondField=df['secondField'][i])
                    #     tmp.save()
                    for i in range(len(df)):
                        tmp = patient.objects.create(patient_id=df['patient_id'][i], patient_name=df['patient_name'][i],
                                                     gender=df['gender'][i], birth=df['birth'][i], age=df['age'][i],
                                                     enabled=df['enabled'][i], deleted=df['deleted'][i],
                                                     created_time=df['created_time'][i],
                                                     updated_time=df['updated_time'][i])
                        tmp.save()

                    messages.success(request, '数据导入成功')




                except Exception as e:
                    messages.error(request, '数据读入失败:' + str(e))
            else:
                messages.error(request, '文件类型错误')

        else:
            messages.error(request, '上传文件不能为空')

    return render(request, "fileTest/uploadFIleTest.html", context)


def uploadFileTest_department(request):
    context = {}
    context['flag'] = ''
    # return_to = reverse('upload_data')
    if request.method == 'POST':
        filename = request.FILES.get('file', '')
        if os.path.exists(settings.UPLOAD_ROOT + "/" + filename.name):
            messages.error(request, '文件已经存在，请不要重复导入！')
            return render(request, "fileTest/uploadFIleTest.html", context)
        if filename:
            excel_type = filename.name.split('.')[1]

            # 上传文件格式限制
            if excel_type in ['xlsx', 'xls']:
                # 如果文件夹不存在，创建upload文件夹
                if not os.path.exists(settings.UPLOAD_ROOT):
                    os.makedirs(settings.UPLOAD_ROOT)
                try:
                    # 循环二进制写入
                    with open(settings.UPLOAD_ROOT + "/" + filename.name, 'wb') as f:
                        for i in filename.readlines():
                            f.write(i)
                    request.session['file_root'] = '../upload' + '/' + filename.name
                    # with open(settings.UPLOAD_ROOT + "/" + filename.name, 'wb') as f:
                    df = pd.read_excel(settings.UPLOAD_ROOT + "/" + filename.name)  # 这个会直接默认读取到这个Excel的第一个表单
                    # data = df.head()  # 默认读取前5行的数据
                    # for i in range(len(df)):
                    #     tmp = firstFileContent.objects.create(firstField=df['firstField'][i],
                    #                                           secondField=df['secondField'][i])
                    #     tmp.save()
                    for i in range(len(df)):
                        tmp = department.objects.create(department_id=df['department_id'][i],
                                                        patient_id=df['patient_id'][i],
                                                        department_name=df['department_name'][i],
                                                        department_address=df['department_address'][i],
                                                        enabled=df['enabled'][i], deleted=df['deleted'][i],
                                                        created_time=df['created_time'][i],
                                                        updated_time=df['updated_time'][i])
                        tmp.save()

                    messages.success(request, '数据导入成功')




                except Exception as e:
                    messages.error(request, '数据读入失败:' + str(e))
            else:
                messages.error(request, '文件类型错误')

        else:
            messages.error(request, '上传文件不能为空')

    return render(request, "fileTest/uploadFIleTest.html", context)


def uploadFileTest_illness(request):
    context = {}
    context['flag'] = ''
    # return_to = reverse('upload_data')
    if request.method == 'POST':
        filename = request.FILES.get('file', '')
        if os.path.exists(settings.UPLOAD_ROOT + "/" + filename.name):
            messages.error(request, '文件已经存在，请不要重复导入！')
            return render(request, "fileTest/uploadFIleTest.html", context)
        if filename:
            excel_type = filename.name.split('.')[1]

            # 上传文件格式限制
            if excel_type in ['xlsx', 'xls']:
                # 如果文件夹不存在，创建upload文件夹
                if not os.path.exists(settings.UPLOAD_ROOT):
                    os.makedirs(settings.UPLOAD_ROOT)
                try:
                    # 循环二进制写入
                    with open(settings.UPLOAD_ROOT + "/" + filename.name, 'wb') as f:
                        for i in filename.readlines():
                            f.write(i)
                    request.session['file_root'] = '../upload' + '/' + filename.name
                    # with open(settings.UPLOAD_ROOT + "/" + filename.name, 'wb') as f:
                    df = pd.read_excel(settings.UPLOAD_ROOT + "/" + filename.name)  # 这个会直接默认读取到这个Excel的第一个表单
                    # data = df.head()  # 默认读取前5行的数据
                    # for i in range(len(df)):
                    #     tmp = firstFileContent.objects.create(firstField=df['firstField'][i],
                    #                                           secondField=df['secondField'][i])
                    #     tmp.save()
                    for i in range(len(df)):
                        tmp = illness.objects.create(illness_id=df['illness_id'][i], patient_id=df['patient_id'][i],
                                                     illness_name=df['illness_name'][i], comment=df['comment'][i],
                                                     enabled=df['enabled'][i], deleted=df['deleted'][i],
                                                     created_time=df['created_time'][i],
                                                     updated_time=df['updated_time'][i])
                        tmp.save()

                    messages.success(request, '数据导入成功')

                except Exception as e:
                    messages.error(request, '数据读入失败:' + str(e))
            else:
                messages.error(request, '文件类型错误')

        else:
            messages.error(request, '上传文件不能为空')

    return render(request, "fileTest/uploadFIleTest.html", context)


def uploadFileTest_treatment(request):
    context = {}
    context['flag'] = ''
    # return_to = reverse('upload_data')
    if request.method == 'POST':
        filename = request.FILES.get('file', '')
        if os.path.exists(settings.UPLOAD_ROOT + "/" + filename.name):
            messages.error(request, '文件已经存在，请不要重复导入！')
            return render(request, "fileTest/uploadFIleTest.html", context)
        if filename:
            excel_type = filename.name.split('.')[1]

            # 上传文件格式限制
            if excel_type in ['xlsx', 'xls']:
                # 如果文件夹不存在，创建upload文件夹
                if not os.path.exists(settings.UPLOAD_ROOT):
                    os.makedirs(settings.UPLOAD_ROOT)
                try:
                    # 循环二进制写入
                    with open(settings.UPLOAD_ROOT + "/" + filename.name, 'wb') as f:
                        for i in filename.readlines():
                            f.write(i)
                    request.session['file_root'] = '../upload' + '/' + filename.name
                    # with open(settings.UPLOAD_ROOT + "/" + filename.name, 'wb') as f:
                    df = pd.read_excel(settings.UPLOAD_ROOT + "/" + filename.name)  # 这个会直接默认读取到这个Excel的第一个表单
                    # data = df.head()  # 默认读取前5行的数据
                    # for i in range(len(df)):
                    #     tmp = firstFileContent.objects.create(firstField=df['firstField'][i],
                    #                                           secondField=df['secondField'][i])
                    #     tmp.save()
                    for i in range(len(df)):
                        tmp = treatment.objects.create(treatment_id=df['treatment_id'][i],
                                                       patient_id=df['patient_id'][i],
                                                       treatment_name=df['treatment_name'][i], comment=df['comment'][i],
                                                       enabled=df['enabled'][i], deleted=df['deleted'][i],
                                                       created_time=df['created_time'][i],
                                                       updated_time=df['updated_time'][i])
                        tmp.save()

                    messages.success(request, '数据导入成功')

                except Exception as e:
                    messages.error(request, '数据读入失败:' + str(e))
            else:
                messages.error(request, '文件类型错误')

        else:
            messages.error(request, '上传文件不能为空')

    return render(request, "fileTest/uploadFIleTest.html", context)


def describeFunc(request):
    if not request.user.is_authenticated:
        login_form = LoginFrom()

        context = {'login_form': login_form, 'form_title': '登录'}
        messages.error(request, '请先登录！')
        return render(request, 'user/login.html', context)
    if request.method == 'POST':
        describe_form = describeFrom(request.POST)
        if describe_form.is_valid():
            describeInfo = describe_form.cleaned_data['describeText']
            messages.error(request, describeInfo)
            content = {'describe_form': describe_form}
            return render(request, 'fileTest/uploadFIleTest.html', content)
    else:
        describe_form = describeFrom()
    content = {'describe_form': describe_form, 'form_title': '信息上传'}
    # context['page_title'] = '欢迎'
    return render(request, 'fileTest/uploadFIleTest.html', content)
