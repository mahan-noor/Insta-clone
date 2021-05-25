from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name = 'index'),
    re_path('accounts/profile/(\d+)',views.profile,name = 'profile'),
    path('accounts/create',views.create,name = 'create'),
    path('accounts/updateProfile',views.updateProfile,name = 'updateProfile'),
    path('accounts/search',views.search,name = 'search'),
    re_path('accounts/single/(\d+)',views.single,name = 'single'),
    re_path('like/(\d+)',views.likePost,name= 'likePost'),
    re_path('follow/(\d+)',views.follow,name="user_follow"),
    re_path('editPost/(\d+)',views.editPost,name="editPost"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)