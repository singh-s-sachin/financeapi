from django.shortcuts import render
from rest_framework import viewsets
from .models import open_account,create_fd
from django.http import HttpResponse
from transactions.models import transaction
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
@csrf_exempt
def fd(request):
        if request.method=='POST':
                message = request.body.decode('utf-8')
                message = json.loads(message)
                mobile=message['mobile']
                amount=message['amount']
                time=message['time']
                actual=open_account.objects.get(mobile=mobile)
                val=int(actual.amount)
                if(val>int(amount)):
                        m=maturity_val(amount,time)
                        val-=int(amount)
                        cd=create_fd(mobile=mobile,amount=amount,time=time,maturity=m)
                        cd.save()
                        open_account.objects.filter(mobile=mobile).update(amount=str(val))
                        return HttpResponse("Your maturity value is "+str(m)+"\n Balance="+str(val))
                else:
                        return HttpResponse("Not enough balance in your account")
def maturity_val(amount,time):
	i=(int(amount)*int(time)*7.3)/100
	i+=int(amount)
	return str(i)