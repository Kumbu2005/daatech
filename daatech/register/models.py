from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile (models.Model):
    USER_TYPES = [
        ("SME", "SMEs"),
        ("Insurance", "Insurance Company"),
        ("Commercial", "Commercial Bank"),
        ("Microfinance", "Microfinance Institution")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, choices=USER_TYPES)

    def __str__(self):
        return self.user.username