from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.index, name="index"),
    path("create/", views.create, name='post-create'),
    path("<slug:slug>/", views.detail, name="post-detail"),
    path("<slug:slug>/update/", views.update, name="post-update"),
    path("<slug:slug>/delete/", views.delete, name="post-delete"),
]