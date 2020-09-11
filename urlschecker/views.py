from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
import requests, json
from .models import URL


@login_required
def home(request):
    context = {
        "urls": URL.objects.all()
    }
    return render(request, 'home.html', context)


def update_urls_status(request):
    urls = URL.objects.all()
    for url in urls:
        try:
            u = str(url.url)
            if u.startswith("https") == False and u.startswith("http") == False:
                u = "https://" + u
            elif u.startswith("http") == True:
                u = u.replace("http", "https")
            res = requests.get(u)
            url.status_code = res.status_code
        except:
            url.status_code = 404
        url.save()
    return JsonResponse({'success': 1})


def load_urls(request):
    urls = URL.objects.all().values()
    urls = list(urls)
    return JsonResponse(urls, safe=False)
