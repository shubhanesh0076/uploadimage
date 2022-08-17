from venv import create
from django.db import models

# Create your models here.

class UploadImage(models.Model):
    """UPLOAD IMAGE MODEL."""
    
    image = models.ImageField(upload_to="images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    