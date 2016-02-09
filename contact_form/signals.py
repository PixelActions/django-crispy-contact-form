from django.dispatch import Signal
from contact_form.conf import settings
from django.dispatch import receiver
from django.core.mail import EmailMessage

contact_form_valid = Signal(
    providing_args=['event', 'ip', 'site', 'sender_name', 'sender_email', 'email', 'subject', 'message']
)

contact_form_invalid = Signal(
    providing_args=['event', 'ip', 'site', 'sender_name', 'sender_email']
)


@receiver(contact_form_valid)
def contact_form_send_email_on_valid(sender, event, ip, site, sender_name, sender_email, email, subject, message, **kwargs):
    if settings.CONTACT_FORM_SEND_EMAIL_ON_VALID:
        if settings.CONTACT_FORM_SEND_BCC_TO:
            bcc = [settings.CONTACT_FORM_SEND_BCC_TO,]
        else:
            bcc = []
        email = EmailMessage(subject="%s: %s" %(sender_name,subject), body=message,#from_email=django_settings.DEFAULT_FROM_EMAIL  we ommit cause it happens automaticlaly
        to=[email,], bcc=bcc , reply_to=[sender_email], headers={})
        email.send(fail_silently=False)

        

