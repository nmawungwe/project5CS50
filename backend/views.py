from django.shortcuts import render
import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum


from .models import User, Appliance_list

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'backend/index.html')
    else:
        return render(request, 'backend/login.html')

def login_view(request):
    if request.method == "POST":
        #Attempt to sign in user
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        #checking if authentification was successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "backend/login.html", {"message":"Incorrect username/password"})
    else:
        return render(request, "backend/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        #Esurring passwords match
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "backend/register.html", {"message":"Passwords must match"})
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "backend/register.html", {"message":"Username already taken."})
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "backend/register.html")



def appliances(request):
        try:
            appliances_list = Appliance_list.objects.get(user=request.user.id)
        except Appliance_list.DoesNotExist:
            return JsonResponse({"Message":"Appliance list doesn't exist"}, status=404)

        if request.method == "GET":
            appliances_list = json.dumps(appliances_list.serialize())
            appliances_list = json.loads(appliances_list)
            return JsonResponse(appliances_list, safe=False, status=200)
        elif request.method == "POST":
            data = json.loads(request.body)
            TVs_num = data.get("TVs_num")
            Decoders_num = data.get("Decoders_num")
            SoundSystems_num = data.get("SoundSystems_num")
            Lights_num = data.get("Lights_num")
            Heaters_num = data.get("Heaters_num")
            Stoves_num = data.get("Stoves_num")
            Fridges_num = data.get("Fridges_num")
            Kettles_num = data.get("Kettles_num")
            Microwaves_num = data.get("Microwaves_num")
            Computers_num = data.get("Computers_num")
            Printers_num = data.get("Printers_num")
            Modems_num = data.get("Modems_num")
            ElectricBlankets_num = data.get("ElectricBlankets_num")
            Phones_num = data.get("Phones_num")
            addition = Appliance_list(user=request.user, TVs_num=TVs_num, Decoders_num=Decoders_num, SoundSystems_num=SoundSystems_num, Lights_num=Lights_num , Heaters_num=Heaters_num, Stoves_num=Stoves_num, Fridges_num=Fridges_num, Kettles_num=Kettles_num, Microwaves_num=Microwaves_num, Computers_num=Computers_num, Printers_num=Printers_num, Modems_num=Modems_num, ElectricBlankets_num=ElectricBlankets_num, Phones_num=Phones_num)
            addition.save()
            return JsonResponse({"message":"Addition of appliances was successful"}, status=201)
        elif request.method =='DELETE':
            appliances_list.delete()
            return JsonResponse({"message":"appliance list deleted"})
        else:
            data = json.loads(request.body)
            TVs_num = data.get("TVs_num")
            Decoders_num = data.get("Decoders_num")
            SoundSystems_num = data.get("SoundSystems_num")
            Lights_num = data.get("Lights_num")
            Heaters_num = data.get("Heaters_num")
            Stoves_num = data.get("Stoves_num")
            Fridges_num = data.get("Fridges_num")
            Kettles_num = data.get("Kettles_num")
            Microwaves_num = data.get("Microwaves_num")
            Computers_num = data.get("Computers_num")
            Printers_num = data.get("Printers_num")
            Modems_num = data.get("Modems_num")
            ElectricBlankets_num = data.get("ElectricBlankets_num")
            Phones_num = data.get("Phones_num")
            appliances_list.TVs_num =TVs_num 
            appliances_list.Decoders_num=Decoders_num 
            appliances_list.SoundSystems_num=SoundSystems_num
            appliances_list.Lights_num=Lights_num 
            appliances_list.Heaters_num=Heaters_num 
            appliances_list.Stoves_num=Stoves_num 
            appliances_list.Fridges_num=Fridges_num 
            appliances_list.Kettles_num=Kettles_num 
            appliances_list.Microwaves_num=Microwaves_num 
            appliances_list.Computers_num=Computers_num 
            appliances_list.Printers_num=Printers_num 
            appliances_list.Modems_num=Modems_num 
            appliances_list.ElectricBlankets_num=ElectricBlankets_num 
            appliances_list.Phones_num=Phones_num
            appliances_list.save()
            return JsonResponse({"message":"Appliance list has been updated"}, status=201)


def appliances_post(request):
    if request.method == "POST":
        data = json.loads(request.body)
        TVs_num = data.get("TVs_num")
        Decoders_num = data.get("Decoders_num")
        SoundSystems_num = data.get("SoundSystems_num")
        Lights_num = data.get("Lights_num")
        Heaters_num = data.get("Heaters_num")
        Stoves_num = data.get("Stoves_num")
        Fridges_num = data.get("Fridges_num")
        Kettles_num = data.get("Kettles_num")
        Microwaves_num = data.get("Microwaves_num")
        Computers_num = data.get("Computers_num")
        Printers_num = data.get("Printers_num")
        Modems_num = data.get("Modems_num")
        ElectricBlankets_num = data.get("ElectricBlankets_num")
        Phones_num = data.get("Phones_num")
        addition = Appliance_list(user=request.user, TVs_num=TVs_num, Decoders_num=Decoders_num, SoundSystems_num=SoundSystems_num, Lights_num=Lights_num , Heaters_num=Heaters_num, Stoves_num=Stoves_num, Fridges_num=Fridges_num, Kettles_num=Kettles_num, Microwaves_num=Microwaves_num, Computers_num=Computers_num, Printers_num=Printers_num, Modems_num=Modems_num, ElectricBlankets_num=ElectricBlankets_num, Phones_num=Phones_num)
        addition.save()
        return JsonResponse({"message":"Addition of appliances was successful"}, status=201)







