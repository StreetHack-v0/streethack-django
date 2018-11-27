# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'university/index.html')

def why(request):
	return render(request,'university/why.html')

def products(request):
	return render(request,'university/products.html')

def features(request):
	return render(request,'university/features.html')

def pricing(request):
	return render(request,'university/pricing.html')

def contact_us(request):
	return render(request,'university/contact_us.html')

def get_started(request):
	return render(request,'university/get_started.html')

