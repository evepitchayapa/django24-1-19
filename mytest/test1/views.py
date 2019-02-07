from django.shortcuts import render
from django.http import HttpResponse

def show_mul (request,num):
    response = str(num) *3
    return render("%s" %response)
