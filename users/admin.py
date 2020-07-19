from django.contrib import admin
from .models import Profile, Budget, Saving, Spending

admin.site.register(Profile)
admin.site.register(Budget)
admin.site.register(Spending)
admin.site.register(Saving)
