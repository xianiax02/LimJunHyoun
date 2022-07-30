from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User #장고가 이미 가지고 있는 유저 객체
def login(request):
    if request.method=='POST':
        userid = request.POST['username']
        pwd = request.POST['password']#일단 파이썬 변수에 입력값을 저장해두고 autnticate 메소드로 비교
        user = auth.authenticate(request,username=userid,password=pwd)#사용자가 입력한 유저내임과 패스워드가 존재하는지를 검사해주는 장고 내장 메소드
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'bad_login.html')
    else:
        return render(request,'login.html')
    #POST 요청= 로그인처리, GET 요청= 로그인 폼 담고 있는 페이지 띄워주기
def logout(request):
    auth.logout(request)
    return redirect('home')

# Create your views here.

