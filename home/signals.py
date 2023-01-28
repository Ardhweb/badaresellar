

from home.models import AddChannel
from django.dispatch import receiver
# from django.core.signals import pre_delete
from django.db.models.signals import post_save,pre_delete, pre_init, pre_save
from django.core.signals import request_finished
import os

@receiver(pre_delete, sender=AddChannel)
def delete_channel(sender,instance,**kwargs):
    instance.logo.delete(False)
    # channel = AddChannel.objects.get(id=id)
    # if len(channel.logo) > 0:
    #     os.remove(channel.logo.path)
 



@receiver(post_save, sender=AddChannel)
def update_channel(sender,instance,**kwargs):
    location = instance.logo
    print(f'FileName:{location}')
    # c_location = instance.logo
    # c_location.delete(False)
    # channel = AddChannel.objects.all( )
    # loc = channel.logo
    # print(f'{loc}')
    # channel.save(update_fields=['logo'])
    