from django.urls import path 
from . import views 

urlpatterns = [
    path("",views.dashboard, name="dashboard"),
    path("market/", views.market, name="market"),
    # path("accounts/", views.accounts, name="accounts"),
    path('accounts/', views.add_account, name='accounts'),
    path("analytics/", views.analytics, name="analytics"),
    path("settings/", views.settings, name="settings"),
    path("Kyc/", views.Kyc, name="Kyc"),
    path('accounts/unlink/<int:account_id>/',views.unlink_account,name='unlink_account'),
    # path('market/delete/<int:listing_id>/', views.delete_listing, name='delete_listing'),
    path('market/delete/<int:pk>/', views.delete_listing, name='delete_listing'),
    path('market/delete_loan/<int:loan_id>/', views.delete_loan, name='delete_loan'),
]