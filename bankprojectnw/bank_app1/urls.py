from django.urls import path
from .import views

# app_name='bank_app1'
urlpatterns = [

    path('', views.index, name='index'),
    path('home/',views.home,name='home'),
    path('new/',views.new,name='new'),
    path('login/',views.loginuser,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.registerUser,name='register'),
    path('member/add/',views.create_view,name='list'),




]