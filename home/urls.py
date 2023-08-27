from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='index'),
    path('post/', views.post, name='post'),
    path('store/', views.store, name='store'),
]
