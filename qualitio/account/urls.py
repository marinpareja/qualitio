from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
                       url(r'', 'qualitio.account.views.index')
                       )
