from django.shortcuts import render

def calculator(request):
    return render(request,'calculator.html')
def maincal(request):
    return render(request,'main.html')

def formula(request):
    formula=request.GET['formula']
    answer=eval(formula)
    return render(request,'calculator.html',{'answer':answer})
# Create your views here.
