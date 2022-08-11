from django.contrib import admin
#django rest frmaework ->router->url
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register('post',views.PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]