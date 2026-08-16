from django.urls import path 
from . import views 

urlpatterns = [
    path("",views.dashboard, name="dashboard"),
    path("market/", views.market, name="market"),
    path("accounts/", views.accounts, name="accounts"),
    path("analytics/", views.analytics, name="analytics"),
    path("settings/", views.settings, name="settings")
]