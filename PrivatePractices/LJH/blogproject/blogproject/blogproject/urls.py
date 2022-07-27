"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    #using html
    path('new/',views.new, name='new'),
    path('create/',views.create, name='create'),
    #using django form
    path('formcreate/',views.formcreate, name='formcreate'),
    #using model form
    path('modelformcreate/',views.modelformcreate,name='modelformcreate'),
    path('detail/<int:blog_id>',views.detail,name='detail'),#index.html에서 같이 넘어온 id값을 int:blog_id에 담아 views.detail함수로 넘겨 실행한다.
    path('create_comment/<int:blog_id>',views.create_comment, name='create_comment'),
    path('login/', accounts_views.login, name = 'login'),
    path('logout/',accounts_views.logout,name='logout')

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 #media 파일에 접근할 수 있는 url 추가
