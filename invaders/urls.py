from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^invaders/', include('invaders.web.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    #(r'^$', 'invaders.web.views.index'),
    
    url(r'^layar_endpoint/$', 'invaders.web.views.invader_layar'),
    (r'^admin-media/(.*)', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT+'/admin-media', 'show_indexes' : True}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )


