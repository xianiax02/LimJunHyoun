from django.shortcuts import render

def namecard(request):
    return render(request,'namecard.html')