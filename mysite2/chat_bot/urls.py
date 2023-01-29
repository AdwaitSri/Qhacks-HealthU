from django.contrib import admin
from django.urls import path
from chat_bot import views

app_name='chat_bot'
urlpatterns=[
         path('',views.index,name='index'),
         


]
