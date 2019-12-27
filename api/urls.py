from django.conf.urls import  url

from . import views

urlpatterns = [
    url(r'^users/$', views.user_list, name='api_user_list'),
    url(r'^users/(?P<pk>[0-9]+)$', views.user_detail, name='api_user_detail'),
    url(r'^events1/$', views.event_list, name='api_event_list1'),
    #url(r'^events1/(?P<pk>[0-9]+)$', views.event_detail1, name='api_event_detail1'),
    url(r'^registrations/$', views.registration_list, name='api_registration_list'),
    url(r'^registrations/(?P<pk>[0-9]+)$', views.registration_detail, name='api_registration_detail'),
    url(r'^upload/', views.ImageViewSet.as_view(), name='upload'),
    url(r'^events/$', views.EventList.as_view(), name='api_event_list'),
    url(r'^events2/', views.EventList2.as_view(), name='api_event_list'),
    url(r'^events2/(?P<pk>[0-9]+)$', views.EventDetail.as_view(), name='api_event_detail'),
    url(r'^events/(?P<pk>[0-9]+)$', views.event_detail, name='api_event_detail1'),
]
