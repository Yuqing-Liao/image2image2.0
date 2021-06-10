from datetime import date
import json
from django.db.models import base
from django.shortcuts import render
import os

import subprocess
from i2iProcessApp import models
from Process_web import settings
from django.utils import timezone
from django.http import JsonResponse, request, response

import logging

# Get an instance of a logger
logging.basicConfig(
    format='%(asctime)s - %(pathname)s[%(lineno)d] - %(levelname)s: %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

import time 

def uploadToChange(request):
    if request.method == "POST":
        data_root = []
        #if 'pic1' in request.POST:  #这里错误 pic1非submit
        img1 = request.FILES.getlist("pic1")  #这里改成可以一次上传多个文件
        if img1 != None:
            for f in img1:
                suffix = f.name.rsplit(".")[1]  #获取文件后缀名
                f.name = str(round(time.time() * 1000)) +'.' + suffix
                dir = os.path.join(settings.UPLOAD_ROOT,f.name)
                data_root.append(dir)
                destination = open(dir,'wb+')
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()
                '''
                models.Img.objects.create(
                    name = f.name,
                    uploader = 'test',
                    address = dir,
                    add_time = timezone.now()
                )
                '''
        img2 = request.FILES.getlist("pic2")  #这里改成可以一次上传多个文件
        if img2 != None:
            for f in img2:
                suffix = f.name.rsplit(".")[1]  #获取文件后缀名
                f.name = str(round(time.time() * 1000)) +'.' + suffix
                dir = os.path.join(settings.UPLOAD_ROOT,f.name)
                data_root.append(dir)
                destination = open(dir,'wb+')
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()
                ''';
                models.Img.objects.create(
                    name = f.name,
                    uploader = 'test',
                    address = dir,
                    add_time = timezone.now()
                )
                '''
        if 'submit' in request.POST:
            #test
            back = invoke(request)
            img_root = []
            #back = ["05.jpg","Class1.png"] #程序返回图片名
            for i in back: 
                img_root.append("/result/" + i )
            return render(request,'result.html',{'urls':json.dumps(img_root)})
            #return JsonResponse({"status":False,"error":  img_root})
    else:
        return JsonResponse({"status":False,"error":"请求错误"})
#etc
#看是否要支持多文件上传，如需要可进行循环调用？或修改调用程序
#for i in data_root():
#调用图片处理程序 data_root tasks save_root
#暂时不加入save_root
'''
def invoke(request):
    mode = request.POST.get('tmethod')
    task = '8kjm '
    if(mode == 1): #两张图片风格转换 此处应作出限制只允许上传一张图片
        task = 'AdaIN'
    elif(mode == 2): #风格转换
        tstyle = request.POST.get('tstyle')
        if(tstyle == 'monet'):
            task = 'photo2monet'
        elif(tstyle == 'cezanne'):
            task = 'photo2cezanne'
        elif(tstyle == 'ukiyoe'):
            task = 'photo2ukiyoe'
        elif(tstyle == "vangogh"):
            task = 'photo2vangogh'
        #else:
            #return JsonResponse({"status":False,"error":"暂不支持的转换"})       
    elif(mode == 3): #时间转换
        time = request.POST.get('ttime')
        if(time == 'summer'):
            task = "winter2summer"
        elif(time == 'winter'):
            task = 'summer2winter'
        #else:
            #return JsonResponse({"status":False,"error":"暂不支持的转换"})       
    elif(mode == 4): #简绘
         此部分需前端更新提供额外输入
        time = request.POST.get('ttime')
        if(time == 'summer'):
            task = "winter2summer"
            excute(data_root,task)
        elif(time == 'winter'):
            task = 'summer2winter'
        else:
            return JsonResponse({"status":False,"error":"暂不支持的转换"})
              
    #else:
        #return JsonResponse({"status":False,"error":"错误的模式"})
    #在其他地方调用exe出错了，可能是打包问题？此处为直接调用python文件
    #invoke_root 为所调用文件地址 此处为test.py 
    invoke_root = os.path.join(settings.BASE_DIR,'Process_web')
    #直接获取输出，尝试了下好像无法获取函数返回值，示例见test.py
    back = subprocess.getoutput('cd '+invoke_root+" & python test.py %s" % (task))
    #request.session['save_root'] = save_root
    #request.session.set_expiry(60)
    return back
'''
def invoke(request):
    mode = request.POST.get('tmethod')
    rePath = []
    task = ''

    if(mode == '1'): #两张图片风格转换 此处应作出限制只允许上传一张图片
        #task = 'AdaIN'
        rePath = ['AdaIN/1_fake.png']
    elif(mode == '2'): #风格转换
        tstyle = request.POST.get('tstyle')
        if(tstyle == 'monet'):
            rePath = ['style_monet/1_fake.png','style_monet/2_fake.png']
        elif(tstyle == 'cezanne'):
            rePath = ['style_cezanne/1_fake.png','style_cezanne/2_fake.png']
        elif(tstyle == 'ukiyoe'):
            rePath = ['style_ukiyoe/1_fake.png','style_ukiyoe/2_fake.png']
        elif(tstyle == "vangogh"):
            rePath = ['style_vangogh/1_fake.png','style_vangogh/2_fake.png']
        #else:
            #return JsonResponse({"status":False,"error":"暂不支持的转换"})       
    elif(mode == '3'): #时间转换
        time = request.POST.get('ttime')
        if(time == 'summer'):
            rePath = ['summer2winter/1_fake.png']
        elif(time == 'winter'):
            rePath = ['winter2summer/1_fake.png']
        elif(time == 'night'):
            rePath = ['day2night/1_fake.png']
        #else:
            #return JsonResponse({"status":False,"error":"暂不支持的转换"})       
    elif(mode == '4'): #简绘
        tmap = request.POST.get('tmap')
        if(tmap == '0'):
            rePath = ['map2sat/1_fake.png']
        elif(tmap == '1'):
            rePath = ['sat2map/1_fake.png']
        #else:
            #return JsonResponse({"status":False,"error":"暂不支持的转换"})
    #else:
        #return JsonResponse({"status":False,"error":"暂不支持的转换"})
    return rePath





from django.http import StreamingHttpResponse
def download_file(request):
    """
    sql 文件下载
    :param request:
    :return:
    """
    #file_path = list(file_path)
    '''
    download_name = file_path
    download_name = download_name.strip('?')
    the_file_name = str(download_name).split("/")[-1]  # 显示在弹出对话框中的默认的下载文件名
    filename = settings.MEDIA_ROOT+'/{}'.format(the_file_name)  # 要下载的文件路径
    response = StreamingHttpResponse(readFile(filename))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response
    '''
    
    download_id = request.POST.getlist("checkbox")
    
    for i in download_id:
        print(i)
        download_name = i
        download_name = download_name.strip('?')
        the_file_name = str(download_name).split("/")[-1]  # 显示在弹出对话框中的默认的下载文件名
        #filename = os.path.join(settings.MEDIA_ROOT,download_name)
        name = str(download_name).split("/",2)[2]
        filename = settings.MEDIA_ROOT + '/'+name  # 要下载的文件路径
        response = StreamingHttpResponse(readFile(filename))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)    
    
    return response

    

def readFile(filename, chunk_size=512):
    """
    缓冲流下载文件方法
    :param filename:
    :param chunk_size:
    :return:
    """
    with open(filename, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break

def test(request):
    return render(request,'testfordownload.html',)
def page(request):
    return render(request,'upload.html')

def index(request):
    return render(request,'index.html')
def result(request):
    return render(request,'result.html')
def cTime(request):
    return render(request,'cTime.html')
def cSimple(request):
    return render(request,'cSimple.html')
def cByself(request):
    return render(request,'cByself.html')
def cBysystem(request):
    return render(request,'cBysystem.html')
def wait(request):
    return render(request,'wait.html')
def re(request):
    return render(request,'cBysystemre.html')

