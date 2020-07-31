from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['restaurant_name', 'email_address', 'facebook_page', 'is_subscriber', ]
    search_fields = ['restaurant_name', ]
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)