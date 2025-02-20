"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path, include
from shop.views import MainPageView
from main.views import ContactsView

urlpatterns = [
    path('', MainPageView.as_view()),
    path('admin/', admin.site.urls),
    path('contacts/', ContactsView.as_view()),
    path('s/', include('shop.urls')),
]

from django.conf import settings
from django.views.static import serve

urlpatterns += [
    re_path(r'^files/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]

admin.site.site_header = 'Администрирование приложения'
admin.site.index_title = 'Интернет магазин pskovshevron.ru'
admin.site.site_title = 'Администрирование приложения'