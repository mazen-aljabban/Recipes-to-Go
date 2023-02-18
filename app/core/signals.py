from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Chef

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_chef_for_new_user(sender, **kwargs):
    if kwargs['created']:
        Chef.objects.create(user=kwargs['instance'])