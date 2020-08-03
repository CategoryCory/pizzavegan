from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('restaurant_name', 'email_address', 'vegan_pizza_type', 'menu_description', 'facebook_page',
                  'pizza_photo', 'is_subscriber')
        labels = {
            'restaurant_name': _('What is the name of your restaurant?'),
            'email_address': _('What is your email address?'),
            'vegan_pizza_type': _('Which vegan pizza would you like to feature in this promotion?'),
            'menu_description': _('Please provide a description of your pizza.'),
            'facebook_page': _('What is the link to your pizzeria\'s Facebook page?'),
            'pizza_photo': _('Please upload a photo of the pizza you would like to feature.'),
            'is_subscriber': _('Are you a PMQ subscriber?'),
        }
        help_texts = {
            'is_subscriber': _('Please check if you are a current subscriber to PMQ Pizza Magazine.'),
            'pizza_photo': _('Maximum file size: 5MB'),
        }
