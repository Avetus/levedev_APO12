from django.conf.urls import patterns, include, url
from mysite1.views import params

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', params),
	url(r'^login/', params),
	url(r'^signup/', params),
)