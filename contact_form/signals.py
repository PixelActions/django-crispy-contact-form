from django.dispatch import Signal
from django.dispatch import receiver
from contact_form.conf import settings
from django.settings import settings as django_settings
from django.core.mail import EmailMessage

contact_form_valid = Signal(
    providing_args=['event', 'ip', 'site', 'sender_name', 'sender_email', 'email', 'subject', 'message']
)

contact_form_invalid = Signal(
    providing_args=['event', 'ip', 'site', 'sender_name', 'sender_email']
)

if settings.CONTACT_FORM_SEND_EMAIL_ON_VALID:
    @receiver(contact_form_valid)
    def contact_form_send_email_on_valid(sender, event, ip, site, sender_name, sender_email, email, subject, message, **kwargs):
        if settings.SEND_BBC_TO:
            bcc = [settings.SEND_BBC_TO,]
        if settings.SEND_EMAIL_TO:
            email = EmailMessage(subject="%s: %s" %(sender_name,subject), body=message,#from_email=django_settings.DEFAULT_FROM_EMAIL  we ommit cause it happens automaticlaly
            to=[email,], bcc=bcc , reply_to=[sender_email], headers={})
            email.send(fail_silently=False)
