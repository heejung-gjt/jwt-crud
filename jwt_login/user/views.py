from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import *
import json
import bcrypt
import jwt
 


class SignupView(View):
    def get(self, request, *args, **kwargs):
        context = {'success':'success'}
        return JsonResponse(context)

    def post(self, request, *args, **kwargs):
        data     = json.loads(request.body)
        try:
            if User.objects.filter(username = data['id']).exists() == True:
                context = {'message':'이미 존재하는 아이디'}
                return JsonResponse(context, status = 401)
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            User(
                username = data['id'],
                password = hashed_password,
                nickname = data['nickname']
            ).save()
            context = {'message':'회원가입 성공','password-token':hashed_password}
            return JsonResponse(context, status = 200)
        except KeyError:
            return JsonResponse({'message' : 'invalid_keys'}, status = 400)


class SiginView(View):
    def post(self, request):
        data = json.loads(request.body)
        print(data)
        try:
            if User.objects.filter(username = data['id']).exists():
                user = User.objects.get(username = data['id'])
                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    print('비밀번호 맞습니돠')
                    access_token = jwt.encode({'id':user.id}, 'secret', algorithm='HS256')
                    res = JsonResponse({'access-token': access_token.decode('utf-8'), 'user-id':user.id}, status=200)
                    return res
                return HttpResponse(status=401)
            return HttpResponse(status=401)
        except KeyError:
            return JsonResponse({'message':'invalid keys'}, status = 400)   