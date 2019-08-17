from django.db import models

# Create your models here.
class OrchestratorInputModel(models.Model):
    agentCode = models.CharField(max_length=15)
    companyCode = models.CharField(max_length=2)
    imageSourceType = models.CharField(max_length=1)


class OCRInputModel(models.Model):
    ocrJson = models.CharField(max_length = 3000)
