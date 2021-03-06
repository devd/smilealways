from django.shortcuts import render
from django.http import HttpResponse
from smilecounter.models import SmileRedirect
from datetime import datetime
from pytz import UTC
from django.utils import simplejson

def home(request):
    return render(request, 'smilecounter/index.html', {})

def faq(request):
    return render(request, 'smilecounter/faq.html', {})

def addRedirect(request):
    SmileRedirect.objects.create(time=UTC.localize(datetime.now()))
    response_data = {}
    return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
