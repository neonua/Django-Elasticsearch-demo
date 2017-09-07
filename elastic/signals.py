from .models import Document
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Document)
def index_post(sender, instance, **kwargs):
    # indexing new or changed data
    instance.indexing()
