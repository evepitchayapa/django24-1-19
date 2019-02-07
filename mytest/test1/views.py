from django.shortcuts import render
from django.http import HttpResponse

def show_mul (request,num):
    context = {'number' :num}
    return render(request,'test1/mul.html',context)
