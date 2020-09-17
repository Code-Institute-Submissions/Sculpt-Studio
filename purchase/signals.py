from django.db.models.signals import post_save, post_delete 
from django.dispatch import receiver

from .models import CheckoutLineItem


@receiver(post_save, sender=CheckoutLineItem)
def update_when_save(sender, instance, created, **kwargs):
    '''
    update order total when lineitem created/saved
    '''
    instance.purchase.update_total_cost()



@receiver(post_delete, sender=CheckoutLineItem)
def update_when_delete(sender, instance, **kwargs):
    '''
    update order total when lineitems deleted
    '''
    instance.purchase.update_total_cost()
