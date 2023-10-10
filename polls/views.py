# coding=utf-8
import os
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
from polls.models import news as ns
from polls.models import contact_us as cs
from os import listdir
import MySQLdb as ps
import datetime,time
# import urllib.parse#python3用
import json
import re
from pprint import pprint
import glob
import traceback
# Create your views here.


def about(request):
	response = render_to_response('about.html',locals())
	response['Strict-Transport-Security'] = 'max-age=2592000'
	response['X-Frame-Options'] = 'SAMEORIGIN'
	response['Referrer-Policy'] = 'no-referrer'
	response['X-XSS-Protection'] = '1; mode=block'
	response['X-Content-Type-Options'] = 'nosniff'
	response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
	return response

def ai_clerk(request):
	response = render_to_response('ai_clerk.html',locals())
	response['Strict-Transport-Security'] = 'max-age=2592000'
	response['X-Frame-Options'] = 'SAMEORIGIN'
	response['Referrer-Policy'] = 'no-referrer'
	response['X-XSS-Protection'] = '1; mode=block'
	response['X-Content-Type-Options'] = 'nosniff'
	response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
	return response

def content(request):
	response = render_to_response('content.html',locals())
	response['Strict-Transport-Security'] = 'max-age=2592000'
	response['X-Frame-Options'] = 'SAMEORIGIN'
	response['Referrer-Policy'] = 'no-referrer'
	response['X-XSS-Protection'] = '1; mode=block'
	response['X-Content-Type-Options'] = 'nosniff'
	response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
	return response

def hornor(request):
	response = render_to_response('hornor.html',locals())
	response['Strict-Transport-Security'] = 'max-age=2592000'
	response['X-Frame-Options'] = 'SAMEORIGIN'
	response['Referrer-Policy'] = 'no-referrer'
	response['X-XSS-Protection'] = '1; mode=block'
	response['X-Content-Type-Options'] = 'nosniff'
	response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
	return response

def index(request):
	response = render_to_response('index.html',locals())
	response['Strict-Transport-Security'] = 'max-age=2592000'
	response['X-Frame-Options'] = 'SAMEORIGIN'
	response['Referrer-Policy'] = 'no-referrer'
	response['X-XSS-Protection'] = '1; mode=block'
	response['X-Content-Type-Options'] = 'nosniff'
	response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
	return response

def join_us(request):
	response = render_to_response('join-us.html',locals())
	response['Strict-Transport-Security'] = 'max-age=2592000'
	response['X-Frame-Options'] = 'SAMEORIGIN'
	response['Referrer-Policy'] = 'no-referrer'
	response['X-XSS-Protection'] = '1; mode=block'
	response['X-Content-Type-Options'] = 'nosniff'
	response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
	return response

def news(request):
	response = render_to_response('news.html',locals())
	response['Strict-Transport-Security'] = 'max-age=2592000'
	response['X-Frame-Options'] = 'SAMEORIGIN'
	response['Referrer-Policy'] = 'no-referrer'
	response['X-XSS-Protection'] = '1; mode=block'
	response['X-Content-Type-Options'] = 'nosniff'
	response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
	return response

def partner(request):
	response = render_to_response('partner.html',locals())
	response['Strict-Transport-Security'] = 'max-age=2592000'
	response['X-Frame-Options'] = 'SAMEORIGIN'
	response['Referrer-Policy'] = 'no-referrer'
	response['X-XSS-Protection'] = '1; mode=block'
	response['X-Content-Type-Options'] = 'nosniff'
	response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
	return response

def product(request):
	response = render_to_response('product.html',locals())
	response['Strict-Transport-Security'] = 'max-age=2592000'
	response['X-Frame-Options'] = 'SAMEORIGIN'
	response['Referrer-Policy'] = 'no-referrer'
	response['X-XSS-Protection'] = '1; mode=block'
	response['X-Content-Type-Options'] = 'nosniff'
	response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
	return response

def report(request):
	response = render_to_response('report.html',locals())
	response['Strict-Transport-Security'] = 'max-age=2592000'
	response['X-Frame-Options'] = 'SAMEORIGIN'
	response['Referrer-Policy'] = 'no-referrer'
	response['X-XSS-Protection'] = '1; mode=block'
	response['X-Content-Type-Options'] = 'nosniff'
	response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
	return response

def responsobility(request):
	response = render_to_response('responsobility.html',locals())
	response['Strict-Transport-Security'] = 'max-age=2592000'
	response['X-Frame-Options'] = 'SAMEORIGIN'
	response['Referrer-Policy'] = 'no-referrer'
	response['X-XSS-Protection'] = '1; mode=block'
	response['X-Content-Type-Options'] = 'nosniff'
	response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
	return response

def solution(request):
	response = render_to_response('solution.html',locals())
	response['Strict-Transport-Security'] = 'max-age=2592000'
	response['X-Frame-Options'] = 'SAMEORIGIN'
	response['Referrer-Policy'] = 'no-referrer'
	response['X-XSS-Protection'] = '1; mode=block'
	response['X-Content-Type-Options'] = 'nosniff'
	response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
	return response

def team(request):
	response = render_to_response('team.html',locals())
	response['Strict-Transport-Security'] = 'max-age=2592000'
	response['X-Frame-Options'] = 'SAMEORIGIN'
	response['Referrer-Policy'] = 'no-referrer'
	response['X-XSS-Protection'] = '1; mode=block'
	response['X-Content-Type-Options'] = 'nosniff'
	response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
	return response

def technology(request):
	response = render_to_response('technology.html',locals())
	response['Strict-Transport-Security'] = 'max-age=2592000'
	response['X-Frame-Options'] = 'SAMEORIGIN'
	response['Referrer-Policy'] = 'no-referrer'
	response['X-XSS-Protection'] = '1; mode=block'
	response['X-Content-Type-Options'] = 'nosniff'
	response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
	return response

def getimg_name(request):
	response = HttpResponse()
	response['Strict-Transport-Security'] = 'max-age=2592000'
	response['X-Frame-Options'] = 'SAMEORIGIN'
	response['Referrer-Policy'] = 'no-referrer'
	response['X-XSS-Protection'] = '1; mode=block'
	response['X-Content-Type-Options'] = 'nosniff'
	response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
	
	key = request.GET.keys()
	if "img" not in key or "location" not in key or len(key)>2 :
		response.write("Error")
		return response
	img = request.GET.get("img")
	location = request.GET.get("location")
	sign = ["=","%","@","+","-","$","*","/","#","!","?","^","&","<",">","'",'"']
	for i in sign:
		if i in img or i in location :
			response.write("Error")
			return response

	path = os.getcwd()+"/staticfiles/images/"+location+"/"+img
	try:
		image_data = open(path, "rb").read()
		# return JsonResponse({"path":path}, safe=False)
		response['Content-type'] = "image/png"
		response.write(image_data)
		return response
	except:
		response.write("Error")
		return response

def news_content(request):
	response = {
		'status':'ok'
	}
	
	title_list=[]#文楨標題
	content_list=[]#文章內文
	id_list=[]#文章id
	num=0#news的總文章數
	datetime = time.strftime("%Y-%m-%d")#目前日期
	int_datetime = time.mktime(time.strptime(datetime,"%Y-%m-%d"))#目前日期轉成數字
	datetime_list=[]#依照日期存成列表

	# 指定要列出所有檔案的目錄
	mypath = os.path.join(os.getcwd(), 'news_content')
	# 取得所有檔案與子目錄名稱
	files = glob.glob(os.path.join(mypath, '*'))#python2寫法
	# files = listdir(mypath)#python3寫法

	try:
		for f in files:
			#python3取得目錄下的檔案名稱後 需與路徑做結合 形成完整檔案路徑
			# file_path = os.path.join(mypath, f)
			# with open(file_path,'r',encoding='utf-8') as load_f:#python3開檔
			with open(f,'r') as load_f:#python2開檔寫法
				load_dict = json.load(load_f)
			
			int_vanish_time = time.mktime(time.strptime(load_dict['vanish_time'],"%Y-%m-%d"))
			if load_dict['species']	== "news" and int_vanish_time > int_datetime:#當文章分類為"新知分享" 與 文章消失日期>現在時間
				int_create_time = time.mktime(time.strptime(load_dict['create_time'],"%Y-%m-%d"))#將日期轉為數字
				# 將文章存成[(int(日期),'id','title','content'),(..).]
				datetime_list.append((int(int_create_time),load_dict['id'],load_dict['title'],load_dict['content']))
				#利用日期排順序,日期越往後排越前面
				datetime_list=sorted(datetime_list,key = lambda x : x[0],reverse=True)
				
				num+=1
		
		for d in datetime_list :
			id_list.append(d[1])
			title_list.append(d[2])
			content_list.append(d[3])

			response['title'] = title_list
			response['content'] = content_list
			response['id'] = id_list
			response['num'] = num


	except Exception as ex:
		# print(ex)
		pprint(traceback.format_exc())
		response['status'] = str(traceback.format_exc())

	return JsonResponse(response, safe=False)


def report_content(request):
	response = {
		'status':'ok'
	}
	
	title_list=[]#文楨標題
	content_list=[]#文章內文
	id_list=[]#文章id
	num=0#report的總文章數
	datetime = time.strftime("%Y-%m-%d")#目前日期
	int_datetime = time.mktime(time.strptime(datetime,"%Y-%m-%d"))#目前日期轉成數字
	datetime_list=[]#依照日期存成列表

	# 指定要列出所有檔案的目錄
	mypath = os.path.join(os.getcwd(), 'news_content')
	# 取得所有檔案與子目錄名稱
	files = glob.glob(os.path.join(mypath, '*'))#python2寫法
	# files = listdir(mypath)#python3寫法

	try:
		for f in files:
			#python3取得目錄下的檔案名稱後 需與路徑做結合 形成完整檔案路徑
			# file_path = os.path.join(mypath, f)
			# with open(file_path,'r',encoding='utf-8') as load_f:#python3開檔
			with open(f,'r') as load_f:#python2開檔寫法
				load_dict = json.load(load_f)
			
			int_vanish_time = time.mktime(time.strptime(load_dict['vanish_time'],"%Y-%m-%d"))
			if load_dict['species']	== "report" and int_vanish_time > int_datetime:#當文章分類為"新知分享" 與 文章消失日期>現在時間
				int_create_time = time.mktime(time.strptime(load_dict['news_date'],"%Y-%m-%d"))#將日期轉為數字
				# 將文章存成[(int(日期),'id','title','content'),(..).]
				datetime_list.append((int(int_create_time),load_dict['id'],load_dict['title'],load_dict['content']))
				#利用日期排順序,日期越往後排越前面
				datetime_list=sorted(datetime_list,key = lambda x : x[0],reverse=True)
				
				num+=1
		
		for d in datetime_list :
			id_list.append(d[1])
			title_list.append(d[2])
			content_list.append(d[3])

			response['title'] = title_list
			response['content'] = content_list
			response['id'] = id_list
			response['num'] = num


	except Exception as ex:
		# print(ex)
		pprint(traceback.format_exc())
		response['status'] = str(traceback.format_exc())

	return JsonResponse(response, safe=False)

def content_db(request):

	id_page=str(request.GET.get('id'))+'.json'

	response = {
		'status':'ok'
	}
	
	# 個別文章的路徑
	mypath = os.path.join(os.getcwd(), 'news_content')
	file_path = os.path.join(mypath,id_page)

	try:
		with open(file_path,'r') as load_f:#python2寫法
		# with open(file_path,'r',encoding='utf-8') as load_f:#python3寫法
			load_dict = json.load(load_f)

		response['title'] = load_dict['title']
		response['content'] = load_dict['content']
		response['user'] = load_dict['user']

	except Exception as ex:
		# print(ex)
		pprint(traceback.format_exc())
		response['status'] = str(traceback.format_exc())

	return JsonResponse(response, safe=False)


def sent_mail(request):
	idlist=0
	name = request.GET.get("name")
	email = request.GET.get("email")
	phone = request.GET.get("phone")
	option = request.GET.get("option")
	message = request.GET.get("message")
	datetime = time.strftime("%Y-%m-%d %H:%M:%S")
	contact_us = cs.objects.create(name=name,email=email,phone=phone,subject=option,message=message,time=datetime)
	
	return JsonResponse({})

# def after_request(request):
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#   return response