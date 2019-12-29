from django.db.models.signals import post_save   #signals that gets fired after objesct is saved
from django.contrib.auth.models import User       # to get post saved signal and User model is sender
from django.dispatch import receiver
from .models import Profile
from django.shortcuts import redirect


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        return redirect('register')


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
