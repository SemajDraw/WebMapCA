from django.urls import include, re_path
from . import views

app_name = 'api'

urlpatterns = [
    re_path(r'^login/$', views.token_login, name='token_login'),
    re_path(r'^get_events/$', views.tm_get_events, name='get_events'),
]
