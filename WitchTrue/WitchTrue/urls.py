"""
Definition of urls for WitchTrue.
"""

from datetime import datetime
from app import views
from django.conf.urls import url
from django.conf.urls.static import static #6lab
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.conf import settings 
import django.contrib.auth.views

import app.forms
import app.views



from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^cart$', app.views.cart, name='cart'),
    url(r'^(?P<parametr>\d+)/deleteBlog$', app.views.deleteBlog, name='blogkek'),
    url(r'^(?P<parametr>\d+)/(?P<comm>\d+)/delete$', app.views.delete, name='delete'),
    
    
    url(r'^(?P<comm>\d+)/deletebasket$', app.views.deletebasket, name='deletebasket'),
    url(r'^(?P<comm>\d+)/incrementbasket$', app.views.incrementbasket, name='incrementbasket'),
    url(r'^(?P<comm>\d+)/decrementbasket$', app.views.decrementbasket, name='decrementbasket'),

    url(r'^(?P<parametr>\d+)/deleteall$', app.views.deleteall, name='deleteall'),
    
    url(r'^post$', app.views.post, name='post'),
    url(r'^blog$', app.views.blog, name='blog'),
    url(r'^$', app.views.news, name='news'),
    
    url(r'^$', app.views.newpost, name='newss'),
    
    url(r'^(?P<parametr>\d+)/$', app.views.blogpost, name='blogpost'),
    
    url(r'^(?P<parametr>\d+)/additem$', app.views.additem, name='additem'),
     
    url(r'^$', app.views.basket, name='basket'),
    
    
    url(r'^$', app.views.home, name='home'),
    
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^call$', app.views.call, name='call'),
    url(r'^links$', app.views.links, name='links'),
    url(r'^a1$', app.views.a1, name='a1'),
    url(r'^a2$', app.views.a2, name='a2'),
    url(r'^a3$', app.views.a3, name='a3'),
     url(r'^registration$', app.views.registration, name='registration'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
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
     url(r'^admin/', include(admin.site.urls)),
]
