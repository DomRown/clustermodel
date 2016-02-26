from django.core import serializers
from models import *
from tests.testblobs import blob1
from django.views.generic import TemplateView
from django.shortcuts import render, render_to_response
from django.template import loader, RequestContext
from django.http import HttpResponse
from django.template.response import TemplateResponse,Template,Context
from django.shortcuts import render_to_response
import random,datetime,time,csv



def index(request):
	template = loader.get_template('index.html')
	return render(request,'index.html')

def pured3(request):
	start = time.clock()
 
	dataset=(request.POST.get('getset'))
	algorithm=(request.POST.get('getalg2'))
	numres=(request.POST.get('getnums'))
	klust=int(request.POST.get('getval'))
	print(time.clock() - start)
	if dataset=='IMDB - Ratings':
	 	settype="ratings"
	 	rows=Moviesall.values_list('rating_count','rating').exclude(rating_count__gte=100).exclude(rating_count__lt=1)[:numres]
	 	newrows=[]
	 	for i,e in enumerate(rows):
	 		x=(e[1]*10)
	 		#print int(x)
	 		newrows.append((e[0],int(x)))
	 	#print rows
	 	#print newrows

	 	#,'title','genres__genre','director__fullname','actors__fullname'
	elif dataset=='Iris':
	 	settype="iris"
	 	rows=Irisall.values_list('sepal_width','pet_length','species')[:numres]
	# elif dataset=='Blobs':
	# 	#settype=="blobs"
	# 	rows=blob1
	# elif dataset=='Crescents':
	# 	rows=crescent1
	# elif dataset=='Rings':
	# 	rows=circle1	
	else: return 0
	
	print(time.clock() - start)
	clusted=kmeans(newrows,k=klust)


	print(time.clock() - start)
	##Context takes two variables - a dict mapping var names to var vals
	##These vars are made available on scatter page
	context = RequestContext(request, {
		'data': json.dumps(clusted),
		'settype': json.dumps(settype), 
		'dataset':request.POST.get('getset'),
		'kclusters':request.POST.get('getval')
		})
	
	return render(request, 'scatterchart.html',context) 