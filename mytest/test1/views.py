from django.shortcuts import render
from django.http import HttpResponse

def show_mul (request,num):


    context = {'number' :num,'1':num*1,'2':num*2,'3':num*3,'4':num*4,'5':num*5,
               '6':num*6,'7':num*7,'8':num*8,'9':num*9}
    return render(request,'test1/mul.html',context)
