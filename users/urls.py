from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^dashboard/$', views.Dashboard.as_view(), name="dashboard"),
    url(r'^record/$', views.Record.as_view(), name="record"),
    url(r'^logout/$', views.LogoutView.as_view(), name="logout"),
    url(r'^signup/$', views.SignUpView.as_view(), name="signup"),
    url('^', include('django.contrib.auth.urls')),
]