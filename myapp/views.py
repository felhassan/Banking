from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import CustomUser
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


def myapp(request):
    customUsers=CustomUser.objects.all()
    MY_DATA={'customUsers': customUsers}
    return render(request,"myapp\index.html",context=MY_DATA)

def index(request):
    name="Unknown User"
    if request.GET.get("name") is not None:
        name=request.GET["name"]
    return HttpResponse(f"Hello Dear {name}")
  

def customusers(request):
    customUsers=CustomUser.objects.all()
    MY_DATA={'customUsers': customUsers}
    return HttpResponse(MY_DATA)

@csrf_exempt  
def users(request):
    if request.method=="GET":
        if request.GET.get("CustomUser_id") is not None:
            customUser_id=request.GET["CustomUser_id"]
            try:
                customUsers=CustomUser.objects.get(id=customUser_id).serialize()
                MY_DATA={'customUsers': customUsers}        
            except CustomUser.DoesNotExist:
                MY_DATA={
                    'No user found for this ID': customUser_id,
                    'Please try again with other ID': '?',
                }
                MY_DATA={'customUsers': MY_DATA}
        else:
            customUsers=list(CustomUser.objects.all().values("id","first_name","last_name","email"))
            MY_DATA={'customUsers': customUsers}
    else:
        if request.method=="POST":
            try:
                data=json.loads(request.body)
                customUser_id=data["Custom User ID"]
                try:
                    customUsers=CustomUser.objects.get(id=customUser_id).serialize()
                    MY_DATA={'customUsers': customUsers}  
                except CustomUser.DoesNotExist:
                    MY_DATA={
                        'No user found for this ID': customUser_id,
                        'Please try again with other ID': '?',
                    }
                    MY_DATA={'customUsers': MY_DATA}     
            except KeyError:
                MY_DATA={
                    'Key Not found': "Custom User ID",
                    'Please try again with other Key': '?',
                } 
               
        else:
            customUsers=list(CustomUser.objects.all().values("id","first_name","last_name","email"))
            MY_DATA={'customUsers': customUsers} 
    return JsonResponse(MY_DATA)
