from django.urls import path

from . import views

urlpatterns = [
    path('', views.article_create, name='index'),
    path('embed/<str:url>/', views.embed, name='embed'),
]