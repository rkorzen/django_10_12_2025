from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)


    def clean_email(self):
        return self.cleaned_data["email"].lower()