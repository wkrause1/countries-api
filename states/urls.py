from django.conf.urls import url
from states import views
from django.urls import path

urlpatterns = [
    url(r'^countries/(?P<country_code>[A-z]+)/states/', views.state_list),
    #url('^<state>', views.state_delete),
    url(r'^countries/(?P<country_code>[A-z]+)/(?P<state>[A-z]+)', views.state_detail),
]