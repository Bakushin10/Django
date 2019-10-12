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
from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from ocr_api.views import post_dummy_data, get_dummy_data, post_ocr_results, get_ocr_results, get_ocred_image, get_ocr_results_by_id
from weather.views import get_weather_API
from poll.urls import router as polls_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dummydata/new/', post_dummy_data, name = "post_dummy_data"),
    path('dummydata/', get_dummy_data, name = "get_dummy_data"),
    path('ocr_results/new', post_ocr_results, name = "post_ocr_results"),
    path('ocr_results/<int:username>/', get_ocr_results_by_id, name = "get_ocr_results_by_id"),
    path('ocr_results/', get_ocr_results, name = "get_ocr_results"),
    path('ocr_image/', get_ocred_image, name = "get_ocred_image"),
    path('weatherapi/', get_weather_API, name = "get_weather_API"),
    url(r'index2/', TemplateView.as_view(template_name="index2.html"), name="home"),
    url(r'^api/', include(polls_router.urls))
    
    # default template
    #path('.*', TemplateView.as_view(template_name="index.html"), name="home")
]