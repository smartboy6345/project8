from india.views import *
from django.urls import path
app_name='anything'

urlpatterns=[
    path('shami/',shami,name='shami'),
]