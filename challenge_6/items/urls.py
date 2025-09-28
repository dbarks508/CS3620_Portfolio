from django.urls import path
from items.views import ContactFormView, ContactListView, PortfolioListView, PortfolioDeleteView, PortfolioCreateView, PortfolioUpdateView
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
    path('contactForm/', ContactFormView.as_view(), name="contactForm"),
    path('contactForms/', ContactListView.as_view(), name="contactForms"),
    
    # path(url, view ot use, name of html)
    path('PortfolioList/', PortfolioListView.as_view(), name="PortfolioList"),
    path('portfolio/create/', PortfolioCreateView.as_view(), name="portfolioCreate"),
    path('Portfolio/<int:pk>/Delete/', PortfolioDeleteView.as_view(), name="portfolioDelete"),
    path('Portfolio/<int:pk>/update/', PortfolioUpdateView.as_view(), name="portfolioUpdate"),
    
]