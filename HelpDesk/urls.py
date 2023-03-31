"""HelpDesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from users.views import auth, log_out
from main.views import home, claim, showclaim

urlpatterns = [
    path('admin/', admin.site.urls),
    path('claim/', claim),
    path('claim/<int:id>', showclaim),
    re_path(r'^accounts/login/$', auth, name='login'),
    re_path(r'^accounts/logout/$', log_out, name='logout'),
    path('', home)
]
