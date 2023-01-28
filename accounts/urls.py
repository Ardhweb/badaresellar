from django.urls import path 

from accounts.views import register_signup, login_user, logout_user, edit_user_profile
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('signup/', views.register_signup, name="signup"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('profileedit/', views.edit_user_profile, name='profile-edit'),



    #  # change password urls
    # path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    # path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # #reset password
    # path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    # path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),


    
     # change password urls
    path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #reset password
    path('password_reset/',auth_views.PasswordResetView.as_view(
    template_name="accounts/registration/password_reset_form.html"
    ),name='password_reset'),

    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/registration/password_reset_done.html"
    ),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
        template_name="accounts/registration/password_reset_confirm.html"
    ),name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name="accounts/registration/password_reset_complete.html"
    ),name='password_reset_complete'),
]
