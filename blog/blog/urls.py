from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^index/', 'blogs.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/', 'blogs.views.login_view'),
    url(r'^(?P<blog_name>\w+)/$', 'blogs.views.index'),
    url(r'^(?P<blog_name>\w+)/(?P<post_id>\d+)/$', 'blogs.views.view'),
    url(r'^(?P<blog_name>\w+)/blogs/comment/$', 'blogs.views.comment'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   
)
