from dataclasses import fields
from msilib.schema import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Blog
from django.utils import timezone
from .forms import BlogForm,BlogModelForm,commentform


def home(request):
    posts=Blog.objects.all()#데이터베이스에서 블로그 객체들을 모두 불러와서 html에 찍히게 하기
    #posts=Blog.objects.filter().order_by('-date')이건 최신거 위에로 정렬해서 갖고 오기 'date'는 옛날게 위에
    return render(request, 'index.html',{'posts':posts})
#블로그 글 작성 html보여주는 함수
def new(request):
    return render(request, 'new.html')
#블로그 글 저장해주는 함수
def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')
#using django form
#get(입력값을 받을 수 있는 html을 갖다 줘야함) post(입력한 내용을 데이터베이스에 저장) 둘다 처리 가능
def formcreate(request):
    if request.method=='POST' :
        form=BlogForm(request.POST)
        if form.is_valid():
            post=Blog()
            post.title=form.cleaned_data['title']
            post.body=form.cleaned_data['body']
            post.save()
            return redirect('home')
    

        #입력 내용을 DB에 저장
    if(request.method=='GET'): 
        #입력을 받을 수 있는 html 갖다 주기
        form=BlogForm()
    return render(request,'formcreate.html', {'form':form})   
def modelformcreate(request):
    if request.method=='POST' or request.method == 'FILES':
        form=BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    if request.method=='GET':
        form=BlogModelForm()
    return render(request,'formcreate.html',{'form':form})
def detail(request,blog_id):
    blogdetail=get_object_or_404(Blog,pk=blog_id)
    #blog_id 번째 블로그 글을 데이터베이스로부터 갖고오는 코드
    comment_form=commentform()
    return render(request,'detail.html',{'blog_detail':blogdetail, 'comment_form':comment_form})
    #blog_id 번째 블로그 글을 detail.html로 띄워주는 코드

def create_comment(request,blog_id):
    filled_form=commentform(request.POST)

    if filled_form.is_valid():

        finished_form= filled_form.save(commit=False)#아직 저장하지 말고 대기해
        finished_form.post=get_object_or_404(Blog,pk=blog_id)
        finished_form.save()

        return redirect('detail', blog_id)


# Create your views here.
'''
class BlogView(ListView):               #html: 블로그 리스트를 담은 것:(소문자모델)_list.html
    temlate_name='blogapp/list.html'
    context_object_name='blog_list'
    model=Blog

class BlogCreate(CreateView):           #html: form(입력공간)를 담은 것:(소문자모델)_form.html
    model=Blog
    fields=['title','body']
    success_url=reverse_lazy('list')

class BlogDetail(DetailView):           #html: 상세 페이지를 담은 것:(소문자모델)_detail.html
    model=Blog

class BlogUpdate(UpdateView):           #html: form(입력공간)를 담은 것:(소문자모델)_form.html
    model=ClassBlog
    fields=['title','body']
    success_url=reverse_lazy('list')

class BlogDelete(DeleteView):           #html: 진짜 지울것인지를 담은 것:(소문자모델)_delete_confirm.html
    model=Blogsuccess_url=reverse_lazy('list')
    '''