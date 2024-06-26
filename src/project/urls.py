"""
URL configuration for project project.

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

from django.conf import settings
from django.conf.urls.static import static

# Custom imports
from .views import homepage_view, contact_view, about_view, classes_view, save
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin', RedirectView.as_view(url='/admin/') ),
    path('', homepage_view, name="homepage"),
    path('contact/', contact_view, name="contact"),
    path('about', about_view, name="about"),
    path('classes', classes_view, name="classes"),
    path('save', save, name="save"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
