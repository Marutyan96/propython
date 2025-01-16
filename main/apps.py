from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'main'

    def ready(self):
        import main.signals
        
class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"

