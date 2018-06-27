from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [

    url('grouplist/', TemplateView.as_view(template_name='grouplist.html'), name='grouplist'),
]
