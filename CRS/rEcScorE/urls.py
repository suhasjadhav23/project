# __author__ = 'suhasjadhav'

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView
from rEcScorE import views

# from rEcScorE import views

urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    #  url(r'^$', IndexView.as_view(),name='index'),
    url(r'^$', TemplateView.as_view(template_name="rEcScorE/index.html")),
    url(r'^login/$', TemplateView.as_view(template_name="rEcScorE/signup.html")),
    url(r'^floww/$', TemplateView.as_view(template_name="rEcScorE/flow.html")),

    #   url(r'^$', views.indexView, name='indexView'),
    # url(r'^signupView/(\w*)', views.signupView, name='signupView')
    # # url(r'^$', views.signupView.as_view())

]
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

