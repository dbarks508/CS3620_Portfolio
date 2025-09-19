from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("hobby/", views.hobby, name="hobby"),
    path("hobby/hobbyDetail/", views.hobbyDetail, name="hobbyDetail"),
    path("portfolioItem/", views.portfolioItem, name="portfolioItem"),
    path("portfolioItem/portfolioItemDetail", views.portfolioItemDetail, name="portfolioItem"),
    path("contact/<str:t>/", views.contact, name="contact"),
    path("contact/", views.contact, name="contact"),
]