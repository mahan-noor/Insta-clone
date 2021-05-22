from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    path('accounts/profile/(\d+)',views.profile,name = 'profile'),




]