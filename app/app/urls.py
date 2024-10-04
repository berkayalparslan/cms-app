from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('silk/', include('silk.urls', namespace='silk')),
    path('admin/', admin.site.urls),
    path('',include('posts.urls'), name='index'),
    path('users/', include('users.urls')),
    path("posts/", include("posts.urls")),
    
]


