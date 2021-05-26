from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name = 'home'),
    path('email/',views.email,name = 'email'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    re_path('profile/(?P<profile_id>\d+)',views.profile,name = 'profile'),
    path('upload/image', views.upload_image, name = "upload_image"),
    path('search/',views.search,name ='search'),
    re_path('like/(?P<image_id>\d+)', views.like_image, name = 'like_image'),
    re_path('comment/(?P<image_id>\d+)', views.comment,name = "comment"),
    path('profile/edit', views.profile_edit,name = 'profile_edit'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)