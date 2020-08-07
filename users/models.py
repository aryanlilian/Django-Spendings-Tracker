from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class Budget(models.Model):
    CURRENCY = (
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('RON', 'RON'),
        ('MDL', 'MDL')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    currency = models.CharField(
        max_length=100, choices=CURRENCY, default='USD')

    def __str__(self):
        return f'{self.user.username} Budget'


class Spending(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    amount = models.FloatField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
