from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def dashboard(request):
    user = request.user
    return render(request, "dashboard/dashboard.html")

# def user (request):
#     if user.is_authenticated():
#         return render(request, "dashboard/dashboard.html")
#     else:
#         return render (request,"registration/login.html ")

def market(request):
    return render(request, "dashboard/market.html")

def accounts(request):
    return render(request, "dashboard/accounts.html")

def analytics(request):
    return render(request, "dashboard/analytics.html")

def settings(request):
    return render(request, "dashboard/settings.html")