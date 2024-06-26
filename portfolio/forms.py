from django.forms import ModelForm, TextInput
from portfolio.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        fields = {
            'phone_number': TextInput(
                attrs={
                    'placeholder': 'Phone number must be entered in the format: +123456789. Up to 15 figits'
        }
            )
        }