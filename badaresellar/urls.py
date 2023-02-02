"""badaresellar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings #Import Settings Configure
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('home.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/', include('blog.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler404 = "badaresellar.views.page_not_found_404"
# handler410 = "badaresellar.views.gone_notexits_410"
# handler500 = "badaresellar.views.internal_eror_500"
# handler503 = "badaresellar.views.service_unavailable_503"


#Admin-Panel  Change Customize Txt Header Start Here
admin.site.site_header = " BadaResellar Admin"
admin.site.site_title = "BadaResellar  Admin Portal"
admin.site.index_title = "Welcome to BadaResellar DashBoard"
