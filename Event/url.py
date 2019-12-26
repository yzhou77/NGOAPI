from django.conf.urls import include,url
from .models import Event
#from productapp.views import ClassPostView
from django.views.generic import DetailView, ListView, UpdateView

from . import views
from . import forms
from django.contrib.auth import views as auth_views

urlpatterns = [
	# url(r'^showtime/$',views.showdatetime)
    url(r'^$',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	url(r'^event/(?P<pk>\d+)$',views.event_details,name='event_details'),
	url(r'^event/new/$',views.event_new,name='event_new'),
	url(r'^event/create/$',
	 	views.EventCreate.as_view(),
	 	name='event_create'),
	url(r'^event/(?P<pk>\d+)/edit/$',
		UpdateView.as_view(
			model=Event,
			template_name='eventform.html',
			success_url='',
			form_class=forms.PForm),
		name='event_edit'),
    url(r'^event/(?P<pk>\d+)/edit/update/$',views.update),
    url(r'^event/(?P<pk>\d+)/registration/$',views.event_registration,name='event_registration'),
	url(r'^userview/$',views.user_view,name='user_view'),
    url(r'^login/new/$',views.event_list,name='event_list'),
    url(r'^event/registration/(?P<pk>\d+)$',views.registration_details,name='registration_details'),
    url(r'^event/registration/(?P<pl>\d+)/(?P<pk>\d+)/confirmation$',views.registration_confirmation,name='registration_confirmation'),
	url(r'^event/registration/(?P<pk>\d+)/confirmation/confirmed$',views.confirmed,name='confirmed'),
]
