"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView
from ocr_api.views import post_dummy_data, get_dummy_data, post_ocr_results, get_ocr_results, get_ocred_image
from weather.views import get_weather_API

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dummydata/new/', post_dummy_data),
    url(r'^dummydata/', get_dummy_data),
    url(r'^ocr_results/new', post_ocr_results),
    url(r'^ocr_results/', get_ocr_results),
    url(r'^ocr_image/', get_ocred_image),
    url(r'^weatherapi/', get_weather_API),
    url(r'index2/', TemplateView.as_view(template_name="index2.html"), name="home"),
    
    # default template
    #url(r'^.*', TemplateView.as_view(template_name="index.html"), name="home")
]