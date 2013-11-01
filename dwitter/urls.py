from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dwitter.views.home', name='home'),
    # url(r'^dwitter/', include('dwitter.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'website/login.html'}, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^delete_tweet/(\d+)/$', 'website.views.delete_tweet', name="delete_tweet"),
    url(r'^retweet/(\d+)/$', 'website.views.retweet', name="retweet"),
    url(r'^tweet/(\d+)/$', 'website.views.tweet_page', name="tweet-page"),
    url(r'^user/(\w+)/$', 'website.views.user_page', name="user-page"),
    url(r'^users/$', 'website.views.users_list', name="users-list"),
    url(r'^mentions/$', 'website.views.mentions_page', name="mentions-page"),
    url(r'^$', 'website.views.timeline', name="timeline"),
)
