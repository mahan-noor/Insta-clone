from django.urls import path,re_path
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    re_path('accounts/profile/(\d+)',views.profile,name = 'profile'),
    path('accounts/create',views.create,name = 'create'),
    path('accounts/updateProfile',views.updateProfile,name = 'updateProfile'),






]