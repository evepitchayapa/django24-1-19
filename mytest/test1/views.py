from django.shortcuts import render
from django.http import HttpResponse

def show_mul (request,num):


    context = {'number' :num,'num1':num*1,'num2':num*2,'num3':num*3,'num4':num*4,'num5':num*5,
               'num6':num*6,'num7':num*7,'num8':num*8,'num9':num*9}
    return render(request,'test1/mul.html',context)

def input (request):
    return render(request,'test1/input.html')

def showinput (request):
    num = request.POST['add_number']

    context = {'number' :num,'num1':num*1,'num2':num*2,'num3':num*3,'num4':num*4,'num5':num*5,
               'num6':num*6,'num7':num*7,'num8':num*8,'num9':num*9}

    return render(request,'mul.html',context)
