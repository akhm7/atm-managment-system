from django.apps import AppConfig


class CrudappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crudapp'
    verbose_name = 'General'


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # add this
    def ready(self):
        import users.signals  # noqa