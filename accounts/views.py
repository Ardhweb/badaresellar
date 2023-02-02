from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
# Create your views here.
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegisterForm, ProfileEditForm,UserEditForm\
    ,LoginForm
from accounts.models import CustomUser, Profile

from django.contrib.auth import login,logout, authenticate  # add to imports
from django.contrib import messages #import messages
from django.urls import reverse
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings


def register_signup(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid ():
            new_user = user_form.save(commit=False)
            new_user.set_password(
            user_form.cleaned_data['password'])
            new_user.save()
     
            Profile.objects.create(user=new_user)
            send_mass_mail(subject='Signup Updates',
                     message=f"Recently Someone has Signup at System Please Check is his details that he filled out \
                        \nEmail:{new_user.email} \n Name:{new_user.full_name} \n Contact No. :{new_user.country_code}-{new_user.contact_no}\n \
                        Thank You Please Report at Admin",
                     from_email=settings.EMAIL_HOST_USER,
                     recipient_list=[settings.RECIPIENT_ADDRESS])

        
            return redirect('login')
            #return render(request,'accounts/signup_done.html',{'new_user': new_user,})
        else:
              messages.error(request, 'The form is not valid Please Resubmit.')
              #return HttpResponseRedirect('')
    else:
        user_form = UserRegisterForm()
    return render(request,'accounts/signup.html',{'user_form': user_form, })
            



def login_user(request):
    laform = LoginForm()
    if request.method == "POST":
        laform = LoginForm(request.POST)
        if laform.is_valid():
            user = authenticate(request,
                username=laform.cleaned_data['username'],
                password=laform.cleaned_data['password'],)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request,
                    "f'You have been logged in'")
                    # return HttpResponse('Authenticated successfully')
                    #return render(request,'authenticate/login_done.html', {'user':user})
                    context ={'laform':laform}
                    # try:
                    #     return redirect('https://wa.me/7722882599?') # or return redirect('/') 
                    # except:
                    #     return HttpResponseRedirect('')
                    return redirect('index')
                    #return HttpResponseRedirect('')
                else:
                    return HttpResponse('Disabled account')
            # return redirect('')
            else:
                # message = 'Login failed!'
                messages.error(request, "Login failed!")
                # return HttpResponse('Invalid login')

        else:
            laform = LoginForm()
    return render(request, 'accounts/authenticate/login.html', {'laform':laform})




#Edit -Profile
@login_required
def edit_user_profile(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user,
                                data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated '\
                                    'successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'accounts/authenticate/edit.html',
                {'user_form': user_form,
                'profile_form': profile_form})




def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")


