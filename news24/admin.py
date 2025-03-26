from django.contrib import admin
from .models import Category, News, Sponsor, Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'view')
    search_fields = ('name', 'email')
    list_filter = ('view',)
    ordering = ['view', '-date']

admin.site.register(Category)
admin.site.register(News)
admin.site.register(Sponsor)
admin.site.register(Contact, ContactAdmin)