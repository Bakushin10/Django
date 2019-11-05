from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from ocr_api.views import post_dummy_data, get_dummy_data, post_ocr_results, get_ocr_results, get_ocred_image, get_ocr_results_by_id
#from poll.urls import router as polls_router
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API Lists')

urlpatterns = [
    path('swagger/', schema_view),
    path('admin/', admin.site.urls),
    path('poll/<slug:location>/', include('poll.urls')),
    path('weather/<slug:location>/', include('weather.urls')),
    path('dummydata/new/', post_dummy_data, name = "post_dummy_data"),
    path('dummydata/', get_dummy_data, name = "get_dummy_data"),
    path('ocr_results/new', post_ocr_results, name = "post_ocr_results"),
    path('ocr_results/<int:username>/', get_ocr_results_by_id, name = "get_ocr_results_by_id"),
    path('ocr_results/', get_ocr_results, name = "get_ocr_results"),
    path('ocr_image/', get_ocred_image, name = "get_ocred_image"),
    url(r'index2/', TemplateView.as_view(template_name="index2.html"), name="home"),
    #url(r'^api/', include(polls_router.urls))
    
    # default template
    #path('.*', TemplateView.as_view(template_name="index.html"), name="home")
]