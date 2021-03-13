import os
import re
import jieba
import pymysql

pymysql.install_as_MySQLdb()
import MySQLdb
import time
import datetime
from dateutil.relativedelta import relativedelta
from django.contrib import messages

from django import forms
from django.shortcuts import render, redirect
from django.db import connection
from comment.forms import Search_Comment
from dateutil.relativedelta import relativedelta
from comment.models import thesis
from t.models import treatment, result, department

from user.models import Doctor
from .forms import Search_Comment
from .models import questionsSearched

pymysql.install_as_MySQLdb()


# Create your views here.


# def find_result(request):
#     # conn = MySQLdb.connect(
#     #     host='localhost',
#     #     port=3306,
#     #     user='root',
#     #     passwd='Mouhao0715',
#     #     db='medicalproject',
#     # )
#     # cur = conn.cursor()
#
#     cur = connection.cursor()
#     Search_Comment_form = Search_Comment(request.POST)
#     #path = "1"
#     if Search_Comment_form.is_valid():
#         Search_Comment.text = Search_Comment_form.cleaned_data['text']
#         question = str(Search_Comment.text)
#         # os.chdir("E:/design/spf-jar-pack")
#         # os.chdir("F:/DACHUANGwenjian2/javaspf")
#         path = os.getcwd()
#         if path.find("javaspf") < 0:
#             path += "\\comment\\javaspf"
#         os.chdir(path)
#
#         cmd = "java -jar spf.jar " + question
#         # print(path)
#
#         p = os.popen(cmd)
#         p1 = str(p.read())  # cmd的返回结果
#
#         sql = p1.split('\n')
#         # print(sql)
#         #print(sql[-2])
#
#         result_num = cur.execute(sql[-2])
#         #result_num = cur.execute("select * from t_patient;")
#         #print(result_num)
#
#         gain_data = cur.fetchmany(result_num)
#         result = []
#
#         for member in gain_data:
#             result.append(member)
#
#     context = {}
#     context["path"] = path
#     context["result"] = result
#     context["sql"] = sql[-2]
#     context["result_num"] = result_num
#     context['Search_Comment'] = Search_Comment()
#     return render(request, 'home_result.html', context)

def draw_picture(request, age_data1, age_data2, age_data3, age_data4, date_data1, date_data2, date_data3, date_data4,
                 date_data5, date_data6, sex_data1, sex_data2):
    # result = result.split(';')
    age_data = []
    age_data.append(age_data1)
    age_data.append(age_data2)
    age_data.append(age_data3)
    age_data.append(age_data4)

    # context["result_name"] = result_name
    # context["result"] = result

    #  localtime = time.strftime("%Y-%m", time.localtime())

    context = {}
    context["age_data"] = age_data

    context['age_data1'] = age_data1
    context['age_data2'] = age_data2
    context['age_data3'] = age_data3
    context['age_data4'] = age_data4
    context['date_data1'] = date_data1
    context['date_data2'] = date_data2
    context['date_data3'] = date_data3
    context['date_data4'] = date_data4
    context['date_data5'] = date_data5
    context['date_data6'] = date_data6
    context['sex_data1'] = sex_data1
    context['sex_data2'] = sex_data2
    return render(request, 'draw_picture.html', context)


def draw_picture_trend(request, age_data1, age_data2, age_data3, age_data4, date_data1, date_data2, date_data3,
                       date_data4, date_data5, date_data6, sex_data1, sex_data2):
    now = datetime.datetime.now().replace(day=1)
    now_1 = (now - relativedelta(months=+1)).strftime('%Y-%m')
    now_2 = (now - relativedelta(months=+2)).strftime('%Y-%m')
    now_3 = (now - relativedelta(months=+3)).strftime('%Y-%m')
    now_4 = (now - relativedelta(months=+4)).strftime('%Y-%m')
    now_5 = (now - relativedelta(months=+5)).strftime('%Y-%m')
    now = now.strftime('%Y-%m')

    time = []
    time.append(now_5)
    time.append(now_4)
    time.append(now_3)
    time.append(now_2)
    time.append(now_1)
    time.append(now)

    time_data = []
    time_data.append(date_data1)
    time_data.append(date_data2)
    time_data.append(date_data3)
    time_data.append(date_data4)
    time_data.append(date_data5)
    time_data.append(date_data6)

    context = {}

    context["time0"] = time[0]
    context["time1"] = time[1]
    context["time2"] = time[2]
    context["time3"] = time[3]
    context["time4"] = time[4]
    context["time5"] = time[5]
    context["time_data"] = time_data
    # 图片间参数传递
    context['age_data1'] = age_data1
    context['age_data2'] = age_data2
    context['age_data3'] = age_data3
    context['age_data4'] = age_data4
    context['date_data1'] = date_data1
    context['date_data2'] = date_data2
    context['date_data3'] = date_data3
    context['date_data4'] = date_data4
    context['date_data5'] = date_data5
    context['date_data6'] = date_data6
    context['sex_data1'] = sex_data1
    context['sex_data2'] = sex_data2
    return render(request, 'draw_picture_trend.html', context)


def draw_picture_sex(request, age_data1, age_data2, age_data3, age_data4, date_data1, date_data2, date_data3,
                     date_data4, date_data5, date_data6, sex_data1, sex_data2):
    sex_data = []
    sex_data.append(sex_data1)
    sex_data.append(sex_data2)

    context = {}

    context["sex_data"] = sex_data
    # 图片间参数传递
    context['age_data1'] = age_data1
    context['age_data2'] = age_data2
    context['age_data3'] = age_data3
    context['age_data4'] = age_data4
    context['date_data1'] = date_data1
    context['date_data2'] = date_data2
    context['date_data3'] = date_data3
    context['date_data4'] = date_data4
    context['date_data5'] = date_data5
    context['date_data6'] = date_data6
    context['sex_data1'] = sex_data1
    context['sex_data2'] = sex_data2
    return render(request, 'draw_picture_sex.html', context)


def find_result(request):

    if not request.user.is_authenticated:
        messages.error(request, '请登陆后再使用该功能！')
        context = {'Search_Comment': Search_Comment()}
        return render(request, 'home.html', context)
    # else:
    user = request.user
    doctor = Doctor.objects.get(user=user)
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='Mouhao0715',
        db='medicalproject1',
    )
    cur = conn.cursor()

    Search_Comment_form = Search_Comment(request.POST)
    # # path = "1"
    if Search_Comment_form.is_valid():
        Search_Comment.text = Search_Comment_form.cleaned_data['text']
        # context['question'] = question
        question = str(Search_Comment.text)

        # context['question'] = question
        man_flag = 0
        woman_flag = 0

        not_flag = 0
        if question.find("做") >= 0:
            question = question.replace("做", "做了")
        if question.find("没有") >= 0:
            question = question.replace("没有", "的")
            not_flag = 1

        matchObj = re.search(r'^(.*)(患者|病人)(.*)$', question)  # 匹配性别
        if matchObj:
            patient_dis = matchObj.group(1)
            female_match = re.search(r'^(.*)(女性|女)(.*)$', patient_dis)
            male_match = re.search(r'^(.*)(男性|男)(.*)$', patient_dis)
            if female_match:
                woman_flag = 1
                question = female_match.group(1) + female_match.group(3) + matchObj.group(2) + matchObj.group(3)
            elif male_match:
                man_flag = 1
                question = male_match.group(1) + male_match.group(3) + matchObj.group(2) + matchObj.group(3)

        year_data = "0"
        matchObj2 = re.search(r'^(.*)(\d\d\d\d)(年间|年)(.*)$', question)  # 匹配年份
        if matchObj2:
            year_data = matchObj2.group(2)
            question = matchObj2.group(1) + matchObj2.group(4)

        # disease_name = "0"
        # disease_obj = re.search(r'^(.*)(患者|病人)(.*)$', question)   # 匹配....患者
        # if disease_obj:
        #     if disease_obj.group(1).find('得') < 0:
        #         temp =

        # os.chdir("E:/design/spf-jar-pack")
        # os.chdir("F:/DACHUANGwenjian2/javaspf")
        path = os.getcwd()
        if path.find("javaspf") < 0:
            path += "\\comment\\javaspf"
        os.chdir(path)

        cmd = "java -jar spf.jar " + question

        p = os.popen(cmd)
        p1 = str(p.read())  # cmd的返回结果

        sql = p1.split('\n')
        ignoreList = {'低', '高', '男', '女', '好', '年'}
        if question == "" or sql[-2].find("SELECT") < 0:  # 要改
            seq_list = list(jieba.cut(question, cut_all=False))  # 分词列表
            question_name_list = set()  # 集合去重
            for seq in seq_list:
                if seq in ignoreList:
                    continue
                if questionsSearched.objects.filter(questionsName__contains=seq):

                    question_list = questionsSearched.objects.filter(questionsName__contains=seq)

                    # for i in range(len(question_list)):
                    #     question_list[i].numSearched += 1
                    #
                    #     question_list[i].save()
                    for j in range(len(question_list)):
                        question_name_list.add(question_list[j].questionsName)
            context = {}
            context['age_data1'] = 0
            context['age_data2'] = 0
            context['age_data3'] = 0
            context['age_data4'] = 0

            context['date_data1'] = 0
            context['date_data2'] = 0
            context['date_data3'] = 0
            context['date_data4'] = 0
            context['date_data5'] = 0
            context['date_data6'] = 0

            context['sex_data1'] = 0
            context['sex_data2'] = 0
            context['disease_name'] = "0"
            context['Search_Comment'] = Search_Comment()
            context['recommend_flag'] = 1
            context['question_name_list'] = question_name_list
            context['question'] = Search_Comment.text
            return render(request, 'home_result.html', context)

            # context = {}
            # # question = questionsSearched.objects.create(questionsName=question, department=doctor.department)
            # # # 大致方法就是这个样子样子了， 就是要在question = questionsSearched.objects.create这个语句之前完成sql语句的生成
            # # # 然后再save，避免出现无法查询的问题！
            # # # sql在这后面
            # # question.save()
            # messages.error(request, question)
            # context['age_data1'] = 0
            # context['age_data2'] = 0
            # context['age_data3'] = 0
            # context['age_data4'] = 0
            #
            # context['date_data1'] = 0
            # context['date_data2'] = 0
            # context['date_data3'] = 0
            # context['date_data4'] = 0
            # context['date_data5'] = 0
            # context['date_data6'] = 0
            #
            # context['sex_data1'] = 0
            # context['sex_data2'] = 0
            # context['Search_Comment'] = Search_Comment()

            # return render(request, 'home_result.html', context)
        else:  # 加个好转率
            if woman_flag == 1:
                sql[-2] = sql[-2].replace(";", " and t_patient.gender = '女';")
            elif man_flag == 1:
                sql[-2] = sql[-2].replace(";", " and t_patient.gender = '男';")

            if year_data != "0":
                year_str = " and t_patient.created_time like '" + year_data + "%';"
                sql[-2] = sql[-2].replace(";", year_str)

            #  放最后避免treatment_name无法更新
            if not_flag == 1:
                sql[-2] = sql[-2].replace("t_treatment.treatment_name like", "t_treatment.treatment_name not like")

            disease_flag = -1
            disease_name = "0"
            treatment_flag = -1
            treatment_name = "0"
            disease_obj = re.search(r'^(.*)t_illness.illness_name like \'(.*?)\'(.*)$', sql[-2])
            if disease_obj:
                disease_name = disease_obj.group(2)
            treatment_obj = re.search(r'^(.*)t_treatment.treatment_name like \'(.*?)\'(.*)$', sql[-2])
            if treatment_obj:
                treatment_name = treatment_obj.group(2)

            result_num = cur.execute(sql[-2])

            SqlDomain = cur.description  # 获取属性名,返回的元组只有[0]为需要的 （[shuxingming],[])
            DomainNum = len(SqlDomain)
            SqlDomainName = []
            # SqlDomainName = [None] * DomainNum  # 前端判断为None就不输出
            age_flag = 0  # 记录年龄所在列
            age_data = [0] * 4

            date_flag = 0  # 记录update_time的列数
            date_data = [0] * 6

            sex_flag = 0
            sex_data = [0] * 2
            #  datetime.date.today() - relativedelta(months=+1)
            now = datetime.datetime.now().replace(day=1)
            # delta = datetime.timedelta(months=1)
            # now_1 = (now - delta).strftime('%Y-%m')
            # now_2 = (now - delta*2).strftime('%Y-%m')
            # now_3 = (now - delta*3).strftime('%Y-%m')
            # now_4 = (now - delta*4).strftime('%Y-%m')
            # now_5 = (now - delta*5).strftime('%Y-%m')
            # now_6 = now - delta*6.strftime('%Y-%m')
            now_1 = (now - relativedelta(months=+1))
            now_2 = (now - relativedelta(months=+2))
            now_3 = (now - relativedelta(months=+3))
            now_4 = (now - relativedelta(months=+4))
            now_5 = (now - relativedelta(months=+5))

            # dic = {'patient_id': '患者编号'}
            comment_flag = 0
            better_num = 0
            sum_num = 0
            better_rate = 0

            patient_id_flag = -1
            patient_id_data = []

            deleted_name = ["enabled", "deleted", "created_time", "updated_time"]  # 不要的字段
            if sql[-2].find("result") > 0:
                deleted_name.append("comment")
            existed_name = []  # 去重
            location = []  # 记录需要的列
            for i in range(DomainNum):
                if SqlDomain[i][0] == "updated_time":
                    date_flag = i
                elif SqlDomain[i][0] not in deleted_name and SqlDomain[i][0] not in existed_name:
                    SqlDomainName.append(SqlDomain[i][0])
                    # SqlDomainName.append(dic[SqlDomain[i][0]])
                    existed_name.append(SqlDomain[i][0])
                    location.append(i)
                    if SqlDomain[i][0] == "age":
                        age_flag = i
                    if SqlDomain[i][0] == "gender":
                        sex_flag = i
                    if SqlDomain[i][0] == "comment":
                        comment_flag = i
                    if SqlDomain[i][0] == "illness_name":
                        disease_flag = i
                    if SqlDomain[i][0] == "treatment_name":
                        treatment_flag = i
                    if SqlDomain[i][0] == "patient_id":
                        patient_id_flag = i

            gain_data = cur.fetchmany(result_num)
            result1 = []

            for i in range(result_num):
                temp = []
                for j in range(len(gain_data[0])):
                    if j in location:  # 获取需要数据
                        temp.append(gain_data[i][j])
                    if j == age_flag:  # 判断年龄分布
                        if gain_data[i][j] < 17:
                            age_data[0] += 1
                        elif 17 < gain_data[i][j] < 40:
                            age_data[1] += 1
                        elif 40 < gain_data[i][j] < 65:
                            age_data[2] += 1
                        elif gain_data[i][j] > 65:
                            age_data[3] += 1
                    if j == date_flag:  # 病例趋势
                        if gain_data[i][j].__ge__(now_5) and gain_data[i][j].__lt__(now_4):
                            date_data[0] += 1
                        elif gain_data[i][j].__ge__(now_4) and gain_data[i][j].__lt__(now_3):
                            date_data[1] += 1
                        elif gain_data[i][j].__ge__(now_3) and gain_data[i][j].__lt__(now_2):
                            date_data[2] += 1
                        elif gain_data[i][j].__ge__(now_2) and gain_data[i][j].__lt__(now_1):
                            date_data[3] += 1
                        elif gain_data[i][j].__ge__(now_1) and gain_data[i][j].__lt__(now):
                            date_data[4] += 1
                        elif gain_data[i][j].__ge__(now):  # 本月数据
                            date_data[5] += 1
                    if j == sex_flag:
                        if gain_data[i][j] == '男':
                            sex_data[0] += 1
                        if gain_data[i][j] == '女':
                            sex_data[1] += 1
                    # if j == disease_flag:
                    #     disease_name = gain_data[i][j]
                    # if j == treatment_flag:
                    #     treatment_name = gain_data[i][j]
                    # if j == comment_flag:  # 统计好转率
                    #     sum_num += 1
                    #     if gain_data[i][j] == '好转':
                    #         better_num += 1
                    if j == patient_id_flag:  # 统计好转率
                        patient_id_data.append(gain_data[i][j])

                result1.append(temp)

            disease_thesis = thesis.objects.filter(key_word=disease_name)
            treatment_thesis = thesis.objects.filter(key_word=treatment_name)

            # if sum_num > 0:
            #     better_rate = better_num / sum_num * 100
            # else:
            #     better_rate = 0

            # 获取每个症状的治疗手法
            all_treatment_name = []
            all_treatment_data = []
            all_better_data = []
            treatment_sum = 0

            treatment_warning_flag = 1

            # 权限判断
            for i in patient_id_data:
                department_result = department.objects.get(patient_id=i)
                if department_result.department_name != doctor.department.Department_name:
                    messages.error(request, '没有查询权限')
                    context = {'Search_Comment': Search_Comment()}
                    return render(request, 'home.html', context)

            for i in patient_id_data:
                Treatment = treatment.objects.get(patient_id=i)
                tre_result = result.objects.get(patient_id=i)
                add_flag = 1
                for j in range(len(all_treatment_name)):
                    if all_treatment_name[j] == Treatment.treatment_name:
                        add_flag = 0
                if add_flag > 0:
                    all_treatment_name.append(Treatment.treatment_name)
                    all_treatment_data.append(int(1))
                    if tre_result.result_comment == "好转":
                        all_better_data.append(int(1))
                    else:
                        all_better_data.append(int(0))
                else:
                    all_treatment_data[j] = int(all_treatment_data[j]) + 1
                    if tre_result.result_comment == "好转":
                        all_better_data[j] = int(all_better_data[j]) + 1
                treatment_sum += 1

            for j in range(len(all_treatment_name)):
                if all_treatment_name[j] == "纤维结合蛋白":
                    treatment_warning_flag = 0

            better_rate = []
            for i in range(len(all_treatment_data)):
                temp = all_better_data[i]*100 / all_treatment_data[i]
                temp = round(temp, 2)
                better_rate.append(temp)
                all_treatment_data[i] = all_treatment_data[i] * 100 / treatment_sum
                all_treatment_data[i] = round(all_treatment_data[i], 2)
                # all_treatment_data[i] *= 100
                # all_treatment_data[i] = int(all_treatment_data[i])
                # all_treatment_data[i] /= 100.0

            context = {}
            context["location"] = location
            context["result_name"] = SqlDomainName
            context["result"] = result1
            context["sql"] = sql[-2]
            context["result_num"] = result_num
            context['Search_Comment'] = Search_Comment()
            context['better_rate'] = better_rate

            context['age_data1'] = age_data[0]
            context['age_data2'] = age_data[1]
            context['age_data3'] = age_data[2]
            context['age_data4'] = age_data[3]

            context['date_data1'] = date_data[0]
            context['date_data2'] = date_data[1]
            context['date_data3'] = date_data[2]
            context['date_data4'] = date_data[3]
            context['date_data5'] = date_data[4]
            context['date_data6'] = date_data[5]

            context['sex_data1'] = sex_data[0]
            context['sex_data2'] = sex_data[1]

            context['disease_thesis'] = disease_thesis
            context['treatment_thesis'] = treatment_thesis
            context['question'] = Search_Comment.text
            context['disease_name'] = disease_name  # 如果 = "0" 不需要输出治疗手法与占比
            context['treatment_warning_flag'] = treatment_warning_flag
            context['all_treatment_name'] = all_treatment_name
            context['all_treatment_data'] = all_treatment_data
            context['patient_id_data'] = patient_id_data
            # context['question'] = Search_Comment.text  # 这个地方把注释去了就可以前端显示问题了（理论上
            return render(request, 'home_result.html', context)
