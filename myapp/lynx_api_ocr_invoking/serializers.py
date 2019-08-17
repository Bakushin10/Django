from rest_framework import serializers
from lynx_api_ocr_invoking.models import OCRInputModel, JsonOCRInputModel

class OCRInputModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OCRInputModel
        fields = ('ocrJson',)

class JsonOCRInputModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JsonOCRInputModel
        fields = ('field', 'hasField', 'coordinates', 'x_coordinates', 'y_coordinates', 'text',)