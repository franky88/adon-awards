from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from awards.models import Awardee, AwardTitle, CertBG
# Create your views here.
