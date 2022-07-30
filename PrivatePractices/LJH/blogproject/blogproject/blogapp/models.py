from pyexpat import model
from tkinter import CASCADE
from django.db import models

class Blog(models.Model): # 모델 객체 상속 받아 선언
    title=models.CharField(max_length=200)
    body=models.TextField()
    photo=models.ImageField(blank=True, null=True, upload_to='blog_photo')#사진 추가할때마다 미디어 안의 블로그포토 폴더에 자동으로 저장하겠다.
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title #제목이 앞에 뜨게 타이틀 속성을 지정
    
class comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Blog, on_delete=models.CASCADE)#cascade-->삭제되면 그 게시물을 참조하고 있는 코멘트 모델도 삭제한다. 어떤 게시물에 달린 댓글인지를 알 수 있는, 포스트 객체에 대한 외래키, 참조할 것임
    
    def __str__(self):
        return self.comment

# Create your models here.
