from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset
from django import forms

from jobs.models import Registration


class ContactForm(forms.Form):
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)


    def clean_email(self):
        return self.cleaned_data["email"].lower()


# class RegistrationForm(forms.Form):
#     message = forms.CharField(widget=forms.Textarea, required=False)
#     email = forms.EmailField()

class OfferRegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = ['message', 'email']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Twoja wiadomosc',
                "message"
            ),
            Fieldset(
                'Dane kontaktowe',
                "email"
            ),
            Submit('submit', 'Submit', css_class='button white'),
        )