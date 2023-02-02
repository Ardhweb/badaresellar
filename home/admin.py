from django.contrib import admin

# Register your models here.
from home.models import AddChannel,ImageList,Contact,Reviews
from sorl.thumbnail.admin import AdminImageMixin



class ImageListInline(admin.TabularInline):
    model = ImageList
    raw_id__fields = ['channel']

@admin.register(AddChannel)
class AddChannelAdmin(admin.ModelAdmin):
    list_display = ['channel_name',]
    inlines = [ImageListInline]
    search_fields = ("channel_name__startswith","id__startswith" )




@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ("name__startswith", )

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin,AdminImageMixin):
    list_display = ['id','name','thumbnail_preview']
    search_fields = ("name__startswith", )
    #readonly_fields = ('thumbnail_preview',)
    
    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Image Preview'
    thumbnail_preview.allow_tags = True