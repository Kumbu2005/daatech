from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Listing, Accounts, loans
from django.db.models import Q
from .forms import KycForm, ListingForm, linkedAccounts, AccountSettingsForm, loansForm

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

# def market(request):
#     return render(request, "dashboard/market.html")

# def accounts(request):
#     return render(request, "dashboard/accounts.html")

def analytics(request):
    return render(request, "dashboard/analytics.html")

def Kyc(request):
    if request.method == 'POST':
        form = KycForm(request.POST, request.FILES)

        if form.is_valid():
            kyc = form.save(commit=False)
            kyc.user = request.user
            kyc.save()

            return redirect('dashboard')

    else:
        form = KycForm()

    return render(request, "dashboard/Kyc.html", {
        'form': form,
    })

def settings(request):
    if request.method == 'POST':
        form = AccountSettingsForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('settings')

    else:
        form = AccountSettingsForm(instance=request.user)

    return render(request, 'dashboard/settings.html', {
        'form': form
    })



def market(request):

    category = request.GET.get('category', '')
    

    if not request.user.profile.user_type == 'SME':
        listings = Listing.objects.all().order_by('-created_at')

    elif request.user.profile.user_type == 'SME':
        listings = Listing.objects.filter(borrower=request.user).order_by('-created_at')
    else:
        listings = Listing.objects.none()

    if category:
        listings = listings.filter(category=category)

    loan_offers = loans.objects.all().order_by('-created_at')

    form = ListingForm()
    loan_form = loansForm()

    if request.method == 'POST':

       
        if 'listing_submit' in request.POST:

            form = ListingForm(request.POST, request.FILES)

            if form.is_valid():
                listing = form.save(commit=False)
                listing.borrower = request.user
                listing.save()

                return redirect('market')

        
        elif 'loan_submit' in request.POST:

            loan_form = loansForm(request.POST, request.FILES)

            if loan_form.is_valid():
                loan = loan_form.save(commit=False)
                loan.lender = request.user
                loan.save()

                return redirect('market')

    return render(request, 'dashboard/market.html', {
        'listings': listings,
        'loan_offers': loan_offers,
        'form': form,
        'loan_form': loan_form,
        'category': category,
    })

def add_account(request):
    user_accounts = Accounts.objects.filter(user=request.user)
    if request.method == 'POST':
        form = linkedAccounts(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            return redirect('accounts')
    else:
        form = linkedAccounts()

    return render(request, 'dashboard/accounts.html', {
        'form': form,
        'user_accounts': user_accounts
    })

def unlink_account(request, account_id):
    account = Accounts.objects.get(
        id=account_id,
        user=request.user
    )

    if request.method == 'POST':
        account.delete()

    return redirect('accounts')

# def delete_listing(request, listing_id):
#     listing = Listing.objects.get(
#         id=listing_id,
#         borrower=request.user
#     )

#     if request.method == 'POST':
#         listing.delete()

#     return redirect('market')

from django.shortcuts import get_object_or_404, redirect

def delete_listing(request, pk):
    if request.method == "POST":
        listing = get_object_or_404(Listing, pk=pk, borrower=request.user)
        listing.delete()

    return redirect('market')



def delete_loan(request, loan_id):

    if request.method == 'POST':
    
            loan = get_object_or_404(loans,id=loan_id,lender=request.user)
            loan.delete()
    
    return redirect('market')