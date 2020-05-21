#from django.conf.urls import  url
from django.urls import path
from basic_app import views
#Template tagging
app_name = 'basic_app' # look at the baisic_app and find the urls that matches
urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
