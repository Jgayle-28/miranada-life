from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^addindex/', views.add_time_index, name="add_time_index")
]
