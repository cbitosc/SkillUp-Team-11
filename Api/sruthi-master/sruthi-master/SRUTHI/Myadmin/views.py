from django.shortcuts import render
import requests
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
import json
from django.http import HttpResponse,JsonResponse

# Create your views here.
def Myadmin(request):
    return render(request,'admin-login.html',None)

def admin_login(request):
    admin_id=request.POST.get('admin_id')
    password=request.POST.get('pwd')
    det={"admin_id":admin_id,"password":password}
    token = requests.post("https://shruthiapi.herokuapp.com/admin_login",det)
    if(token.status_code== 200):
        global p
        p = token.json()['access_token']
        headers = {"Authorization": "Bearer "  + p}
        td = requests.get("https://shruthiapi.herokuapp.com/requests",headers=headers) 
        res = td.json()
        td1 = requests.get("https://shruthiapi.herokuapp.com/view_user",headers=headers) 
        res1 = td1.json()
        events_list=requests.get("https://shruthiapi.herokuapp.com/events")
        events_list=events_list.json()
        context={'request_list': res,'users':res1,'events_list':events_list} 
        return render(request,'admin-page.html',context)
    else:
        messages="credentials invalid"
        context={'messages':messages}
        return render(request,'admin-login.html',context)

def hi(request):
    id=request.GET.get("id")
    det1={'req_id':id}
    resp= requests.post("http://shruthiapi.herokuapp.com/confirmation",det1,headers = {'Authorization':f'Bearer {p}'})
    td = requests.get("https://shruthiapi.herokuapp.com/requests",headers={'Authorization':f'Bearer {p}'}) 
    res = td.json()
    td1 = requests.get("https://shruthiapi.herokuapp.com/view_user",headers={'Authorization':f'Bearer {p}'}) 
    res1 = td1.json()
    context={'request_list': res,'users':res1,} 
    return render(request,'admin-page.html',context)
def hi1(request):
    id=request.GET.get("id")
    det1={'req_id':id}
    resp= requests.post("https://shruthiapi.herokuapp.com/req_remove",det1,headers = {'Authorization':f'Bearer {p}'})
    td = requests.get("https://shruthiapi.herokuapp.com/requests",headers={'Authorization':f'Bearer {p}'}) 
    res = td.json()
    td1 = requests.get("https://shruthiapi.herokuapp.com/view_user",headers={'Authorization':f'Bearer {p}'}) 
    res1 = td1.json()
    context={'request_list': res,'users':res1,} 
    return render(request,'admin-page.html',context)

    
