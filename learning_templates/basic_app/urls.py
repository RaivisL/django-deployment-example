from django.conf.urls import url
from basic_app import views
from django.urls import path

# from . import views  ir tas pats kas augstaak vienu


# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns= [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name = 'other'),
]
