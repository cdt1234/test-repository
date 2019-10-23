from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def main(request):
    return render(request,"index－数据概要.html")

def rende(request):
    return render(request,"render.html")

def biao(request):
    return render(request,'表格.html')

def tiao(request):
    return render(request,'条形图.html')

def bing(request):
    return render(request,'饼状图.html')

def data(request):
    return render(request,'data.html')