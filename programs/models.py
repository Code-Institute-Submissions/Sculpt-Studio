from django.db import models

# Create your models here.

class Programs(models.Model):
    """
    model for different programs on sale
    """

    class Meta: 
        verbose_name_plural = 'Programs'

    name = models.CharField(max_length=100)
    type = models.DecimalField(max_digits=2, decimal_places=0)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name 