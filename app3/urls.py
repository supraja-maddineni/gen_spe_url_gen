from django.urls import path
from app3.views import *
app_name='nothing'
urlpatterns=[
    path('third/',third,name='third'),
    path('four/',four,name='four'),
]