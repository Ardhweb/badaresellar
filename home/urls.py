from django.urls import path

from home.views import home_index, channel_details, channel_list,sell_channel

from home import views



urlpatterns = [
    path('', views.home_index, name="index"),
    path('channel-detail/<int:id>/',views.channel_details, name='channel-detail'),
    path('channel/list/', views.channel_list, name="channel-list"),
    path('channel-sell/', views.sell_channel, name='sell-channel'),

    
]
