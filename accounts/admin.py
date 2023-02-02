from django.contrib import admin

# Register your models here.
from accounts.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name']
    readonly_fields = ('password',)
    search_fields = ("email__startswith","full_name__startswith","first_name__startswith", )

    def get_form(self, request, obj=None, **kwargs):
        help_texts = {'password': 'Password Were Are  Hide by Hashing'}
        kwargs.update({'help_texts': help_texts})
        return super(CustomUserAdmin, self).get_form(request, obj, **kwargs)
    
    @admin.display(empty_value='???')
    def full_name(self, obj):
        return obj.full_name