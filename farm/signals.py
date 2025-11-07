from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Produce


def invalidate_produce_list_cache():
    # This matches the key used in the template: make_template_fragment_key('produce_list_fragment', [language_code])
    # We don't know the language codes present, so attempt the common ones from settings
    from django.conf import settings

    for lang_code, _ in getattr(settings, 'LANGUAGES', [('en', 'English')]):
        key = make_template_fragment_key('produce_list_fragment', [lang_code])
        cache.delete(key)


@receiver(post_save, sender=Produce)
def produce_saved(sender, instance, **kwargs):
    invalidate_produce_list_cache()


@receiver(post_delete, sender=Produce)
def produce_deleted(sender, instance, **kwargs):
    invalidate_produce_list_cache()
