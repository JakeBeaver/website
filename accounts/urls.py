from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
     url(r'^login//?$', 'accounts.views.login', name='login'),
     url(r'^logout//?$', 'accounts.views.logout', name='logout'),
     url(r'^auth//?$', 'accounts.views.authenticate', name='auth'),
     url(r'^loggedin//?$', 'accounts.views.loggedin', name='ok'),
     url(r'^invalid//?$', 'accounts.views.invalid', name='invalid'),
     url(r'^register//?$', 'accounts.views.register_user', name='register'),
     url(r'^register_success//?$', 'accounts.views.register_success', name='register success'),
]
