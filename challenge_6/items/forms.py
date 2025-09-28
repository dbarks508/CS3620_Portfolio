from django import forms
from .models import Contact
from .models import PortfolioItem

class ContactForm(forms.Form):
    name = forms.CharField(required=True, label="Name: ", max_length=100)
    email = forms.CharField(required=True, label="Email: ", max_length=100)
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))
    
    def log_data(self):
        print(self.cleaned_data.get("name"))
        print(self.cleaned_data.get("email"))
        print(self.cleaned_data.get("message"))
        
class ContactModelForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ("name", "email", "message")
        
class PortfolioItemForm(forms.ModelForm):
    
    class Meta:
        model = PortfolioItem
        fields = ("name", "description", "img_path")
    