from django.contrib import admin
from .models import OCRInputModel, JsonOCRInputModel

# Register your models here.
admin.site.register(OCRInputModel)
admin.site.register(JsonOCRInputModel)