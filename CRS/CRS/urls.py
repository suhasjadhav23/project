from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', include('rEcScorE.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login', (admin.site.urls)),
    # url(r'^userprofile/userinfo', (admin.site.urls)),


    # mike hibbert tutorial to make login and registraion test
    # url(r'^flow/$', 'rEcScorE.views.FlowView'),
    url(r'^accounts/login/$',  'rEcScorE.views.login'),
    url(r'^accounts/auth/$',  'rEcScorE.views.auth_view'),
    url(r'^accounts/logout/$', 'rEcScorE.views.logout'),
    url(r'^accounts/loggedin/$', 'rEcScorE.views.loggedin'),
    url(r'^accounts/invalid/$', 'rEcScorE.views.invalid_login'),
    url(r'^accounts/sign_up/', 'rEcScorE.views.register_user'),
    url(r'^accounts/register_success/$', 'rEcScorE.views.register_success'),
    url(r'^accounts/confirm/(?P<activation_key>\w+)/','rEcScorE.views.register_confirm'),
    url(r'^userprofile/userinfo/(?P<userid>\d+)/$', 'rEcScorE.views.get_empprof'),
    url(r'^userprofile/myprofile/$', 'rEcScorE.views.myprofile'),
    url(r'^userprofile/editprofile/$', 'rEcScorE.views.editprofile'),


]




