from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from programs.models import Programs
from user_profile.models import Profile
from django.contrib.auth.models import User
from django.utils import timezone



class Testimonials(models.Model):

    class Meta():
        verbose_name_plural = 'Testimonials'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    program_id = models.OneToOneField(Programs, on_delete=models.CASCADE, null=True)
    review = models.TextField(max_length=2064)
    score = models.PositiveIntegerField(default=0, choices=([i,i] for i in range(11)))
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username
