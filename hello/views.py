import requests

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import Greeting

from django.views.decorators.csrf import csrf_exempt

import requests
import time
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


from Processor.machine import machine

# Create your views here.
@csrf_exempt

@csrf_exempt
def requ(request):
    print (request.user, " is adding an article")
    if request.method == "POST":
        web_url = request.POST.get('web_url', False)
        r = machine(web_url)
        return JsonResponse({'response': r})


def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
