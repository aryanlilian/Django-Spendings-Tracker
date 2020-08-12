from django.contrib import admin
from .models import Profile, Budget, Spending, Note, Task

admin.site.register(Profile)
admin.site.register(Budget)
admin.site.register(Spending)
admin.site.register(Note)
admin.site.register(Task)
