from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import random
import string
from .models import URL

def create_short_url(request):
    if request.method == 'POST':
        url = request.POST.get('url', '')
        custom_name = request.POST.get('custom_name', '')
        if not url:
            return JsonResponse({'error': 'Please provide a URL'})
        validate = URLValidator()
        try:
            validate(url)
        except ValidationError:
            return JsonResponse({'error': 'Please provide a valid URL'})
        if len(url) > 250:
            return JsonResponse({'error': 'URL must be below 250 characters'})
        if custom_name:
            if len(custom_name) > 10:
                return JsonResponse({'error': 'Custom name must be below 10 characters'})
            if URL.objects.filter(custom_name=custom_name).exists():
                return JsonResponse({'error': 'Custom name already taken'})
            short_url = custom_name
        else:
            short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            while URL.objects.filter(short_url=short_url).exists():
                short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        url_obj = URL(url=url, short_url=short_url, custom_name=custom_name)
        url_obj.save()
        return JsonResponse({'short_url': short_url})

def redirect_short_url(request, short_url):
    url_obj = URL.objects.filter(short_url=short_url).first()
    if url_obj:
        url_obj.counter += 1
        url_obj.save()
        return redirect(url_obj.url)
    else:
        return JsonResponse({'error': 'Short URL not found'})

