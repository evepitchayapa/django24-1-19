from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Number

def show_mul (request,num):
    lstval = []
    for i in range(12):
        lstval.append(str((i+1)*num))

    context = {'num':num,'number':lstval}

    # context = {'number' :num,'num1':num*1,'num2':num*2,'num3':num*3,'num4':num*4,'num5':num*5,
    #            'num6':num*6,'num7':num*7,'num8':num*8,'num9':num*9}

    # context = {'num':num}
    # for i in range(12):
    #     context['number'+str(i+1)] = num*(i+1)
    return render(request,'test1/mul.html',context)

def input (request):
    return render(request,'test1/input.html')



def showresult (request):

    num = int(request.POST['add_number'])
    lstval = []
    for i in range(12):
        lstval.append((i+1)*num)

    data_number = Number
    update_data = data_number.number_text.get(pk=num)
    update_data.counter_number += 1


    context = {'num':num,'number':lstval}

    return render(request,'test1/mul.html',context)

