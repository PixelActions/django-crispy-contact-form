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
        if settings.CONTACT_FORM_SEND_EMAIL_ON_VALID:
            from .signals import contact_form_valid, contact_form_invalid
            
            @receiver(contact_form_valid)
            def contact_form_send_email_on_valid(sender, event, ip, site, sender_name, sender_email, email, subject, message, **kwargs):
                if settings.CONTACT_FORM_SEND_BBC_TO:
                    bcc = [settings.CONTACT_FORM_SEND_BBC_TO,]
                else:
                    bcc = []
                email = EmailMessage(subject="%s: %s" %(sender_name,subject), body=message,#from_email=django_settings.DEFAULT_FROM_EMAIL  we ommit cause it happens automaticlaly
                to=[email,], bcc=bcc , reply_to=[sender_email], headers={})
                email.send(fail_silently=False)

        

