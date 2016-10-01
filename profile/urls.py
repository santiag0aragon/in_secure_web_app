from django.conf.urls import patterns, url

urlpatterns = patterns(
    'profile.views',
    url(r'login/$', 'login'),
    url(r'auth/$', 'auth_view'),
    url(r'logout/$', 'logout', name='logout'),
    url(r'invalid/$', 'invalid_login'),
)
