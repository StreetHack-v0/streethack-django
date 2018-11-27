# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'events/index.html')

def wsoc2018(request):
	return render(request,'events/wsoc2018.html')

def blockhack2019(request):
	return render(request,'events/blockhack2019.html')

def blockchain_in_business(request):
	return render(request,'events/blockchain_in_business.html')

def streethack_2019_1(request):
	return render(request,'events/streethack_2019_1.html')

