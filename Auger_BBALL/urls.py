"""
Definition of urls for Auger_BBALL.
"""

from datetime import datetime
from django.conf.urls import *
from app.forms import BootstrapAuthenticationForm



# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()









urlpatterns = patterns('',
    # Examples:
   
    
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^teams', 'app.views.teams', name='teams'),
    url(r'^team_detail/(?P<pk>[0-9]+)/$', 'app.views.team_detail', name='team_detail'),
    url(r'^season_detail/(?P<pk>[0-9]+)/$', 'app.views.season_detail', name='season_detail'),
    url(r'^player_detail/(?P<pk>[0-9]+)/$', 'app.views.player_detail', name='player_detail'),
    url(r'^game_detail/(?P<pk>[0-9]+)/$', 'app.views.game_detail', name='game_detail'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
