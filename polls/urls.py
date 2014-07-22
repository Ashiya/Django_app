from django.conf.urls import patterns ,url
from polls import views
urlpatterns=patterns('',
	url(r'^$', views.index , name='index'),
	url(r'^(?P<pid>\d+)/$', views.detail, name='detail'),

	url(r'^(?P<pid>\d+)/results/$', views.results, name='results'),
	# ex: /polls/5/vote/
	url(r'^(?P<pollid>\d+)/vote/$', views.vote, name='vote'),
	
	)