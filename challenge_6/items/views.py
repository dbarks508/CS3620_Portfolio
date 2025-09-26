from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView

from .models import Hobby
from .models import PortfolioItem
from items.forms import ContactForm

apis = [
    {"name": "View Home", "path": "/home"},
    {"name": "View Hobbies", "path": "/hobby"},
    {"name": "View Portfolio Items", "path": "/portfolioItem"},
    {"name": "View Contact Information", "path": "/contact"},
]

def home(request):
    return render(request, "items/home.html", {"apis": apis})

def hobby(request):
    hobbyList = Hobby.objects.all()
    context = {"hobbyList": hobbyList, "apis": apis}
    return render(request, "items/hobby.html", context)

def hobbyDetail(request):
    hobbyList = Hobby.objects.all()
    context = {"hobbyList": hobbyList, "apis": apis}
    return render(request, "items/hobbyDetail.html", context)

def portfolioItem(request):
    portfolioItemList = PortfolioItem.objects.all()
    context = {"portfolioItemList": portfolioItemList, "apis": apis}
    return render(request, "items/portfolioItem.html", context)

def portfolioItemDetail(request):
    portfolioItemList = PortfolioItem.objects.all()
    context = {"portfolioItemList": portfolioItemList, "apis": apis}
    return render(request, "items/portfolioItemDetail.html", context)

def contact(request, t=None):
    email = ""
    if t == "personal":
        email = "dylan.barks95@gmail.com"
    elif t == "school":
        email = "dylanbarks@mail.weber.edu"
    else:
        email = "dylan.barks95@gmail.com *** dylanbarks@mail.weber.edu"

    context = {"email": email, "apis": apis}
    return render(request, "items/contact.html", context)

class ContactFormView(FormView):
    template_name = "contactForm.html"
    form_class = ContactForm
    seccess_url = "contactForm"
    
    def form_valid(self, form):
        form.log_data()
        return super().form_valid(form)
