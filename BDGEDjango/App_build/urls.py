from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('build1/', views.build1, name='build1'),
    path('build2/', views.build2, name='build2'),
    path('build3/', views.build3, name='build3'),

]