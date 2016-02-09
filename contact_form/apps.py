from django.apps import AppConfig as DjangoAppConfig
from django.utils.translation import ugettext_lazy as _
from contact_form.conf import settings
from django.dispatch import receiver
from django.core.mail import EmailMessage

class AppConfig(DjangoAppConfig):
    """Configuration for the contact_form app (only for Django v1.7+)"""
    label = name = 'contact_form'
    verbose_name = _('Contact Form')

    def ready(self):
        from . import signals