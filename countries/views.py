from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Country
from django.http import HttpResponse, JsonResponse
from countries.serializers import CountrySerializer

@csrf_exempt
def country_list(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CountrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def country_detail(request, country_code):
    try:
        country = Country.objects.get(country_code=country_code)
    except Country.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CountrySerializer(country)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CountrySerializer(country, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        country.delete()
        return HttpResponse(status=204)


