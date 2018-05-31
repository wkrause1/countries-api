from django.conf.urls import url
from countries import views

urlpatterns = [
    url(r'^countries/$', views.country_list),
    url(r'^countries/(?P<country_code>[A-z]+)$', views.country_detail),
]