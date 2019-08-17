from rest_framework import serializers
from lynx_ui.models import OrchestratorInputModel, OCRInputModel

class OrchestratorInputModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrchestratorInputModel
        fields = ('agentCode', 'companyCode', 'imageSourceType')


class OCRInputModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OCRInputModel
        fields = ('ocrJson',)