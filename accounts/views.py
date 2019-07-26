from django.shortcuts import render
from rest_framework import viewsets
from .models import open_account,create_fd,create_loan
from django.http import HttpResponse,JsonResponse
from transactions.models import transaction
import json
import datetime
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
@csrf_exempt
def loan(request):
        if request.method=='POST':
                message = request.body.decode('utf-8')
                message = json.loads(message)
                mobile=message['mobile']
                amount=message['amount']
                time=message['time']
                m=0
                try:
                        actual=create_fd.objects.get(mobile=mobile)
                        if(int(amount)<int(actual.amount)):
                                approved=True
                                m=(int(amount)*int(time)*12)/100
                        else:
                                approved=False
                        ln=create_loan(mobile=mobile,amount=amount,duration=str(int(time)*12),time=str(datetime.datetime.now()),repay=str(m/int(time)*12),approved=approved)
                        ln.save()
                        return HttpResponse(approved)
                except:
                        return HttpResponse("User dosent have account with us or may already a loan.")
        if request.method=='GET':
                message = request.body.decode('utf-8')
                message = json.loads(message)
                mobile=message['mobile']
                try:
                        actual=create_loan.objects.get(mobile=mobile)
                        if(actual.approved==True):
                                k={
                                        "approval":"done",
                                        "time":actual.time,
                                        "repay":actual.repay,
                                        "duration":actual.duration
                                        }
                        else:
                                k={
                                        "approval":"pending"
                                }
                        return JsonResponse(k, safe=False)
                except:
                        return HttpResponse("No active/pending loans")
        if request.method=="PUT":
                message = request.body.decode('utf-8')
                message = json.loads(message)
                mobile=message['mobile']
                try:
                        actual=create_loan.objects.get(mobile=mobile)
                        print(actual.approved)
                        if actual.approved==True:
                                return HttpResponse("Loan already approved")
                        else:
                                amt=int(actual.amount)
                                duration=int(actual.duration)
                                create_loan.objects.filter(mobile=mobile).update(approved=True,time=str(datetime.datetime.now()),repay=str(amt/duration))
                                k={
                                        "approval":"done",
                                        "time":actual.time,
                                        "repay":actual.repay,
                                        "duration":actual.duration
                                        }
                                return JsonResponse(k,safe=False)
                except:
                        return HttpResponse("No loans to approve")
        if request.method=="VIEW":
                try:
                        actual=list(create_loan.objects.filter(approved=False).values())
                        return JsonResponse(actual,safe=False)
                except:
                        return HttpResponse("No pending requests.")

