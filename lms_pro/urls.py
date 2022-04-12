from django.urls import path

from . import views

app_name = 'lms_pro'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]