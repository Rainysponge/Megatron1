import os
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import time
import datetime
from dateutil.relativedelta import relativedelta

from django import forms
from django.shortcuts import render, redirect
from django.db import connection
from comment.forms import Search_Comment
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

def draw_picture(request, age_data1, age_data2, age_data3, age_data4, date_data1, date_data2, date_data3, date_data4, date_data5, date_data6, sex_data1, sex_data2):
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


def draw_picture_trend(request, age_data1, age_data2, age_data3, age_data4, date_data1, date_data2, date_data3, date_data4, date_data5, date_data6, sex_data1, sex_data2):
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


def draw_picture_sex(request, age_data1, age_data2, age_data3, age_data4, date_data1, date_data2, date_data3, date_data4, date_data5, date_data6, sex_data1, sex_data2):
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
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='Mouhao0715',
        db='medicalproject',
    )
    cur = conn.cursor()

    Search_Comment_form = Search_Comment(request.POST)
    # path = "1"
    if Search_Comment_form.is_valid():
        Search_Comment.text = Search_Comment_form.cleaned_data['text']
        question = str(Search_Comment.text)
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
        sex_data = [0]*2
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

        deleted_name = ["enabled", "deleted", "created_time", "updated_time"]  # 不要的字段
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

        gain_data = cur.fetchmany(result_num)
        result = []

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

            result.append(temp)

    context = {}
    context["location"] = location
    context["result_name"] = SqlDomainName
    context["result"] = result
    context["sql"] = sql[-2]
    context["result_num"] = result_num
    context['Search_Comment'] = Search_Comment()

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
    return render(request, 'home_result.html', context)

