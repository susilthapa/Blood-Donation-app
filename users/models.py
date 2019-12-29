from django.db import models
from django.contrib.auth.models import User

#
BLOOD_GROUP_CHOICES = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    blood_group = models.CharField(choices=BLOOD_GROUP_CHOICES, max_length=3, null=False, blank=False)
    age = models.CharField(max_length=100, null=True, default=None)
    phone_number = models.CharField(max_length=12, null=True, default=None)
    # email = models.EmailField()
    latitude = models.FloatField(null=True, default=None)
    longitude = models.FloatField(null=True, default=None)
    terms_and_conditions = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
