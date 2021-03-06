from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}\'s Profile'


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    amount = models.FloatField()
    recurrent = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username}\'s Budget'


class Currency(models.Model):

    CURRENCY = (
        ('AED', 'AED'),
        ('AUD', 'AUD'),
        ('BRL', 'BRL'),
        ('CAD', 'CAD'),
        ('CHF', 'CHF'),
        ('CLP', 'CLP'),
        ('CNY', 'CNY'),
        ('COP', 'COP'),
        ('CZK', 'CZK'),
        ('DKK', 'DKK'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
        ('HKD', 'HKD'),
        ('HUF', 'HUF'),
        ('IDR', 'IDR'),
        ('ILS', 'ILS'),
        ('INR', 'INR'),
        ('JPY', 'JPY'),
        ('KRW', 'KRW'),
        ('MDL', 'MDL'),
        ('MXN', 'MXN'),
        ('MYR', 'MYR'),
        ('NOK', 'NOK'),
        ('NZD', 'NZD'),
        ('PHP', 'PHP'),
        ('PLN', 'PLN'),
        ('RON', 'RON'),
        ('RUB', 'RUB'),
        ('SAR', 'SAR'),
        ('SEK', 'SEK'),
        ('SGD', 'SGD'),
        ('THB', 'THB'),
        ('TRY', 'TRY'),
        ('TWD', 'TWD'),
        ('USD', 'USD'),
        ('ZAR', 'ZAR'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=4, choices=CURRENCY, default='USD')

    def __str__(self):
        return f'{self.user.username}\'s Currency'


class Spending(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    amount = models.FloatField()
    recurrent = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username}\'s {self.name}'


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    category = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}\'s {self.title}'


class Task(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
