from django.db import models

# Create your models here.
class profile (models.Model):
    USER_TYPE = [
        ("","Select the one that best describes you"),
        ("SMEs", "SMEs"),
        ("Insurance-Company", "Insurance Company"),
        ("Commercial-Bank", "Commercial Bank"),
        ("Microfinance-Institution", "Microfinance Institution")
    ]

    