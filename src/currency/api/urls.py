from django.urls import path
from currency.api import views
from django.contrib.auth import views as auth_views


app_name = 'api-currency'

urlpatterns = [
    path('rates/', views.RatesView.as_view(), name='rates'),
    path('rate/<int:pk>', views.RateView.as_view(), name='rate'),
]
