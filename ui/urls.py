from django.urls import path, re_path
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name='ui/index.html'), name="home"),
    path('create/', views.article_create, name='index'),
    path('embed/<str:urls>/', views.embed, name='embed'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)