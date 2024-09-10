from django.urls import path
from . import views
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('uploaded-images/', views.get_uploaded_images, name='get_uploaded_images'),
    path('uploaded-videos/', views.get_uploaded_videos, name='get_uploaded_videos'),
    path('uploaded-files/', views.get_uploaded_files, name='get_uploaded_videos'),
]
