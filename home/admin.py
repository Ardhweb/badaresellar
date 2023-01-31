from django.contrib import admin

# Register your models here.
from home.models import AddChannel,ImageList,Contact,Reviews




class ImageListInline(admin.TabularInline):
    model = ImageList
    raw_id__fields = ['channel']

@admin.register(AddChannel)
class AddChannelAdmin(admin.ModelAdmin):
    list_display = ['channel_name',]
    inlines = [ImageListInline]




@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['id','name']