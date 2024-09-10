from django.db import models


# Create your models here.
class MotionEvent(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='motion_images')
    video = models.FileField(upload_to='motion_videos')
