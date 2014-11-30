from django.conf.urls import patterns, include, url
from mysite1.views import foo
from mysite1.views import login
from mysite1.views import signup
from mysite1.views import generate_user
from mysite1.views import generate_tag
from mysite1.views import generate_question
from mysite1.views import generate_answer

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login),
	url(r'^signup/', signup),
	url(r'^generateuser/', generate_user),
	url(r'^generatetag/', generate_tag),
	url(r'^generatequestion/', generate_question),
	url(r'^generateanswer/', generate_answer),
	url(r'^$', foo),
	
)