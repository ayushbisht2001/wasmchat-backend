from django.shortcuts import render
from .models import person_collection
from django.http import  HttpResponse, JsonResponse
# from django.core.serializers import serialize
from bson.json_util import dumps
import json
# Create your views here.


def index(request):
    return HttpResponse("<h1>App is running</h1>")

def add_person(request):
    records = {
        "first_name":"john",
        "last_name": "smith"
    }
    person_collection.insert_one(records)
    return HttpResponse("new person is added")


def get_all_person(request):
    persons = list(person_collection.find())
    data = dumps(persons)
    return HttpResponse(data,content_type = "application/json")

