from django.urls import re_path
from family_tree import views

# Template tagging

app_name = 'family_tree'

urlpatterns = [
    re_path(r'^treee/$', views.tree_page, name='tree_page'),
    re_path(r'^contact/$', views.contact_page, name='contact_page'),
    re_path(r'^register/$', views.register_page, name='register_page'),
    re_path(r'^login/$', views.login_page, name='login_page'),

]