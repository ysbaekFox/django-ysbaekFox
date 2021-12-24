from django.shortcuts import render

# Create your views here.
import logging
from django.http import HttpResponse

logger = logging.getLogger('django')

def index(request):
    logger.error("test")
    return HttpResponse("Hello, world. You're at the polls index.")