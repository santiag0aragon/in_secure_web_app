from django.conf.urls import patterns, url

urlpatterns = patterns(
    'user_auth.views',
    url(r'/$', 'create_user')
)
