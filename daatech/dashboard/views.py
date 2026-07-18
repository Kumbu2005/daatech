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
