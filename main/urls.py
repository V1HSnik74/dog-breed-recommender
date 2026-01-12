from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_survey_result/', views.get_survey_result, name='get_survey_result')
]
