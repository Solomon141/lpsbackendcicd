from django.shortcuts import render
import requests
from django.http import JsonResponse
import urllib3
...
urllib3.disable_warnings()

def GetClientByExternalID(request):
    if request.method == 'GET':
        print(' GetClientByExternalID using external id')
        entityExternalId = request.GET.get('entityExternalId')
        api_url = f'https://solomon:P@55w0rd@196.189.119.44:8443/fineract-provider/api/v1/search?exactMatch=true&query={entityExternalId}&resource=clients,clientIdentifiers&tenantIdentifier=default'
        response = requests.get(api_url, verify=False)
        return JsonResponse(response.json(), safe=False)
    
   # 
def UserDetail(request):
    if request.method == 'GET':
        entityAccountNo = request.GET.get('entityAccountNo')
        api_url = f'https://solomon:P@55w0rd@196.189.119.44:8443/fineract-provider/api/v1/clients/{entityAccountNo}?associations=all?&tenantIdentifier=default'
        response = requests.get(api_url, verify=False)
        return JsonResponse(response.json())
    
    
def CustomerAllSavings(request):
    if request.method == 'GET':
        entityAccountNo = request.GET.get('entityAccountNo')
        api_url = f'https://solomon:P@55w0rd@196.189.119.44:8443/fineract-provider/api/v1/clients/{entityAccountNo}/accounts?associations=all?&tenantIdentifier=default'
        response = requests.get(api_url, verify=False)
        return JsonResponse(response.json())
    
    
def GetClientLoanPlan(request):
    if request.method == 'GET':
        loanPlanId = request.GET.get('loanPlanId')
        print('starting qpi request')
        api_url = f'https://solomon:P@55w0rd@196.189.119.44:8443/fineract-provider/api/v1/loans/{loanPlanId}?associations=all&exclude=guarantors,futureSchedule?&tenantIdentifier=default'
        response = requests.get(api_url, verify=False)
        print(response)
        return JsonResponse(response.json(), safe=False)