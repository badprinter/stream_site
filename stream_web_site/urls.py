"""
URL configuration for stream_web_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, re_path, include
from account import views as account_views
from account.Authentication import TokenCookieAuthentication

urlpatterns = [
    #    path('admin/', admin.site.urls),

    # Accout
    re_path('^login', account_views.UserLogin.as_view(), name='login'),
    re_path('^signup', account_views.UserSignup.as_view(), name='signup'),


    re_path(r'^api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    re_path(r'^api/v2/login', TokenCookieAuthentication.as_view(), name='token_login'),
]
