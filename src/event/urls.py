from django.urls import path

from . import views

app_name = 'event'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('<slug:title>', views.eventDetails_view, name='detailPage')
]