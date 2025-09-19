from django.http import HttpResponse
from django.shortcuts import render

from .models import Hobby
from .models import PortfolioItem

def home(request):
    return HttpResponse(" Hello and welcome to my portfolio site! My Name is Dylan Barks and I am from Ann Arbor, Michigan." +
                        " I moved to Utah about a year and a half ago and love rock climbing and running here." +
                        " I live with my fiance, Lexi, and out goofy Golden Doodle, Lola.")

def hobby(request):
    hobbyList = Hobby.objects.all()
    context = {"hobbyList": hobbyList}
    return render(request, "items/hobby.html", context)

def portfolioItem(request):
    portfolioItemList = PortfolioItem.objects.all()
    context = {"portfolioItemList": portfolioItemList}
    return render(request, "items/portfolioItem.html", context)

def contact(request, t=None):
    email = ""
    if t == "personal":
        email = "dylan.barks95@gmail.com"
    elif t == "school":
        email = "dylanbarks@mail.weber.edu"
    else:
        email = "dylan.barks95@gmail.com || dylanbarks@mail.weber.edu"

    context = {"email": email}
    return render(request, "items/contact.html", context)
