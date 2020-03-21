from django.urls import path
from currency import views
from django.contrib.auth import views as auth_views


app_name = 'currency'

urlpatterns = [
    path('download/rates/', views.RateCSV.as_view(), name='download-rates'),
]
