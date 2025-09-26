from django.contrib import admin

from .models import Hobby
from .models import PortfolioItem

admin.site.register(Hobby)
admin.site.register(PortfolioItem)
