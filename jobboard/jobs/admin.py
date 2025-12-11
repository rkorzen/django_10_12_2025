from django.contrib import admin
from .models import Offer, RecruiterProfile, Company


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    filter_horizontal = ["tags", ]
    list_display = ["title", "company", "is_published"]
    search_fields = ["title", "description"]
    list_filter = ["is_published", "company"]



@admin.register(RecruiterProfile)
class RecruiterProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "phone_number", "email"]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "website", "size"]