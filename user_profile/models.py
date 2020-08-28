from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from programs.models import Programs
from django.core.validators import MaxValueValidator, MinValueValidator 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=264, blank=True)
    country = CountryField(blank=True)
    height  = models.IntegerField(default=0, blank=True)
    weight  = models.IntegerField(default=0, blank=True)
    goal = models.TextField(max_length=1024, blank=True)

    def __str__(self):
        return self.user.username

    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


class Testimonials(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    program = models.ForeignKey(Programs, on_delete=models.CASCADE)
    review = models.TextField(max_length=2064)
    score = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])
    date = models.DateField()