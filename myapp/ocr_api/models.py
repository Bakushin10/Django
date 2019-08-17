from django.db import models

# Create your models here.
class OCRInputModel(models.Model):
    ocrJson = models.CharField(max_length = 3000)


class JsonOCRInputModel(models.Model):
    """
    sample data
    
    "field": 2, 
    "hasField": "True", 
    "coordinates": [{"y": 23, "x": 93}, {"y": 23, "x": 110}, {"y": 33, "x": 110}, {"y": 33, "x": 93}], 
    "text": "\u8a3c\u5238"
    """
    field = models.CharField(blank = False, null = False, max_length = 5)
    hasField = models.BooleanField(default = False)
    coordinates = models.TextField(blank = False, null = False, max_length = 1000)
    x_coordinates = models.TextField(blank = False, null = False, default = "", max_length = 20)
    y_coordinates = models.TextField(blank = False, null = False, default = "", max_length = 20)
    text = models.CharField(blank = False, null = False, max_length = 50)