from django.conf.urls import patterns, include, url
from mysite1.views import foo
from mysite1.views import login
from mysite1.views import signup

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', foo),
	url(r'^login/', login),
	url(r'^signup/', signup),
)