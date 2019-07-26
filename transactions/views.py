from django.shortcuts import render
from rest_framework import viewsets
from .models import transaction
from django.http import HttpResponse,JsonResponse
import json
import datetime
from accounts.models import open_account
# Create your views here.

from django.views.decorators.csrf import csrf_exempt
#tid=2019000001
@csrf_exempt
def deposit(request):
    if request.method=='POST':
        message = request.body.decode('utf-8')
        message = json.loads(message)
        mobile=message['mobile']
        amount=int(message['amount'])
        actual=open_account.objects.get(mobile=mobile)
        t=int(actual.amount)+amount
        actual.amount=str(t)
        actual.save()
        savetransaction('deposit',amount,mobile)
        return HttpResponse("Balance="+str(t))

@csrf_exempt
def debit(request):
    if request.method=='POST':
        message = request.body.decode('utf-8')
        message = json.loads(message)
        mobile=message['mobile']
        amount=int(message['amount'])
        actual=open_account.objects.get(mobile=mobile)
        t=int(actual.amount)
        if(amount>t):
            return HttpResponse("Insufficient balance")
        else:
            t-=amount
            open_account.objects.filter(mobile=mobile).update(amount=str(t))
            actual.amount=str(t)
            print(actual.amount)
            savetransaction('debit',amount,mobile)
            return HttpResponse("Balance="+str(t))



@csrf_exempt
def credit(request):
    if request.method=='POST':
        message = request.body.decode('utf-8')
        message = json.loads(message)
        mobile=message['mobile']
        amount=int(message['amount'])
        actual=open_account.objects.get(mobile=mobile)
        t=int(actual.amount)+amount
        open_account.objects.filter(mobile=mobile).update(amount=str(t))
        savetransaction('credit',amount,mobile)
        return HttpResponse(t)

def savetransaction(ty,amount,mobile):
    tid=datetime.datetime.now()
    t=transaction(tid=str(tid),kind=ty,amount=amount,account=mobile)
    t.save()
def showtransactions(request):
    if request.method=='GET': 
        message = request.body.decode('utf-8')
        message = json.loads(message)
        mobile=message['mobile']  
        if(mobile!="0000000000"):
            a=list(transaction.objects.filter(account=mobile).values())
            print(a)
        else:
            a=list(transaction.objects.all().values())
        return JsonResponse(a,safe=False)
