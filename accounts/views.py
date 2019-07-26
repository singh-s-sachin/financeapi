from django.shortcuts import render
from rest_framework import viewsets
from .models import open_account
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def open(request):
    if request.method=='POST':
        message = request.body.decode('utf-8')
        message = json.loads(message)
        name=message['name']
        current_address=message['address']
        aadhar=message['aadhar']
        pan=message['pan']
        relative=message['relative']
        mobile=message['mobile']
        amount=message['amount']
        try:
                ac=open_account(name=name,current_address=current_address,aadhar=aadhar,pan=pan,relative=relative,mobile=mobile,amount=amount)
                ac.save()
                return HttpResponse(name,mobile)
        except:
                return HttpResponse("User already exists")