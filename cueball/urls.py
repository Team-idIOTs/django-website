from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cues/', views.cues, name='cues'),
    path('monitor/', views.monitor, name='monitor'),
    path('settings/', views.settings, name='settings'),
]