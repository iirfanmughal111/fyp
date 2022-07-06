"""vdas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import imp
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include

# from . import views
 
# For Media managing
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/',include('django.contrib.auth.urls')),
    path('member/',include('member.urls')),
    path('',include('main.urls')),

    # path('',views.index,name='home'),
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


admin.site.index_title = 'Vehcile Data Acquisition System'
admin.site.site_header = 'FYP Adminisntration '
admin.site.site_title = 'F Y P'




