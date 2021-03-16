import os
import pandas as pd
from collections import defaultdict
from django.shortcuts import render
from django.contrib import messages
from Megatron import settings
from user.forms import LoginFrom
from .models import firstFileContent
from t.models import *
from .forms import describeFrom


# from Megatron.settings import BASE_DIR


# Create your views here.

def fileProofread(df, dic):
    real_column_index = []  # 用于存放excel中需要读取的列号
    real_column = []  # 用于存放excel中需要读取的列的循序，并以数据库中的字段名进行更正！
    columnList = []
    for key in dic.keys():
        columnList.append(key)

    for i in range(len(df.columns)):
        #    print(df.columns[i])
        for (key, val) in dic.items():
            if df.columns[i] in val and key in columnList:
                real_column.append(key)
                real_column_index.append(i)
                columnList.remove(key)
    return real_column_index, real_column, columnList


def compareStandard(num, floor, upper):
    if num > upper:
        return '(高)'
    if num < floor:
        return '(低)'
    return ''


def uploadFileInit(request):
    describe_form = describeFrom()
    content = {'describe_form': describe_form, 'form_title': '信息上传', 'page_title': '欢迎'}
    return render(request, 'fileTest/uploadFIleTest.html', content)


def uploadFileTest_result(request):
    # context = {}

    describe_form = describeFrom()
    context = {'describe_form': describe_form, 'form_title': '信息上传'}
    # return_to = reverse('upload_data')
    if request.method == 'POST':
        dic = defaultdict(list)
        dic['result_id'] += ['结果编号', 'result_id']
        dic['patient_id'] += ['患者编号', 'patient_id']
        dic['result_comment'] += ['患者状况', 'result_comment']
        dic['enabled'] += ['有效', 'enabled']
        dic['deleted'] += ["无效", 'deleted']
        dic['created_time'] += ['入院时间', 'created_time']
        dic['updated_time'] += ["出院时间", 'updated_time']

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

                    df = pd.read_excel(settings.UPLOAD_ROOT + "/" + filename.name)  # 这个会直接默认读取到这个Excel的第一个表单

                    real_column_index = []  # 用于存放excel中需要读取的列号
                    real_column = []  # 用于存放excel中需要读取的列的循序，并以数据库中的字段名进行更正！
                    columnList = ['result_id', 'patient_id', 'result_comment', 'enabled', 'deleted', 'created_time'
                        , 'updated_time']

                    for i in range(len(df.columns)):
                        #    print(df.columns[i])
                        for (key, val) in dic.items():
                            if df.columns[i] in val and key in columnList:
                                real_column.append(key)
                                real_column_index.append(i)
                                columnList.remove(key)

                    if columnList:  # 判断所需要的字段是否都已经读进来了
                        messages.error(request, '缺乏关键信息！' + str(columnList))
                    df_real = pd.read_excel(settings.UPLOAD_ROOT + "/" + filename.name
                                            , usecols=real_column_index, names=real_column)
                    # usecols 用于放需要哪些列
                    # names 用于自定义列名

                    for i in range(len(df_real)):
                        tmp = result.objects.create(result_id=df_real['result_id'][i],
                                                    patient_id=df_real['patient_id'][i],
                                                    result_comment=df_real['result_comment'][i],
                                                    enabled=df_real['enabled'][i],
                                                    deleted=df_real['deleted'][i],
                                                    created_time=df_real['created_time'][i],
                                                    updated_time=df_real['updated_time'][i])
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
        dic = defaultdict(list)
        dic['patient_id'] += ['患者编号', 'patient_id']
        dic['patient_name'] += ['患者姓名', 'patient_name']
        dic['gender'] += ['性别', 'gender']
        dic['birth'] += ['生日', 'birth']
        dic['age'] += ["年龄", 'age']
        dic['enabled'] += ['有效', 'enabled']
        dic['created_time'] += ["入院时间", 'created_time']
        dic['deleted'] += ["无效", 'deleted']

        dic['updated_time'] += ["出院时间", 'updated_time']

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

                    # real_column_index = []  # 用于存放excel中需要读取的列号
                    # real_column = []  # 用于存放excel中需要读取的列的循序，并以数据库中的字段名进行更正！
                    # columnList = []
                    # for key in dic.keys():
                    #     columnList.append(key)
                    #
                    # for i in range(len(df.columns)):
                    #     #    print(df.columns[i])
                    #     for (key, val) in dic.items():
                    #         if df.columns[i] in val and key in columnList:
                    #             real_column.append(key)
                    #             real_column_index.append(i)
                    #             columnList.remove(key)

                    # return real_column_index, real_column, columnList
                    real_column_index, real_column, columnList = fileProofread(df, dic)  # 调用fileProofread()

                    if columnList:  # 判断所需要的字段是否都已经读进来了
                        messages.error(request, '缺乏关键信息！' + str(columnList))
                    df_real = pd.read_excel(settings.UPLOAD_ROOT + "/" + filename.name
                                            , usecols=real_column_index, names=real_column)

                    for i in range(len(df_real)):
                        tmp = patient.objects.create(patient_id=df_real['patient_id'][i],
                                                     patient_name=df_real['patient_name'][i],
                                                     gender=df_real['gender'][i], birth=df_real['birth'][i],
                                                     age=df_real['age'][i],
                                                     enabled=df_real['enabled'][i], deleted=df_real['deleted'][i],
                                                     created_time=df_real['created_time'][i],
                                                     updated_time=df_real['updated_time'][i])
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
        dic = defaultdict(list)
        dic['department_id'] += ['科室编号', 'department_id']
        dic['patient_id'] += ['患者编号', 'patient_id']
        dic['department_name'] += ['性别', 'gender']
        dic['department_address'] += ['科室地址', 'department_address']
        dic['enabled'] += ["有效", 'enabled']
        dic['deleted'] += ['无效', 'deleted']
        dic['created_time'] += ["入院时间", 'created_time']
        # dic['deleted'] += ["无效", 'deleted']

        dic['updated_time'] += ["出院时间", 'updated_time']
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
                    real_column_index, real_column, columnList = fileProofread(df, dic)  # 调用fileProofread()

                    if columnList:  # 判断所需要的字段是否都已经读进来了
                        messages.error(request, '缺乏关键信息！' + str(columnList))
                    df_real = pd.read_excel(settings.UPLOAD_ROOT + "/" + filename.name
                                            , usecols=real_column_index, names=real_column)
                    for i in range(len(df_real)):
                        tmp = department.objects.create(department_id=df_real['department_id'][i],
                                                        patient_id=df_real['patient_id'][i],
                                                        department_name=df_real['department_name'][i],
                                                        department_address=df_real['department_address'][i],
                                                        enabled=df_real['enabled'][i], deleted=df_real['deleted'][i],
                                                        created_time=df_real['created_time'][i],
                                                        updated_time=df_real['updated_time'][i])
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
        dic = defaultdict(list)
        dic['illness_id'] += ['疾病编号', 'illness_id']
        dic['patient_id'] += ['患者编号', 'patient_id']
        dic['illness_name'] += ['疾病名', 'illness_name']
        dic['blood_sugar'] += ['患者血糖', 'blood_sugar']
        dic['blood_pressure'] += ["患者血压", 'blood_pressure']
        dic['blood_fat'] += ["患者血脂", 'blood_fat']
        dic['comment'] += ["状况", 'comment']
        dic['enabled'] += ['有效', 'enabled']
        dic['deleted'] += ['无效', 'deleted']

        dic['updated_time'] += ["出院时间", 'updated_time']
        dic['created_time'] += ['入院时间', 'created_time']

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
                    df = pd.read_excel(settings.UPLOAD_ROOT + "/" + filename.name)  # 这个会直接默认读取到这个Excel的第一个表单

                    real_column_index, real_column, columnList = fileProofread(df, dic)  # 调用fileProofread(), 方便修改

                    if columnList:  # 判断所需要的字段是否都已经读进来了
                        messages.error(request, '缺乏关键信息！' + str(columnList))
                    df_real = pd.read_excel(settings.UPLOAD_ROOT + "/" + filename.name
                                            , usecols=real_column_index, names=real_column)

                    for i in range(len(df_real)):
                        blood_sugar_tmp = pd.to_numeric(df_real['blood_sugar'][i])
                        # blood_pressure_tmp = pd.to_numeric(df_real['blood_pressure'][i])
                        blood_fat_tmp = pd.to_numeric(df_real['blood_fat'][i])

                        blood_sugar = str(df_real['blood_sugar'][i]) + compareStandard(blood_sugar_tmp, 3.9, 7.8)
                        blood_fat = str(df_real['blood_fat'][i]) + compareStandard(blood_fat_tmp, 2.8, 5.17)

                        tmp = illness.objects.create(illness_id=df_real['illness_id'][i],
                                                     patient_id=df_real['patient_id'][i],
                                                     illness_name=df_real['illness_name'][i],
                                                     blood_sugar=blood_sugar,
                                                     blood_pressure=df_real['blood_pressure'][i],
                                                     blood_fat=blood_fat,
                                                     comment=df_real['comment'][i],
                                                     enabled=df_real['enabled'][i],
                                                     deleted=df_real['deleted'][i],
                                                     created_time=df_real['created_time'][i],
                                                     updated_time=df_real['updated_time'][i])

                        # dic['blood_sugar'] += ['患者血糖', 'blood_sugar']
                        # dic['blood_pressure'] += ["患者血压", 'blood_pressure']
                        # dic['blood_fat'] += ["患者血脂", 'blood_fat']
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
        dic = defaultdict(list)
        dic['treatment_id'] += ['诊疗方法编号', 'treatment_id']
        dic['patient_id'] += ['患者编号', 'patient_id']
        dic['treatment_name'] += ['诊疗方法', 'treatment_name']
        dic['comment'] += ['诊疗评论', 'comment']
        dic['updated_time'] += ["出院时间", 'updated_time']
        dic['created_time'] += ['入院时间', 'created_time']
        dic['deleted'] += ['无效', 'deleted']
        dic['enabled'] += ['有效', 'enabled']

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
                    real_column_index, real_column, columnList = fileProofread(df, dic)  # 调用fileProofread(), 方便修改

                    if columnList:  # 判断所需要的字段是否都已经读进来了
                        messages.error(request, '缺乏关键信息！' + str(columnList))
                    df_real = pd.read_excel(settings.UPLOAD_ROOT + "/" + filename.name
                                            , usecols=real_column_index, names=real_column)
                    for i in range(len(df_real)):
                        tmp = treatment.objects.create(treatment_id=df_real['treatment_id'][i],
                                                       patient_id=df_real['patient_id'][i],
                                                       treatment_name=df_real['treatment_name'][i],
                                                       comment=df_real['comment'][i],
                                                       enabled=df_real['enabled'][i], deleted=df_real['deleted'][i],
                                                       created_time=df_real['created_time'][i],
                                                       updated_time=df_real['updated_time'][i])
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
