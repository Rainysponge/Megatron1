import os
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

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
    #path = "1"
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

        SqlDomain = cur.description  # 获取属性名,返回的元组只有[0]为需要的
        DomainNum = len(SqlDomain)
        SqlDomainName = []
        # SqlDomainName = [None] * DomainNum  # 前端判断为None就不输出
        deleted_name = ["enabled", "deleted", "created_time", "updated_time"]   # 不要的字段
        existed_name = []   # 去重
        location = []   # 记录需要的列
        for i in range(DomainNum):
            if SqlDomain[i][0] not in deleted_name and SqlDomain[i][0] not in existed_name:
                SqlDomainName.append(SqlDomain[i][0])
                existed_name.append(SqlDomain[i][0])
                location.append(i)

        gain_data = cur.fetchmany(result_num)
        result = []

        for i in range(result_num):
            temp = []
            for j in range(len(gain_data[0])):
                if j in location:
                    temp.append(gain_data[i][j])
            result.append(temp)

    context = {}
    context["location"] = location
    context["result_name"] = SqlDomainName
    context["result"] = result
    context["sql"] = sql[-2]
    context["result_num"] = result_num
    context['Search_Comment'] = Search_Comment()
    return render(request, 'home_result.html', context)

