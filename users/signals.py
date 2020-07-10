from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Buget, Saving


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def create_buget(sender, instance, created, **kwargs):
    if created:
        Buget.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_buget(sender, instance, **kwargs):
    instance.buget.save()


@receiver(post_save, sender=User)
def create_saving(sender, instance, created, **kwargs):
    if created:
        Saving.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_saving(sender, instance, **kwargs):
    instance.saving.save()
