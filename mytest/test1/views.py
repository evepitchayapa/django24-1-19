from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
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
    stat={}
    for i in stat:
        if num == stat[i]:
            stat[i] = int(stat[i])+1
        else:
            stat[i] = 1
    lstval = []
    for i in range(12):
        lstval.append((i+1)*num)

    for i in stat:
        print (i)
        if ('num'+str(num)) == i:
            stat[i] +=1
            break
        else:
            stat['num'+str(num)]  = 1
            break

    context = {'num':num,'number':lstval,'stat':stat}

    return render(request,'test1/mul.html',context)

