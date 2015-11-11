from django.conf.urls import patterns, url

from transactions import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<pk>\d+)/$',
                           views.DetailView.as_view(), name='detail'),
                       url(r'^(?P<pk>\d+)/results/$',
                           views.ResultsView.as_view(), name='results'),
                       url(r'^flow/$', views.FlowView.as_view(), name='flow'),
                       url(r'^(?P<account_id>\d+)/deal/$',
                           views.deal, name='deal'),
                       )
