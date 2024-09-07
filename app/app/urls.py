from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('posts.urls'), name='index'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path("posts/", include("posts.urls")),
]
