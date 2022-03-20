"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.contrib.auth.views import LoginView, LogoutView

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include # лаба 6
from django.contrib import admin # лаба 6
admin.autodiscover() # лаба 6

from django.conf.urls.static import static #лаба 10
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #лаба 10
from django.conf import settings #лаба 10
from django.views.generic import RedirectView

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^links$', app.views.links, name='links'),
    url(r'^pool$', app.views.pool, name='pool'),
    url(r'^blog', app.views.blog, name='blog'), # лаба 8
    url(r'^(?P<parametr>\d+)/$', app.views.blogpost, name='blogpost'), # лаба 8
    url(r'^newpost$', app.views.newpost, name='newpost'), # лаба 10
    url(r'^videopost$',app.views.videopost, name='videopost'), # лаба 10
    url(r'^registration$', app.views.registration, name='registration'), # лаба 6
    url(r'^developers$', app.views.developers, name='developers'),# new
    url(r'^catalog$', app.views.catalog, name='catalog'), # new1
    url(r'^basket$', app.views.basket, name='basket'),
    url(r'^(?P<parametr1>\d+)', app.views.delete, name='delete'), # new1
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Вход',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)), # лаба 6
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #лаба 10
urlpatterns += staticfiles_urlpatterns() #лаба 10