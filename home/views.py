
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from home.models import Reviews

# Create your views here.

from home.models import Contact,AddChannel,ImageList
from home.forms import ContactForm
from django.contrib import messages #import messages
from django.core.paginator import Paginator, EmptyPage,\
 PageNotAnInteger



def home_index(request):
    channels = AddChannel.objects.all()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Thank You For contact us.')
            # render(request,'home/index.html', {'contact_form':contact_form})
            #return HttpResponse('Success')
            return redirect('index')
        else:
            return HttpResponseRedirect(reverse('index', ))
    else:
        contact_form = ContactForm()
    return render(request,'home/index.html', {'contact_form':contact_form,'channels':channels})


    
def channel_list(request):
    ch_list = AddChannel.objects.all()  #Here published is Custom Model Manager Look to model file.
    paginator = Paginator(ch_list, 10) #show only 3 post each pages
    page_obj  = request.GET.get('page')
    ch_obj = paginator.get_page(page_obj)
    #return render(request, 'blog/post-listing.html', {'post_list':post_list})
    return render(request, 'home/channels/channel_listing.html', {'ch_obj': ch_obj,'page_obj':page_obj})


def channel_details(request, id=None):
    # detail = get_object_or_404(AddChannel, id)
    channel_detail = AddChannel.objects.get(id=id)
    imagelist =  ImageList.objects.filter(channel=id)
    return render(request,'home/channels/details.html',{'channel_detail':channel_detail,'imagelist':imagelist})
    


def sell_channel(request):
    return render(request,'home/channels/sell.html')