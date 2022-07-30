from urllib import response
from django.shortcuts import render
import requests
import json
from .forms import *
# Create your views here.

myid='4e04845cea160466d1ce4d03772965b2'

def home(request):
    if request.method=='POST':
        form=SearchForm(request.POST)
        searchword=request.POST.get('search')
        if form.is_valid():
            url='https://api.themoviedb.org/3/search/movie?api_key='+myid+'&query='+searchword
            response=requests.get(url)
            resdata=response.text
            obj=json.loads(resdata)
            obj=obj['results']
            return render(request,'search.html',{'obj':obj})

    else:
        form=SearchForm()
        url='https://api.themoviedb.org/3/trending/all/day?api_key='+myid
        response=requests.get(url)
        resdata=response.text#안의 정보에 접근하려면 .text
        obj=json.loads(resdata)#json객체을 파이썬 객체로 바꿔서 파이썬 문법으로 이용하려면... 
        obj=obj['results']
        return render(request,'index.html',{'obj':obj,'form':form})
def detail(request,movieid):#해당 url에 겟 요청 보내고 아이디 받기
    url='https://api.themoviedb.org/3/movie/'+movieid+'?api_key='+myid
    response=requests.get(url)
    resdata=response.text
    return render(request,'detail.html',{'resdata':resdata})