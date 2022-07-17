import re
from winreg import REG_RESOURCE_REQUIREMENTS_LIST
from django.shortcuts import render

# Create your views here.
def Login(request):
    return render(request,'Login.html')
def start(request):
    return render(request,'index.html')
    