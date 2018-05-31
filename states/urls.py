from django.conf.urls import url
from states import views
from django.urls import path

urlpatterns = [
    url(r'^countries/(?P<country_code>[A-z]+)/states/', views.state_list),
    #url('countries/<country_code>/states/', views.state_list),
   # url(r'^countries/(?P<country_code>[A-Z]+)/states', views.state_detail),
]