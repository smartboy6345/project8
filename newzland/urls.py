from newzland.views import *
from django.urls import path
app_name='anything'

urlpatterns=[
    path('wilimson/',wilimson,name='wilimson'),
    path('phlips/',phlips,name='phlips'),
]