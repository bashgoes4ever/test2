# coding=utf-8
from django.urls import path
from .views import *


urlpatterns = [
    path('app/', AppView.as_view()),
    path('app/gen_key', KeyView.as_view()),
]