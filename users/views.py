from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.http import JsonResponse

# Create your views here.
class CustomLoginView(LoginView):
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    def form_valid(self, form):
        response = super().form_valid(form)
        return JsonResponse({'success': True})