
from django.db import models

# Create your models here.
channel_categories = (('VlogandLifestyle', 'Vlog'),
('Education', 'Eduaction'),)
class AddChannel(models.Model):
    
    logo = models.FileField(upload_to='channels/',blank=False,)
    channel_name = models.CharField(max_length=30, blank=False,editable=True, default="")
    category = models.CharField(max_length=30, choices=channel_categories, default="")
    channel_link = models.URLField(editable=True, default="")
    total_subscriber = models.CharField(max_length=250, blank=False,editable=True, default="")
    watch_time = models.CharField(max_length=250, blank=False,editable=True, default="")
    adsense_approved = models.BooleanField(default=False, editable=True,)
    description = models.TextField(max_length=250, blank=False,editable=True, default="")
    channel_created_date = models.DateField(editable=True, help_text="Put Date When you Started this channel.", verbose_name='Youtube Joining Date', default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



class Contact(models.Model):
    name = models.CharField(max_length=20, blank=False)
    contact = models.CharField(max_length=10, blank=False)
    email = models.EmailField(blank=False)
    query = models.TextField(max_length=30)
    