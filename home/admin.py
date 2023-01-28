from django.contrib import admin

# Register your models here.
from home.models import AddChannel,Contact


@admin.register(AddChannel)
class AddChannelAdmin(admin.ModelAdmin):
    list_display = ['channel_name',]




@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']