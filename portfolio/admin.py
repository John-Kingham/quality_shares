from django.contrib import admin
from .models import Portfolio
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Portfolio)
class PortfolioAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)
