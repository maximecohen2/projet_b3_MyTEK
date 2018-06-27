from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    
    url('celebrity/', TemplateView.as_view(template_name='celebrite.html'), name='celebrity'),
    url('playlist/', TemplateView.as_view(template_name='playList.html'), name='playlist'),
]
