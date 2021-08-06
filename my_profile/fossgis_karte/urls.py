from django.urls import re_path
from fossgis_karte import views

urlpatterns = [
    re_path(r'^$', views.help, name='help')
]