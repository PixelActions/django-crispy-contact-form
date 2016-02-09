from django.dispatch import Signal
from django.dispatch import receiver
from contact_form.conf import settings
from django.core.mail import EmailMessage

contact_form_valid = Signal(
    providing_args=['event', 'ip', 'site', 'sender_name', 'sender_email', 'email', 'subject', 'message']
)

contact_form_invalid = Signal(
    providing_args=['event', 'ip', 'site', 'sender_name', 'sender_email']
)