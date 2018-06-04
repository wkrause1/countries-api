from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import State
from django.http import HttpResponse, JsonResponse
from states.serializers import StateSerializer

@csrf_exempt
def state_list(request, country_code):

    if request.method == 'GET':
        print("Entering state GET requeset")
        states = State.objects.filter(country__country_code=country_code)
        serializer = StateSerializer(states, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        print("Entering state POST Request")
        data = JSONParser().parse(request)
        serializer = StateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def state_delete(state_text):
    print('Entering API Delete method')
    try:
        state = State.objects.get(state_text=state_text)
    except State.DoesNotExist:
        return HttpResponse(status=404)
    state.delete()
    return HttpResponse(status=204)



@csrf_exempt
def state_detail(request, state_code):
    try:
        state = State.objects.get(state_code=state_code)
    except State.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StateSerializer(state)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StateSerializer(state, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        state.delete()
        return HttpResponse(status=204)


