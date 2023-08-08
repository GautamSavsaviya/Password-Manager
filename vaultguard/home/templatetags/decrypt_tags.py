from django import template
from home.utils import decrypt

register = template.Library()


@register.filter
def decrypt_password(password):
    return decrypt(password)
