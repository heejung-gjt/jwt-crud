from django.http.response import JsonResponse
from django.shortcuts import render
from user.models import User
# from .models import *
import json

# Create your views here.
def index(request):
    if request.is_ajax:
        user_id = request.GET.get('param')
        print('ddddddddddddd', user_id)
        if user_id:
            user = User.objects.get(pk=user_id)
            context = {
                "id": user.username
            }
            return JsonResponse(context, status=200)
        else:
            return render(request, 'index.html')


def signup(request):
  return render(request, 'signup.html')


def signin(request):
  return render(request, 'signin.html')