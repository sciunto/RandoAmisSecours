# -*- coding: utf-8 -*-
# vim: set ts=4

# Copyright 2013 Rémi Duraffort
# This file is part of RandoAmisSecours.
#
# RandoAmisSecours is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# RandoAmisSecours is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with RandoAmisSecours.  If not, see <http://www.gnu.org/licenses/>

from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy

from RandoAmisSecours.views.account import RASAuthenticationForm, RASPasswordChangeForm, RASPasswordResetForm, RASSetPasswordForm


# Main page
urlpatterns = patterns('RandoAmisSecours.views.main',
    url(r'^$', 'index', name='index'),
)

# Authentication
urlpatterns += patterns('django.contrib.auth.views',
    url(r'^accounts/login/$', 'login', {'template_name': 'RandoAmisSecours/account/login.html', 'authentication_form': RASAuthenticationForm}, name='accounts.login'),
    url(r'^accounts/logout/$', 'logout', {'template_name': 'RandoAmisSecours/account/logged_out.html'}, name='accounts.logout'),
    url(r'^accounts/password/change/$', 'password_change', {'template_name': 'RandoAmisSecours/account/password_change.html', 'password_change_form': RASPasswordChangeForm, 'post_change_redirect': reverse_lazy('accounts.password_change_done')}, name='accounts.password_change'),
    url(r'^accounts/password/reset/$', 'password_reset', {'template_name': 'RandoAmisSecours/account/password_reset.html', 'email_template_name': 'RandoAmisSecours/account/password_reset_email.txt', 'password_reset_form': RASPasswordResetForm, 'post_reset_redirect': reverse_lazy('accounts.password_reset_done')}, name='accounts.password_reset'),
    url(r'^accounts/password/reset/confirm/(?P<uidb36>[0-9A-Za-z]{1,13})/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'password_reset_confirm', {'template_name': 'RandoAmisSecours/account/password_reset_confirm.html', 'set_password_form': RASSetPasswordForm}, name='accounts.password_reset_confirm'),
    url(r'^accounts/password/reset/complete/$', 'password_reset_complete', {'template_name': 'RandoAmisSecours/account/password_reset_complete.html'}, name='accounts.password_reset_complete'),
)

urlpatterns += patterns('RandoAmisSecours.views.account',
    url(r'^accounts/register/$', 'register', name='accounts.register'),
    url(r'^accounts/register/(?P<user_id>\d+)/confirm/(?P<user_hash>\w+)/$', 'register_confirm', name='accounts.register.confirm'),
    url(r'^accounts/profile/$', 'profile', name='accounts.profile'),
    url(r'^accounts/profile/update/$', 'update', name='accounts.profile.update'),
    url(r'^accounts/password/change/done/$', 'password_change_done', name='accounts.password_change_done'),
    url(r'^accounts/password/reset/done/$', 'password_reset_done', name='accounts.password_reset_done'),
)

urlpatterns += patterns('RandoAmisSecours.views.friends',
    url(r'^friends/search/$', 'search', name='friends.search'),
    url(r'^friends/invite/(?P<user_id>\d+)/$', 'invite', name='friends.invite'),
)

# Outing
urlpatterns += patterns('RandoAmisSecours.views.outing',
    url(r'^outings/$', 'index', name='outings.index'),
    url(r'^outings/draft/$', 'index', {'status': 'draft'}, name='outings.index.draft'),
    url(r'^outings/finished/$', 'index', {'status': 'finished'}, name='outings.index.finished'),
    url(r'^outings/late/$', 'index', {'status': 'late'}, name='outings.index.late'),
    url(r'^outings/canceled/$', 'index', {'status': 'canceled'}, name='outings.index.canceled'),
    url(r'^outings/create/$', 'create', name='outings.create'),
    url(r'^outings/(?P<outing_id>\d+)/$', 'details', name='outings.details'),
    url(r'^outings/(?P<outing_id>\d+)/update/$', 'update', name='outings.update'),
    url(r'^outings/(?P<outing_id>\d+)/delete/$', 'delete', name='outings.delete'),
    url(r'^outings/(?P<outing_id>\d+)/confirm/$', 'confirm', name='outings.confirm'),
    url(r'^outings/(?P<outing_id>\d+)/finish/$', 'finish', name='outings.finish'),
)
