from tokenize import maybe
from turtle import home
from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
    
    def ready(self, **kwargs):
        # AddChannel = self.get_model('AddChannel')
        # import badaresellar.home.signals
        # pre_delete.connect(my_callback, sender=AddChannel)
        import home.signals

