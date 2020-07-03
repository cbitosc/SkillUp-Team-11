from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import requests
import json
from django.http import HttpResponse
p=''
# Create your views here.
def user_login(request):
    return render(request,'user_login.html',None)
def user_registration(request):
    return render(request,'user_registration.html',None)
def registration(request):
    if request.method=="POST":
        #obj=User()
        name=request.POST['name']
        password=request.POST['pw']
        college=request.POST['clname']
        Rollno=request.POST['rno']
        branch=request.POST['branch']
        year=request.POST['year']
        mobile_no=request.POST['mobile no']
        email_id=request.POST['email']
        data={'password':password,'name':name,'Rollno':Rollno,'college':college,'branch':branch,'year':year, 'mobile_no':mobile_no,'email_id':email_id}
        r=requests.post('https://shruthiapi.herokuapp.com/user_register',data)
        k=request.POST.get('name')+"  is registered"
        messages.success(request,k)
        return redirect("http://127.0.0.1:8000/")
def api_call(request):
    Rollno=request.POST.get('Rollno')
    password=request.POST.get('password')
    det={'Rollno':Rollno,'password':password}
    token = requests.post("https://shruthiapi.herokuapp.com/user_login",det)
    if(token.status_code== 200):
        global p
        p = token.json()
        headers = {"Authorization": "Bearer "  + p['access_token']}
        det2={'Rollno':Rollno}
        td = requests.get("http://shruthiapi.herokuapp.com/user_details",det2,headers=headers) 
        res = td.json()
        context={'user_list': res,} 
        return render(request,'api.html',context)
    else:
        messages="credentials invalid"
        context={'messages':messages}
        return render(request,'user_login.html',context)
def profile(request,Rollno):
    det={'Rollno':Rollno}
    token = requests.post("http://shruthiapi.herokuapp.com/roll_access",det)
    if(token.status_code== 200):
        global p
        p = token.json()
        headers = {"Authorization": "Bearer "  + p['access_token']}
        td = requests.get("http://shruthiapi.herokuapp.com/user_details",det,headers=headers) 
        res = td.json()
        context={'user_list': res,} 
        return render(request,'profile.html',context)

    else:
        messages="error"
        context={'messages':messages}
        return render(request,'user_login.html',context)
    
def EventsReg(request,Rollno):
    det={'Rollno':Rollno}
    token = requests.post("http://shruthiapi.herokuapp.com/roll_access",det)
    if(token.status_code== 200):
        global p
        p = token.json()
        headers = {"Authorization": "Bearer "  + p['access_token']}
        td = requests.get("https://shruthiapi.herokuapp.com/user_event",det,headers=headers) 
        res = td.json()
        context={'events_list': res,} 
        return render(request,'EventsReg.html',context)
    else:
        messages="error"
        context={'messages':messages}
        return render(request,'user_login.html',context)
def Events(request):
    token = requests.get("https://shruthiapi.herokuapp.com/events")
    res=token.json()
    context={'Events_list':res,}
    return render(request,'Events.html',context)
def Eventregistration(request,user_id):
    det={'user_id':user_id}
    token = requests.get("https://shruthiapi.herokuapp.com/events")
    res=token.json()
    context={'users':det,'events':res}
    return render(request,'reg.html',context)
def reg(request,user_id):
    event_id=request.POST.get('events')
    det={'user_id':user_id,'event_id':event_id}
    token=requests.post("https://shruthiapi.herokuapp.com/user_evtreg",det)
    if(token.status_code==201):
        return HttpResponse("User Successfully Registered to event")
    elif(token.status_code==400):
        return HttpResponse("You have already registered  for this event")
    else:
        return HttpResponse("There was an error while registration")
def fav(request,user_id):
    token1=requests.get("https://shruthiapi.herokuapp.com/events")
    token1=token1.json()
    det={'user_id':user_id}
    token = requests.post("http://shruthiapi.herokuapp.com/userid_access",det)
    context={'events_list':token1,}
    return render(request,'fav.html',context)

    
    


    