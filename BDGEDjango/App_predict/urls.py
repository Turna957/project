from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('pred1/', views.pred1, name='pred1'),
    path('pred2/', views.pred2, name='pred2'),
]