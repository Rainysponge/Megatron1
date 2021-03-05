import os
import pandas as pd
from django.shortcuts import render
from django.contrib import messages
from Megatron import settings
from .models import firstFileContent


# from Megatron.settings import BASE_DIR


# Create your views here.


def uploadFileTest(request):
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
                    for i in range(len(df)):
                        tmp = firstFileContent.objects.create(firstField=df['firstField'][i],
                                                              secondField=df['secondField'][i])
                        # tmp.save()

                    messages.success(request, '数据导入成功')




                except Exception as e:
                    messages.error(request, '数据读入失败:'+str(e))
            else:
                messages.error(request, '文件类型错误')

        else:
            messages.error(request, '上传文件不能为空')

    return render(request, "fileTest/uploadFIleTest.html", context)
