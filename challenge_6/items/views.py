from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from .models import Hobby
from .models import PortfolioItem
from .forms import PortfolioItemForm
from items.forms import ContactForm, ContactModelForm
from items.models import Contact
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin


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

# from tutorial
class ContactFormView(FormView):
    template_name = "items/contactForm.html"
    form_class = ContactModelForm
    success_url = "/contact/"
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# from tutorial
class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    context_object_name = "contact_data"
    
    def render_to_response(self, context, **responce_kwargs):
        back = '<a href="/contact/">Back</a>'
        contacts = ""
        for contact in context["contact_data"]:
            contacts += f'<li>{contact.name} || {contact.email} || {contact.message}</li>'
        return HttpResponse(f'<html><body><ul>{contacts}</ul>{back}</body></html>')
    
# create new pi view class
class PortfolioCreateView(LoginRequiredMixin, CreateView):
    model = PortfolioItem
    template_name = "items/portfolioCreate.html"
    form_class = PortfolioItemForm
    success_url = "/portfolioItem/"

# update existing pi view class
class PortfolioUpdateView(LoginRequiredMixin, UpdateView):
    model = PortfolioItem
    template_name = "items/portfolioUpdate.html"
    form_class = PortfolioItemForm
    success_url = "/portfolioItem/"

# delete existing pi view class
class PortfolioDeleteView(LoginRequiredMixin, DeleteView):
    model = PortfolioItem
    template_name = "items/portfolioDelete.html"
    success_url = "/portfolioItem/"
    