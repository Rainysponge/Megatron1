import os
import re
import pandas as pd
from collections import defaultdict
from django.shortcuts import render
from django.contrib import messages
from django.utils import timezone
from Megatron import settings
from user.forms import LoginFrom
from user.models import Profile
from comment.forms import Search_Comment
from t.models import *
from .models import table_format, Patient_Information
from .forms import describeFrom, tResultSubmitForm, tDepartmentSubmitForm, tPatientSubmitForm, tTreatmentSubmitForm, \
    tIllnessSubmitForm, patientUpdateDataForm, searchPatientDailyForm


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
        table = table_format.objects.all()[0]
        dic_format = defaultdict(set)
        dic_format['result_id'] = set(table.result_id.split(','))
        dic_format['patient_id'] = set(table.patient_id.split(','))
        dic_format['result_comment'] = set(table.result_comment.split(','))
        dic_format['enabled'] = set(table.enabled.split(','))
        dic_format['deleted'] = set(table.deleted.split(','))
        dic_format['created_time'] = set(table.created_time.split(','))
        dic_format['updated_time'] = set(table.updated_time.split(','))

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
                    columnList = ['result_id', 'patient_id', 'result_comment', 'enabled', 'deleted', 'created_time',
                                  'updated_time']

                    for i in range(len(df.columns)):
                        #    print(df.columns[i])
                        for (key, val) in dic_format.items():
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
    describe_form = describeFrom()
    context = {'describe_form': describe_form, 'form_title': '信息上传', 'flag': ''}
    # return_to = reverse('upload_data')
    if request.method == 'POST':
        table = table_format.objects.all()[0]
        dic_format = defaultdict(set)
        dic_format['patient_name'] = set(table.patient_name.split(','))
        dic_format['patient_id'] = set(table.patient_id.split(','))
        dic_format['gender'] = set(table.gender.split(','))
        dic_format['birth'] = set(table.birth.split(','))
        dic_format['age'] = set(table.age.split(','))

        dic_format['enabled'] = set(table.enabled.split(','))
        dic_format['deleted'] = set(table.deleted.split(','))
        dic_format['created_time'] = set(table.created_time.split(','))
        dic_format['updated_time'] = set(table.updated_time.split(','))

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

                    real_column_index, real_column, columnList = fileProofread(df, dic_format)  # 调用fileProofread()
                    context['real_column_index'] = real_column_index
                    context['real_column'] = real_column
                    context['columnList'] = columnList
                    if columnList:  # 判断所需要的字段是否都已经读进来了
                        messages.error(request, '缺乏关键信息！' + str(columnList))
                    df_real = pd.read_excel(settings.UPLOAD_ROOT + "/" + filename.name
                                            , usecols=real_column_index, names=real_column)

                    for i in range(len(df_real)):
                        tmp = patient.objects.create(patient_id=df_real['patient_id'][i],
                                                     patient_name=df_real['patient_name'][i],
                                                     gender=df_real['gender'][i],
                                                     birth=df_real['birth'][i],
                                                     age=df_real['age'][i],
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


def uploadFileTest_department(request):
    context = {}
    context['flag'] = ''
    # return_to = reverse('upload_data')
    if request.method == 'POST':
        table = table_format.objects.all()[0]
        dic_format = defaultdict(set)
        dic_format['department_id'] = set(table.department_id.split(','))
        dic_format['patient_id'] = set(table.patient_id.split(','))
        dic_format['department_name'] = set(table.department_name.split(','))
        dic_format['department_address'] = set(table.department_address.split(','))

        dic_format['enabled'] = set(table.enabled.split(','))
        dic_format['deleted'] = set(table.deleted.split(','))
        dic_format['created_time'] = set(table.created_time.split(','))
        dic_format['updated_time'] = set(table.updated_time.split(','))

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
                    real_column_index, real_column, columnList = fileProofread(df, dic_format)  # 调用fileProofread()

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
        table = table_format.objects.all()[0]
        dic_format = defaultdict(set)
        dic_format['illness_id'] = set(table.department_id.split(','))
        dic_format['patient_id'] = set(table.patient_id.split(','))
        dic_format['illness_name'] = set(table.department_name.split(','))
        dic_format['blood_sugar'] = set(table.department_address.split(','))
        dic_format['blood_pressure'] = set(table.department_address.split(','))
        dic_format['blood_fat'] = set(table.department_address.split(','))
        dic_format['comment'] = set(table.department_address.split(','))

        dic_format['enabled'] = set(table.enabled.split(','))
        dic_format['deleted'] = set(table.deleted.split(','))
        dic_format['created_time'] = set(table.created_time.split(','))
        dic_format['updated_time'] = set(table.updated_time.split(','))

        # dic = defaultdict(list)
        # dic['illness_id'] += ['疾病编号', 'illness_id']
        # dic['patient_id'] += ['患者编号', 'patient_id']
        # dic['illness_name'] += ['疾病名', 'illness_name']
        # dic['blood_sugar'] += ['患者血糖', 'blood_sugar']
        # dic['blood_pressure'] += ["患者血压", 'blood_pressure']
        # dic['blood_fat'] += ["患者血脂", 'blood_fat']
        # dic['comment'] += ["状况", 'comment']
        # dic['enabled'] += ['有效', 'enabled']
        # dic['deleted'] += ['无效', 'deleted']
        #
        # dic['updated_time'] += ["出院时间", 'updated_time']
        # dic['created_time'] += ['入院时间', 'created_time']

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

                    real_column_index, real_column, columnList = fileProofread(df,
                                                                               dic_format)  # 调用fileProofread(), 方便修改

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

        table = table_format.objects.all()[0]
        dic_format = defaultdict(set)
        dic_format['treatment_id'] = set(table.department_id.split(','))
        dic_format['patient_id'] = set(table.patient_id.split(','))
        dic_format['treatment_name'] = set(table.department_name.split(','))
        dic_format['comment'] = set(table.department_address.split(','))

        dic_format['deleted'] = set(table.deleted.split(','))
        dic_format['enabled'] = set(table.enabled.split(','))

        dic_format['created_time'] = set(table.created_time.split(','))
        dic_format['updated_time'] = set(table.updated_time.split(','))

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
                    real_column_index, real_column, columnList = fileProofread(df, dic_format)
                    # 调用fileProofread(), 方便修改

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
    infoDict = defaultdict(str)
    if request.method == 'POST':
        describe_form = describeFrom(request.POST)
        if describe_form.is_valid():
            describeInfo = describe_form.cleaned_data['describeText']
            # 2000 - 12 - 10，患者王hh于早上8: 37
            # 前往我院就诊。王hh感到有发热，乏力的症状。其血压检查为高压：120，低压：80；肺部CT扫描结果为碎玻璃化。王hh首次核
            # 酸检验结果为阴性，第二次检验结果为阳性；患者确诊为新型冠状肺炎。本院采用1号中药的治疗方法，于2020 - 12 - 31，王
            # hh患者结果好转。
            describeInfo = describeInfo.replace('\n', '')
            describeInfo = describeInfo.replace(' ', '')
            time_pattern = re.compile('(\d{4}-\d{2}-\d{2})')
            name_pattern = re.compile('患者(.*)于.*([1-9][0-9]?[:|：][1-9][0-9]?)[前|来|到].*?')
            feel_pattern = re.compile('.*感[到|觉|受](.*?)的.*')
            blood_pressure_pattern = re.compile('高压.*[:|：]([0-9][0-9]*)[,|，].*低压.*[:|：]([1-9][0-9]*)')
            blood_sugar_pattern = re.compile('血糖.*?([1-9][0-9]*\.[0-9][0-9]*)')
            blood_fat_pattern = re.compile('血脂.*?([1-9][0-9]*\.[0-9][0-9]*)')
            testing_method_pattern = re.compile('[;|；](.*?)检测结果[为|是](.*?)[;|；|。]')
            treatment_method_pattern = re.compile('[采|使]用([1-9][0-9]*)号(.*?)[的|地]治疗[方|手]法')
            illness_pattern = re.compile('患者确诊[为|是](.*?)。')
            result_pattern = re.compile('结果(.*?)。')

            timeInfo = time_pattern.findall(describeInfo)
            nameInfo = name_pattern.findall(describeInfo)
            feelInfo = feel_pattern.findall(describeInfo)
            bloodPressureInfo = blood_pressure_pattern.findall(describeInfo)
            bloodSugarInfo = blood_sugar_pattern.findall(describeInfo)
            bloodFatInfo = blood_fat_pattern.findall(describeInfo)
            testingMethodInfo = testing_method_pattern.findall(describeInfo)
            treatmentMethodIfo = treatment_method_pattern.findall(describeInfo)
            illnessInfo = illness_pattern.findall(describeInfo)
            resultInfo = result_pattern.findall(describeInfo)

            infoDict['到院时间'] = timeInfo[0]
            infoDict['离院时间'] = timeInfo[-1] if len(timeInfo) >= 2 else '暂未离院'

            infoDict['患者姓名'] = nameInfo[0][0] if nameInfo else '未获取'
            infoDict['到院时间'] += ' ' + nameInfo[0][1] if len(nameInfo[0]) else ''
            infoDict['症状描述'] = feelInfo if feelInfo else '未获取'
            infoDict['血压'] = str(bloodPressureInfo) if bloodPressureInfo else '未获取'
            infoDict['血糖'] = bloodSugarInfo[0] if bloodSugarInfo else '未获取'
            infoDict['血脂'] = bloodFatInfo[0] if bloodFatInfo else '未获取'
            for i in range(len(testingMethodInfo)):
                infoDict['检测'] = testingMethodInfo[i][0] + '结果为' + testingMethodInfo[i][1] + ';'

                # infoDict['治疗手段'] = treatmentMethodIfo[0] + '号' + treatmentMethodIfo[1] if testingMethodInfo else '未获取'
            for i in range(len(treatmentMethodIfo)):
                infoDict['治疗手段'] += treatmentMethodIfo[i][0] + '号' + treatmentMethodIfo[i][1]

            infoDict['诊断结果'] = illnessInfo[0] if illnessInfo else '未获取'
            infoDict['治疗结果'] = resultInfo[-1] if resultInfo else '未获取'
            # infoDict['到院时间'] += nameInfo[1]

            messages.error(request, describeInfo)
            content = {'describe_form': describe_form, 'infoDict': dict(infoDict), 'describeInfo': describeInfo}
            return render(request, 'fileTest/uploadFIleTest.html', content)
    else:
        describe_form = describeFrom()
    content = {'describe_form': describe_form, 'form_title': '信息上传', 'infoDict': dict(infoDict)}
    # context['page_title'] = '欢迎'
    return render(request, 'fileTest/uploadFIleTest.html', content)


def tResultSubmit(request):
    if not request.user.is_authenticated:
        login_form = LoginFrom()

        context = {'login_form': login_form, 'form_title': '登录'}
        messages.error(request, '请先登录！')
        return render(request, 'user/login.html', context)
    dic = table_format.objects.all()[0]
    dic_format = defaultdict(set)
    dic_format['result_id'] = set(dic.result_id.split(','))
    dic_format['patient_id'] = set(dic.patient_id.split(','))
    dic_format['result_comment'] = set(dic.result_comment.split(','))
    dic_format['enabled'] = set(dic.enabled.split(','))
    dic_format['deleted'] = set(dic.deleted.split(','))
    dic_format['created_time'] = set(dic.created_time.split(','))
    dic_format['updated_time'] = set(dic.updated_time.split(','))
    if request.method == 'POST':
        t_result_submit_form = tResultSubmitForm(request.POST)
        if t_result_submit_form.is_valid():
            result_id = t_result_submit_form.cleaned_data['result_id']
            patient_id = t_result_submit_form.cleaned_data['patient_id']
            result_comment = t_result_submit_form.cleaned_data['result_comment']

            enabled = t_result_submit_form.cleaned_data['enabled']
            deleted = t_result_submit_form.cleaned_data['deleted']
            created_time = t_result_submit_form.cleaned_data['created_time']
            updated_time = t_result_submit_form.cleaned_data['updated_time']

            dic.result_id += (',' + result_id) if result_id else ''
            dic.patient_id += (',' + patient_id) if patient_id else ''
            dic.result_comment += (',' + result_comment) if result_comment else ''
            dic.enabled += (',' + enabled) if enabled else ''
            dic.deleted += (',' + deleted) if deleted else ''
            dic.created_time += (',' + created_time) if created_time else ''
            dic.updated_time += (',' + updated_time) if updated_time else ''

            dic.save()
            # t_result_submit_info = '123'
            messages.error(request, '更改格式成功！')
            content = {'t_result_submit_form': t_result_submit_form, 'dic_format': dict(dic_format)}
            return render(request, 'fileTest/upload_t_result.html', content)
    else:
        t_result_submit_form = tResultSubmitForm()
    content = {'t_result_submit_form': t_result_submit_form, 'form_title': '信息上传', 'dic_format': dict(dic_format)}
    # context['page_title'] = '欢迎'
    return render(request, 'fileTest/upload_t_result.html', content)


def tDepartmentSubmit(request):
    if not request.user.is_authenticated:
        login_form = LoginFrom()

        context = {'login_form': login_form, 'form_title': '登录'}
        messages.error(request, '请先登录！')
        return render(request, 'user/login.html', context)
    dic = table_format.objects.all()[0]
    dic_format = defaultdict(set)
    dic_format['department_id'] = set(dic.department_id.split(','))
    dic_format['patient_id'] = set(dic.patient_id.split(','))
    dic_format['department_name'] = set(dic.department_name.split(','))
    dic_format['department_address'] = set(dic.department_address.split(','))

    dic_format['enabled'] = set(dic.enabled.split(','))
    dic_format['deleted'] = set(dic.deleted.split(','))
    dic_format['created_time'] = set(dic.created_time.split(','))
    dic_format['updated_time'] = set(dic.updated_time.split(','))

    if request.method == 'POST':
        t_department_submit_form = tDepartmentSubmitForm(request.POST)
        if t_department_submit_form.is_valid():
            department_id = t_department_submit_form.cleaned_data['department_id']
            patient_id = t_department_submit_form.cleaned_data['patient_id']
            department_name = t_department_submit_form.cleaned_data['department_name']
            department_address = t_department_submit_form.cleaned_data['department_address']

            enabled = t_department_submit_form.cleaned_data['enabled']
            deleted = t_department_submit_form.cleaned_data['deleted']
            created_time = t_department_submit_form.cleaned_data['created_time']
            updated_time = t_department_submit_form.cleaned_data['updated_time']

            dic.department_id += (',' + department_id) if department_id else ''
            dic.patient_id += (',' + patient_id) if patient_id else ''
            dic.department_name += (',' + department_name) if department_name else ''
            dic.department_address += (',' + department_address) if department_address else ''
            dic.enabled += (',' + enabled) if enabled else ''
            dic.deleted += (',' + deleted) if deleted else ''
            dic.created_time += (',' + created_time) if created_time else ''
            dic.updated_time += (',' + updated_time) if updated_time else ''

            dic.save()
            # t_result_submit_info = '123'

            messages.error(request, '更改格式成功！')
            content = {'t_department_submit_form': t_department_submit_form, 'dic_format': dict(dic_format)}
            return render(request, 'fileTest/upload_t_department.html', content)
    else:
        t_department_submit_form = tDepartmentSubmitForm()
    content = {'t_department_submit_form': t_department_submit_form, 'form_title': '信息上传',
               'dic_format': dict(dic_format)}
    # context['page_title'] = '欢迎'
    return render(request, 'fileTest/upload_t_department.html', content)


def tPatientSubmit(request):
    if not request.user.is_authenticated:
        login_form = LoginFrom()

        context = {'login_form': login_form, 'form_title': '登录'}
        messages.error(request, '请先登录！')
        return render(request, 'user/login.html', context)
    dic = table_format.objects.all()[0]
    dic_format = defaultdict(set)
    dic_format['patient_name'] = set(dic.patient_name.split(','))
    dic_format['patient_id'] = set(dic.patient_id.split(','))
    dic_format['gender'] = set(dic.gender.split(','))
    dic_format['birth'] = set(dic.birth.split(','))
    dic_format['age'] = set(dic.age.split(','))

    dic_format['enabled'] = set(dic.enabled.split(','))
    dic_format['deleted'] = set(dic.deleted.split(','))
    dic_format['created_time'] = set(dic.created_time.split(','))
    dic_format['updated_time'] = set(dic.updated_time.split(','))

    if request.method == 'POST':
        t_patient_submit_form = tPatientSubmitForm(request.POST)
        if t_patient_submit_form.is_valid():
            patient_name = t_patient_submit_form.cleaned_data['patient_name']
            patient_id = t_patient_submit_form.cleaned_data['patient_id']
            gender = t_patient_submit_form.cleaned_data['gender']
            birth = t_patient_submit_form.cleaned_data['birth']
            age = t_patient_submit_form.cleaned_data['age']

            updated_time = t_patient_submit_form.cleaned_data['updated_time']
            deleted = t_patient_submit_form.cleaned_data['deleted']
            created_time = t_patient_submit_form.cleaned_data['created_time']
            enabled = t_patient_submit_form.cleaned_data['enabled']

            dic.patient_name += (',' + patient_name) if patient_name else ''
            dic.patient_id += (',' + patient_id) if patient_id else ''
            dic.gender += (',' + gender) if gender else ''
            dic.birth += (',' + birth) if birth else ''
            dic.age += (',' + age) if age else ''

            dic.enabled += (',' + enabled) if enabled else ''
            dic.deleted += (',' + deleted) if deleted else ''
            dic.created_time += (',' + created_time) if created_time else ''
            dic.updated_time += (',' + updated_time) if updated_time else ''

            dic.save()
            # t_result_submit_info = '123'
            messages.error(request, '更改格式成功！')
            content = {'t_patient_submit_form': t_patient_submit_form, 'dic_format': dict(dic_format)}
            return render(request, 'fileTest/upload_t_patient.html', content)
    else:
        t_patient_submit_form = tPatientSubmitForm()
    content = {'t_patient_submit_form': t_patient_submit_form, 'form_title': '信息上传', 'dic_format': dict(dic_format)}
    # context['page_title'] = '欢迎'
    return render(request, 'fileTest/upload_t_patient.html', content)


def tTreatmentSubmit(request):
    if not request.user.is_authenticated:
        login_form = LoginFrom()

        context = {'login_form': login_form, 'form_title': '登录'}
        messages.error(request, '请先登录！')
        return render(request, 'user/login.html', context)
    dic = table_format.objects.all()[0]
    dic_format = defaultdict(set)
    dic_format['treatment_id'] = set(dic.department_id.split(','))
    dic_format['patient_id'] = set(dic.patient_id.split(','))
    dic_format['treatment_name'] = set(dic.department_name.split(','))
    dic_format['comment'] = set(dic.department_address.split(','))

    dic_format['deleted'] = set(dic.deleted.split(','))
    dic_format['enabled'] = set(dic.enabled.split(','))

    dic_format['created_time'] = set(dic.created_time.split(','))
    dic_format['updated_time'] = set(dic.updated_time.split(','))
    if request.method == 'POST':
        t_treatment_submit_form = tTreatmentSubmitForm(request.POST)
        if t_treatment_submit_form.is_valid():
            treatment_id = t_treatment_submit_form.cleaned_data['treatment_id']
            patient_id = t_treatment_submit_form.cleaned_data['patient_id']
            treatment_name = t_treatment_submit_form.cleaned_data['treatment_name']
            comment = t_treatment_submit_form.cleaned_data['comment']

            updated_time = t_treatment_submit_form.cleaned_data['updated_time']
            deleted = t_treatment_submit_form.cleaned_data['deleted']
            created_time = t_treatment_submit_form.cleaned_data['created_time']
            enabled = t_treatment_submit_form.cleaned_data['enabled']
            #
            dic.patient_name += (',' + treatment_id) if treatment_id else ''
            dic.patient_id += (',' + patient_id) if patient_id else ''
            dic.gender += (',' + treatment_name) if treatment_name else ''
            dic.birth += (',' + comment) if comment else ''

            dic.enabled += (',' + enabled) if enabled else ''
            dic.deleted += (',' + deleted) if deleted else ''
            dic.created_time += (',' + created_time) if created_time else ''
            dic.updated_time += (',' + updated_time) if updated_time else ''

            dic.save()
            # t_result_submit_info = '123'
            messages.error(request, '更改格式成功！')
            content = {'t_treatment_submit_form': t_treatment_submit_form, 'dic_format': dict(dic_format)}
            return render(request, 'fileTest/upload_t_treatment.html', content)
    else:
        t_treatment_submit_form = tTreatmentSubmitForm()
    content = {'t_treatment_submit_form': t_treatment_submit_form, 'form_title': '信息上传',
               'dic_format': dict(dic_format)}
    # context['page_title'] = '欢迎'
    return render(request, 'fileTest/upload_t_treatment.html', content)


def tIllnessSubmit(request):
    if not request.user.is_authenticated:
        login_form = LoginFrom()

        context = {'login_form': login_form, 'form_title': '登录'}
        messages.error(request, '请先登录！')
        return render(request, 'user/login.html', context)
    dic = table_format.objects.all()[0]
    dic_format = defaultdict(set)
    dic_format['illness_id'] = set(dic.department_id.split(','))
    dic_format['patient_id'] = set(dic.patient_id.split(','))
    dic_format['illness_name'] = set(dic.department_name.split(','))
    dic_format['blood_sugar'] = set(dic.department_address.split(','))
    dic_format['blood_pressure'] = set(dic.department_address.split(','))
    dic_format['blood_fat'] = set(dic.department_address.split(','))
    dic_format['comment'] = set(dic.department_address.split(','))

    dic_format['enabled'] = set(dic.enabled.split(','))
    dic_format['deleted'] = set(dic.deleted.split(','))
    dic_format['created_time'] = set(dic.created_time.split(','))
    dic_format['updated_time'] = set(dic.updated_time.split(','))
    if request.method == 'POST':
        t_illness_submit_form = tIllnessSubmitForm(request.POST)
        if t_illness_submit_form.is_valid():
            illness_id = t_illness_submit_form.cleaned_data['illness_id']
            patient_id = t_illness_submit_form.cleaned_data['patient_id']
            illness_name = t_illness_submit_form.cleaned_data['illness_name']
            blood_sugar = t_illness_submit_form.cleaned_data['blood_sugar']
            blood_pressure = t_illness_submit_form.cleaned_data['blood_pressure']
            blood_fat = t_illness_submit_form.cleaned_data['blood_fat']

            updated_time = t_illness_submit_form.cleaned_data['updated_time']
            comment = t_illness_submit_form.cleaned_data['comment']

            deleted = t_illness_submit_form.cleaned_data['deleted']
            created_time = t_illness_submit_form.cleaned_data['created_time']
            enabled = t_illness_submit_form.cleaned_data['enabled']
            #
            dic.illness_ide += (',' + illness_id) if illness_id else ''
            dic.patient_id += (',' + patient_id) if patient_id else ''
            dic.illness_name += (',' + illness_name) if illness_name else ''
            dic.blood_sugar += (',' + blood_sugar) if blood_sugar else ''
            dic.blood_pressure += (',' + blood_pressure) if blood_pressure else ''
            dic.blood_fat += (',' + blood_fat) if blood_fat else ''
            dic.comment += (',' + comment) if comment else ''

            dic.created_time += (',' + created_time) if created_time else ''
            dic.updated_time += (',' + updated_time) if updated_time else ''
            dic.deleted += (',' + deleted) if deleted else ''
            dic.enabled += (',' + enabled) if enabled else ''

            dic.save()
            # t_result_submit_info = '123'
            messages.error(request, '更改格式成功！')
            content = {'t_illness_submit_form': t_illness_submit_form, 'dic_format': dict(dic_format)}

            return render(request, 'fileTest/upload_t_illness.html', content)
    else:
        t_illness_submit_form = tIllnessSubmitForm()
    content = {'t_illness_submit_form': t_illness_submit_form, 'form_title': '信息上传',
               'dic_format': dict(dic_format)}

    # context['page_title'] = '欢迎'
    return render(request, 'fileTest/upload_t_illness.html', content)


def patientUpdateData(request):
    if not request.user.is_authenticated:
        messages.error(request, '请登陆后再使用该功能！')
        context = {'Search_Comment': Search_Comment()}
        return render(request, 'home.html', context)
    user = request.user
    today = timezone.now()
    queryset = Patient_Information.objects.filter(user=user, time__day=today.day, time__month=today.month,
                                                  time__year=today.year)
    context = {}
    if queryset:
        messages.error(request, '今天已经填过了哦！')
        context = {'Search_Comment': Search_Comment()}
        return render(request, 'home.html', context)
    if request.method == 'POST':
        form = patientUpdateDataForm(request.POST)
        if form.is_valid():
            heart_rate = form.cleaned_data['heart_rate']
            weight = form.cleaned_data['weight']
            step_number = form.cleaned_data['step_number']
            sleep_time = form.cleaned_data['sleep_time']
            patient_update_data = Patient_Information.objects.create(user=user,
                                                                     heart_rate=heart_rate, step_number=step_number,
                                                                     weight=weight, sleep_time=sleep_time)
            patient_update_data.save()
            messages.error(request, '填报成功！')
            context = {'Search_Comment': Search_Comment()}
            return render(request, 'home.html', context)
    else:
        form = patientUpdateDataForm()

    # context['page_title'] = '欢迎'
    context['form'] = form
    context['form_title'] = '信息上传'

    return render(request, 'fileTest/patientUpdateData.html', context)


def changeDataForm(dataTime, k):
    List = dataTime.all()
    m = len(dataTime)
    # patient_update_data = Patient_Information.objects.create(user=user,
    #                                                          heart_rate=heart_rate, step_number=step_number,
    #                                                          weight=weight, sleep_time=sleep_time)
    heart_rate_list = [0 for _ in range(k)]
    step_number_list = [0 for _ in range(k)]
    weight_list = [0.0 for _ in range(k)]
    sleep_time_list = [0.0 for _ in range(k)]
    today = timezone.now()
    index = 0
    for i in range(k):
        dayI = today - timezone.timedelta(i)
        if dataTime.filter(time__year=dayI.year, time__month=dayI.month, time__day=dayI.day):
            heart_rate_list[i] = int(List[index].heart_rate)
            step_number_list[i] = int(List[index].step_number)
            weight_list[i] = float(List[index].weight)
            sleep_time_list[i] = float(List[index].sleep_time)
            index += 1

    return heart_rate_list[::-1], step_number_list[::-1], weight_list[::-1], sleep_time_list[::-1]  # 翻转


def showPatientData(request):
    if not request.user.is_authenticated:
        messages.error(request, '请登陆后再使用该功能！')
        context = {'Search_Comment': Search_Comment()}
        return render(request, 'home.html', context)

    user = request.user
    today = timezone.now()
    time7 = today - timezone.timedelta(days=7)
    time30 = today - timezone.timedelta(days=30)
    time100 = today - timezone.timedelta(days=100)
    # dataTime = Patient_Information.objects.filter(user=user, time__month=1)
    dataTime7 = Patient_Information.objects.filter(user=user, time__gte=time7)
    dataTime30 = Patient_Information.objects.filter(user=user, time__gte=time30)
    dataTime100 = Patient_Information.objects.filter(user=user, time__gte=time100)

    context = {}

    context['dataTime7HeartRate'], context['dataTime7StepNumber'], context['dataTime7Weight'], context[
        'dataTime7SleepTime'] \
        = changeDataForm(dataTime7, 7)
    context['dataTime30HeartRate'], context['dataTime30StepNumber'], context['dataTime30Weight'], context[
        'dataTime30SleepTime'] \
        = changeDataForm(dataTime30, 30)
    context['dataTime100HeartRate'], context['dataTime100StepNumber'], context['dataTime100Weight'], context[
        'dataTime100SleepTime'] \
        = changeDataForm(dataTime100, 100)
    context['dateTime7'] = ["{}-{}-{}".format((today - timezone.timedelta(i)).year,
                                              (today - timezone.timedelta(i)).month,
                                              (today - timezone.timedelta(i)).day) for i in range(6, -1, -1)]
    context['dateTime30'] = ["{}-{}-{}".format((today - timezone.timedelta(i)).year,
                                               (today - timezone.timedelta(i)).month,
                                               (today - timezone.timedelta(i)).day) for i in range(29, -1, -1)]
    context['dateTime100'] = ["{}-{}-{}".format((today - timezone.timedelta(i)).year,
                                                (today - timezone.timedelta(i)).month,
                                                (today - timezone.timedelta(i)).day) for i in range(99, -1, -1)]
    return render(request, 'fileTest/showPatientData.html', context)


def docSearchPatientDaily(request):
    if not request.user.is_authenticated:
        messages.error(request, '请登陆后再使用该功能！')
        context = {'Search_Comment': Search_Comment()}
        return render(request, 'home.html', context)
    user = request.user
    if not user.profile.is_doc:
        messages.error(request, '无权限使用该功能')
        context = {'Search_Comment': Search_Comment()}
        return render(request, 'home.html', context)

    today = timezone.now()
    time7 = today - timezone.timedelta(days=7)
    time30 = today - timezone.timedelta(days=30)
    time100 = today - timezone.timedelta(days=100)
    #

    context = {}
    if request.method == 'POST':
        form = searchPatientDailyForm(request.POST)
        if form.is_valid():
            patientName = form.cleaned_data['text']
            context['patientName'] = patientName
            profile = Profile.objects.filter(real_name__contains=patientName, is_patient=True)
            if len(profile) == 0:
                # patientUser = profile[0].user
                # context['patientUser'] = patientUser
                formE = searchPatientDailyForm()
                context['Search_Comment'] = formE
                context['form_title'] = '随访数据'
                context['message'] = '没有该用户'

                return render(request, 'fileTest/docSearchPatientDaily.html', context)
            patientUser = profile[0].user
            patientList = []
            patientListBool = False
            if len(profile) > 1:
                patientListBool = True
                for i in range(len(profile)):
                    patientList.append(profile[i].real_name)
            context['patientList'] = patientList
            context['patientListBool'] = patientListBool
            # if len(profile) > 1:
            context['patientUser'] = patientUser.profile.real_name

            dataTime7 = Patient_Information.objects.filter(user=patientUser, time__gte=time7)
            dataTime30 = Patient_Information.objects.filter(user=patientUser, time__gte=time30)
            dataTime100 = Patient_Information.objects.filter(user=patientUser, time__gte=time100)

            # context['patientUser'] = patientUser

            context['dataTime7HeartRate'], context['dataTime7StepNumber'], context['dataTime7Weight'], context[
                'dataTime7SleepTime'] \
                = changeDataForm(dataTime7, 7)
            context['dataTime30HeartRate'], context['dataTime30StepNumber'], context['dataTime30Weight'], context[
                'dataTime30SleepTime'] \
                = changeDataForm(dataTime30, 30)
            context['dataTime100HeartRate'], context['dataTime100StepNumber'], context['dataTime100Weight'], context[
                'dataTime100SleepTime'] \
                = changeDataForm(dataTime100, 100)
            context['dateTime7'] = ["{}-{}-{}".format((today - timezone.timedelta(i)).year,
                                                      (today - timezone.timedelta(i)).month,
                                                      (today - timezone.timedelta(i)).day) for i in range(6, -1, -1)]
            context['dateTime30'] = ["{}-{}-{}".format((today - timezone.timedelta(i)).year,
                                                       (today - timezone.timedelta(i)).month,
                                                       (today - timezone.timedelta(i)).day) for i in range(29, -1, -1)]
            context['dateTime100'] = ["{}-{}-{}".format((today - timezone.timedelta(i)).year,
                                                        (today - timezone.timedelta(i)).month,
                                                        (today - timezone.timedelta(i)).day) for i in range(99, -1, -1)]

            formE = searchPatientDailyForm()
            context['Search_Comment'] = formE
            context['form_title'] = '随访数据'

            return render(request, 'fileTest/docSearchPatientDaily.html', context)

    else:
        form = searchPatientDailyForm()

    # context['page_title'] = '欢迎'
    context['Search_Comment'] = form
    context['form_title'] = '随访数据'

    return render(request, 'fileTest/docSearchPatientDaily.html', context)
