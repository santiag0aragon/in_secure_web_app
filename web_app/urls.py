from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^messages/', include('messages_app.urls')),
    url(r'^accounts/', include('profile.urls')),
    url(r'^create_user', include('user_auth.urls')),
)
