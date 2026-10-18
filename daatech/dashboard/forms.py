from django import forms
from .models import Listing, Accounts, Kyc, loans
from django.contrib.auth.models import User



class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'amount','category',]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Item name'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Describe your item'
            }),

            'amount': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Amount'
            }),
        }
class loansForm(forms.ModelForm):
    class Meta:
        model = loans
        fields = ['title', 'description', 'amount','category',]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Item name'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Describe your item'
            }),

            'amount': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Amount'
            }),
            'category': forms.Select(attrs={
                'class': 'form-input'
            }),
        }

class linkedAccounts(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = ['bank','account_type','account_number' ]

class AccountSettingsForm(forms.ModelForm):

    first_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'settings-input',
            'placeholder': 'Enter your first name'
        })
    )

    last_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'settings-input',
            'placeholder': 'Enter your last name'
        })
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'settings-input',
            'placeholder': 'Enter your email address'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']



class KycForm(forms.ModelForm):
    class Meta:
        model = Kyc
        fields = ['business_name', 'business_address','business_registration_document', 'national_id', 'national_id_pic',
                   'business_logo', 'business_type', 'business_category', 'business_description',
                     'website', 'social_media_links', 'business_size', 'annual_revenue', 'number_of_employees', 
                     'years_in_business','bank_statements']

        widgets = {
                    'business_name': forms.TextInput(attrs={
                        'class': 'Kyc-form-input',
                        'placeholder': 'Business Name'
                    }),

                    'business_address': forms.TextInput(attrs={
                        'class': 'Kyc-form-input',
                        'placeholder': 'Business Address'
                    }),

                    'national_id': forms.TextInput(attrs={
                        'class': 'Kyc-form-input',
                        'placeholder': 'National ID Number'
                    }),

                    'business_type': forms.Select(attrs={
                        'class': 'Kyc-form-input'
                    }),
                    'business_category': forms.Select(attrs={
                        'class': 'Kyc-form-input'
                    }),
                    'business_description': forms.Textarea(attrs={
                        'class': 'Kyc-form-input',
                        'placeholder': 'Describe your business'
                    }),
                    'business_logo': forms.ClearableFileInput(attrs={
                        'class': 'Kyc-form-input',
                    }),
                    'business_address': forms.TextInput(attrs={
                        'class': 'Kyc-form-input',
                        'placeholder': 'Business Address'
                    }),
                    'website': forms.URLInput(attrs={
                        'class': 'Kyc-form-input',
                        'placeholder': 'Website URL'
                    }),
                    'social_media_links': forms.Textarea(attrs={
                        'class': 'Kyc-form-input',
                        'placeholder': 'Social Media Links'
                    }),
                    'business_size': forms.Select(attrs={
                        'class': 'Kyc-form-input'
                    }),
                    'annual_revenue': forms.NumberInput(attrs={
                        'class': 'Kyc-form-input',
                        'placeholder': 'Annual Revenue'
                    }),
                    'number_of_employees': forms.NumberInput(attrs={
                        'class': 'Kyc-form-input',
                        'placeholder': 'Number of Employees'
                    }),
                    'years_in_business': forms.NumberInput(attrs={
                        'class': 'Kyc-form-input',
                        'placeholder': 'Years in Business'
                    }),
                    'bank_statements': forms.ClearableFileInput(attrs={
                        'class': 'Kyc-form-input',
                    }),
        }