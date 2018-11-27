# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'enterprise/index.html')

def why(request):
	return render(request,'enterprise/why.html')

def products(request):
	return render(request,'enterprise/products.html')

def features(request):
	return render(request,'enterprise/features.html')

def pricing(request):
	return render(request,'enterprise/pricing.html')

def contact_us(request):
	return render(request,'enterprise/contact_us.html')

def get_started(request):
	return render(request,'enterprise/get_started.html')

