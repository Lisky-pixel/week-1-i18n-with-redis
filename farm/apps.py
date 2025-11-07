from django.apps import AppConfig


class FarmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'farm'

    def ready(self):
        # import signals to register them
        try:
            import farm.signals  # noqa: F401
        except Exception:
            # avoid failing imports during manage.py commands before migrations
            pass
