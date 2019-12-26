from django.conf.urls import url
from User import views


app_name = 'Myuser'

urlpatterns = [
    #url('', HomePageView.as_view() , name='login'),
    url('user/', views.user_list, name='user_list' ),
    url('new/', views.user_new, name='user_new'),
    url('delete/(?P<pk>\d+)', views.user_delete, name='user_delete'),
    url('edit/(?P<pk>\d+)', views.user_edit, name='user_edit'),
]