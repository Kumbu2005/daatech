from django.db import models
from django.contrib.auth.models import User


class Listing(models.Model):

    CATEGORY_CHOICES = [
        ('agriculture', 'Agriculture'),
        ('vehicles', 'Vehicles'),
        ('property', 'Property'),
        ('equipment', 'Equipment'),
        ('office', 'Office Supplies'),
        ('other', 'Other'),
    ]


    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Accounts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.CharField(max_length=100)
    account_type = models.CharField(max_length=50)
    account_number = models.CharField(max_length=20, unique=True, error_messages={
            'unique': 'Invalid Account number.'
        })

    def __str__(self):
        return f"{self.bank} - {self.account_type} - {self.account_number}"

class Kyc(models.Model):

    CATEGORY_CHOICES = [
            ('agriculture', 'Agriculture'),
            ('hardware', 'Hardware'),
            ('pharmacy', 'Pharmacy'),
            ('grocery', 'Grocery'),
            ('superMarket', 'Super Market'),
            ('other', 'Other'),
        ]
    TYPE_CHOICES = [
            ('sole_proprietorship', 'Sole Proprietorship'),
            ('partnership', 'Partnership'),
            ('corporation', 'Corporation'),
            ('limited_liability_company', 'Limited Liability Company (LLC)'),
            ('cooperative', 'Cooperative'),
            ('non_profit', 'Non-Profit Organization'),
            ('franchise', 'Franchise'),
            ('joint_venture', 'Joint Venture'),
            ('other', 'Other'),
        ]
    SIZE_CHOICES = [
            ('small', 'Small'),
            ('medium', 'Medium'),
            ('large', 'Large'),
        ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)
    business_address = models.CharField(max_length=200)
    national_id = models.CharField(max_length=20, unique=True, blank=True, null=True, error_messages={'unique': 'Invalid National ID.'})
    national_id_pic = models.ImageField(upload_to='kyc_documents/', blank=True, null=True)
    business_registration_document = models.FileField(upload_to='kyc_documents/', blank=True, null=True)
    business_logo = models.ImageField(upload_to='kyc_documents/', blank=True, null=True)
    business_type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='other')        
    business_category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='other')
    business_description = models.TextField(max_length=500, blank=True, null=True) 
    annual_revenue = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    number_of_employees = models.PositiveIntegerField(blank=True, null=True)
    years_in_business = models.PositiveIntegerField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    social_media_links = models.URLField(blank=True, null=True)
    business_size = models.CharField(max_length=100, choices=SIZE_CHOICES, default='small')
    bank_statements = models.FileField(upload_to='kyc_documents/', blank=True, null=True)
    

    def __str__(self):
            return self.business_name 

class loans(models.Model):
         CATEGORY_CHOICES = [
             ('agriculture', 'Agriculture'),
             ('vehicles', 'Vehicles'),
             ('property', 'Property'),
             ('equipment', 'Equipment'),
             ('office', 'Office Supplies'),
             ('other', 'Other'),
         ]

         category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
         lender = models.ForeignKey(User, on_delete=models.CASCADE)
         title = models.CharField(max_length=200)
         description = models.TextField()
         amount = models.DecimalField(max_digits=10, decimal_places=2)
         created_at = models.DateTimeField(auto_now_add=True)
     
         def __str__(self):
             return self.title
     