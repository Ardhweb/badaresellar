
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from home.models import Contact,AddChannel
from home.forms import ContactForm
from django.contrib import messages #import messages

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


    
            
