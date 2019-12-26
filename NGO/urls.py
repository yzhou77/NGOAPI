"""NGO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include,url
from django.contrib.auth import login, logout
from django.views.static import serve
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path

from User import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('Event.url')),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    #url(r'^login/$', auth_view.LoginView.as_view(template_name='registration/login.html'), name='login'),
    #url(r'^logout/$', auth_view.LogoutView.as_view(template_name='User/logout.html'), name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^', include('User.urls', namespace='User')),
    url(r'^api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
