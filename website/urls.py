from django.contrib import admin
from django.urls import path
###
from website.views import *

app_name = 'website'

urlpatterns = [
    path('',home_index,name='index'),
    path('content',content_index,name='content'),
    path('pricing',pricing_index,name='pricing'),
    path('register',register_index,name='register'),
    path('terms',terms_index,name='terms')
]
