__author__ = 'reza ghanbari'
# rezapython@gmail.com

from django.conf.urls import url
from . import views

'''
Creating an urls.py file for each app is the best way to make your
applications reusable by other projects.
'''

urlpatterns = [
    # post views
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/' \
        r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),

    url(r'^(?P<post_id>\d+)/share/$', views.post_share,
        name='post_share'),
]
