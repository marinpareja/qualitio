from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'', include('social_auth.urls')),
                       (r'^logout/$', 'django.contrib.auth.views.logout',
                        {'next_page' : '/'}),
                       (r'^login/', 'django.contrib.auth.views.login',
                        {'template_name': "registration/login.html"}),

                       (r'^register/', 'registration.views.register',
                        {'template_name': "registration/registration.html",
                         'backend': 'registration.backends.simple.SimpleBackend',
                         'success_url': 'django.contrib.auth.views.login' }),

                       (r'^permission_required/$', 'qualitio.core.permission_required'),

                       (r'^require/', include('qualitio.require.urls', app_name="require")),
                       (r'^settings/', include('qualitio.projects.urls')),
                       (r'^execute/', include('qualitio.execute.urls', app_name="execute")),
                       (r'^store/', include('qualitio.store.urls', app_name="store")),
                       (r'^report/', include('qualitio.report.urls', app_name="report")),

                       (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       (r'^admin/', include(admin.site.urls))

                       )

urlpatterns += patterns('django.views.generic.simple',
                        ('^$', 'redirect_to', {'url': 'require/'}),
                        )

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                            )

