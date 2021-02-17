from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('session', views.session),
    path('destroy_session', views.destroy_session),
]