from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views 


urlpatterns = [
    # Examples:
    # url(r'^$', 'love.views.home', name='home'),
    url(r'^add/$', 'mysite.views.add', name='add'),
    url(r'^delete/(?P<pk>\d+)/$', 'mysite.views.delete', name='delete'),
    url(r'^show/$', 'mysite.views.show', name='show'),
    url(r'^login/$', views.login, {'template_name':'forms.html','extra_context': {'title':"Welcome"}}),
    # url(r'^contact/$', 'love.views.contact', name='contact'),
    url(r'^leaderboard/$', 'mysite.views.home1', name='leaderboard'),
    # url(r'^register/$', 'leaderboard.views.register', name='register'),
    url(r'^login1/$', 'love.views.login1', name='login1'),
    url(r'^currency/login/$', 'currency.views.login1', name='login2'),
    # # url(r'^signup/$', 'leaderboard.views.signup', name='signup'),
    # url(r'^marks/$', 'leaderboard.views.', name='marks'),
    url(r'^currency/register/$', 'currency.views.register', name='register'),
    url(r'^converter/$', 'currency.views.converter', name='converter'),

    # # url(r'^blog/', include('blog.urls')),
    url(r'^', include('mysite.urls')),
    url(r'^currency/$','currency.views.home',name='currency'),
    url(r'^logout/$', views.logout,{"next_page":"/"}),
    url(r'^admin/', include(admin.site.urls)),
    
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)