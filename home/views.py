from django.http import JsonResponse, HttpResponse
from home.models import MotionEvent


# Create your views here.

def index(request):
    """The home page for Learning Log"""
    return HttpResponse("Let's start with this")
    # return render(request, 'learning_logs/index.html')


def get_uploaded_images(request):
    events = MotionEvent.objects.all().order_by('-timestamp')
    image_urls = ["http://192.168.228.220:8000" + event.image.url for event in events]
    return JsonResponse({'images': image_urls})


def get_uploaded_videos(request):
    events = MotionEvent.objects.all().order_by('-timestamp')
    video_urls = ["http://192.168.228.220:8000" + event.video.url for event in events]
    return JsonResponse({'videos': video_urls})


def get_uploaded_files(request):
    events = MotionEvent.objects.all().order_by('-timestamp')
    image_urls = ["http://192.168.228.220:8000" + event.image.url for event in events]
    video_urls = ["http://192.168.228.220:8000" + event.video.url for event in events]
    return JsonResponse({'images': image_urls, 'videos': video_urls})
