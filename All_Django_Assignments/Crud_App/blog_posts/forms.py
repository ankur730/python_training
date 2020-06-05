from django import forms
from blog_posts.models import Contacts

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
