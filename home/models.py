

from distutils.command.upload import upload
from django.db import models
from django.urls import reverse
# Create your models here.

from django.utils.html import mark_safe

from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
   
   


channel_categories = (
('VlogandLifestyle', 'Vlog'),
('Education', 'Eduaction'),
('Autos & Vehicles','Autos & Vehicles'),
('Comedy','Comedy'),
('Education','Education'),
('Entertainment','Entertainment'),
('Film & Animation','Film & Animation'),
('Gaming','Gaming'),
('Howto & Style','Howto & Style'),
('Music','Music'),
('News & Politics','News & Politics'),
('Nonprofits & Activism','Nonprofits & Activism'),
('People & Blogs','People & Blogs'),
('Pets & Animals','Pets & Animals'),
('Science & Technology','Science & Technology'),
('Sports','Sports'),
('Travel & Events','Travel & Events'),
)

AUDIENCE_GROUP =(
    ('13-17','13-17'),
    ('18-24', '18-24'),
    ('25-34','25-34'),
    ('35-44', '35-44'),
    ('45-54', '45-54'),
    ('55-64', '55-64'),
)

Monetization =(
    ('Monetizated', 'Monetizated'),
    ('Non-monetized','Non-monetized'),
    ('Demontized','Demontized'),
)
class AddChannel(models.Model):
    listing_id = models.CharField(max_length=1000,blank=False)
    thumbnail_imge = models.FileField(upload_to='channels/',blank=True, help_text="Put Here Main Image File or Just Logo.")
    channel_name = models.CharField(max_length=30, blank=False,editable=True,)
    category = models.CharField(max_length=30, choices=channel_categories, )
    channel_type = models.CharField(max_length=250)
    content_type = models.CharField(max_length=300, editable=True, blank=True,)
    audience_age = models.CharField(max_length=250, choices=AUDIENCE_GROUP,)
    language = models.CharField(max_length=250,)
    channel_link = models.URLField(editable=True, )
    channel_created_date = models.DateField(editable=True, help_text="Put Date When you Started this channel.", verbose_name='Youtube Joining Date', )
    current_subscriber = models.CharField(max_length=250, blank=False,editable=True,)
    total_views = models.CharField(max_length=250, blank=False,editable=True, )
    last_views = models.CharField(help_text ="Last 28Days Views",max_length=250, blank=False,editable=True, )
    real_time_views = models.CharField(max_length=250, editable=True, blank=True,)
    active_copyright_strike	 = models.CharField(max_length=300, editable=True, blank=True,)
    active_community_guidelines_strike = models.CharField(max_length=300, editable=True, blank=True,)
    monetization_status = models.CharField(max_length=250, choices=Monetization, blank=False,)
    watch_time = models.CharField(max_length=250, editable=True, blank=True)
    total_revenue = models.CharField(max_length=250, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=250, default="UPI/Bank Transfer/Cash/Paypal")
    out_stock = models.BooleanField(default=False)
    for_sale = models.BooleanField(default=True)
    price = models.CharField(max_length=250, blank=False)
    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.channel_name
    
    def get_absolute_url(self,):
       return reverse('channel-detail',args=[self.id])



class ImageList(models.Model):
    channel = models.ForeignKey(AddChannel, on_delete=models.CASCADE,null=False)
    image = models.ImageField(upload_to='channels/imglist/',blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=20, blank=False)
    contact = models.CharField(max_length=10, blank=False)
    email = models.EmailField(blank=False)
    query = models.TextField(max_length=30)


class Reviews(models.Model):
    name=models.CharField(max_length=25,blank=True ,help_text="Put Name here or Leave Blank")
    image = models.ImageField(upload_to='channels/reviews/', blank=True)
    query = models.TextField(max_length=250, blank=True,help_text="Max words 250 or leave blank")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name
    
    @property
    def thumbnail_preview(self):
        if self.image:
            _image = get_thumbnail(self.image,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_image.url, _image.width, _image.height))
        return ""