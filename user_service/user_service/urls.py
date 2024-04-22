"""
URL configuration for user_service project.

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
from django.urls import path
from user_model import views as user_model_view
from user_login import views as user_login_view
from user_info import views as user_info_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userregistration/', user_model_view.registration_req, name='registration'),
    path('userlogin/', user_login_view.user_login, name='user_login'),
    path('userinfo/', user_info_view.user_info, name='user_info'),
]
