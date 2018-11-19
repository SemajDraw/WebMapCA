from django.urls import include, re_path
from . import views
from api.views import tm_get_events

app_name = 'app'

urlpatterns = [
    re_path('^$', views.landing, name='landing'),
    re_path('^profile/$', views.profile, name='profile'),
    re_path('^profile/update_profile_pic/$', views.update_profile_pic, name='update_profile_pic'),
    re_path(r'^get_events/$', tm_get_events, name='get_events'),
]
