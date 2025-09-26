from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(required=True, label="Name: ", max_length=100)
    email = forms.CharField(required=True, label="Email: ", max_length=100)
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))
    
    def log_data(self):
        print(self.cleaned_data.get("name"))
        print(self.cleaned_data.get("email"))
        print(self.cleaned_data.get("message"))
    