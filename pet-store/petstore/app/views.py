from django.shortcuts import render, HttpResponse, redirect
from .models import Pet
from datetime import datetime
from django.contrib.auth.models import User

# Create your views here.

def index(req):
    allpets = Pet.objects.all()
    # petsdata = Pet.objects.filter(petname = "Chotu")
    return render(req, 'index.html',{"allpets":allpets})

def signup(req):
    print(req.method)
    if req.method=="GET":
        return render(req, 'signup.html')
    else:
        print(req.method)
        uname=req.POST["uname"]
        uemail=req.POST["uemail"]
        upass=req.POST["upass"]
        ucpass=req.POST["ucpass"]
        print(uname, upass, ucpass,uemail)
        if upass != ucpass:
            errmsg='Password and Confirm password must be same'
            context={'errmsg':errmsg}
            return render(req, 'signup.html', context)
        elif uname==upass:
            errmsg='Email address and password must not be same'
            context={'errmsg':errmsg}
            return render(req, 'signup.html', context)
        else:
            try:
                userdata = User.objects.create(username=uname, email=uemail, password=upass)
                userdata.set_password(upass)
                userdata.save()
                print(User.objects.all())
                return redirect("signin")
            except:
                errmsg="User already exists. Try with different username"
                context = {"errmsg":errmsg}
                return render(req, "signup.html", context)

from django.contrib.auth import authenticate, login, logout

def signin(req):
    if req.method=="GET":
        print(req.method)
        return render(req, 'signin.html')
    else:
        uname = req.POST.get("uname")
        uemail=req.POST.get('uemail')
        upass=req.POST['upass']
        print(uemail, upass)
        # userdata=User.objects.filter(email=uemail, password=upass)
        userdata = authenticate(username=uname, email=uemail, password=upass)
        print(userdata)
        if userdata is not None:
            login(req, userdata)
            # return render(req, 'dashboard.html')
            return redirect("dashboard")
        else:
            context ={}
            context['errmsg'] = 'Invalid email or password'
            return render(req, "signin.html", context)
        
def dashboard(req):
    print(req.user)
    username= req.user
    allpets = Pet.objects.all()
    print(allpets)
    return render(req, "dashboard.html", {"username":username, "allpets": allpets})

def userlogout(req):
    logout(req)
    return redirect('/')

def petdetails(req, petid):
    petdata = Pet.objects.get(petid=petid)
    context = {'petdata': petdata}
    return render(req, 'pet-details.html', context)

from .forms import PetForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

class PetRegister(CreateView):
    model = Pet
    fields = "__all__"
    success_url = "/dashboard"
    
class PetUpdate(UpdateView):
    model = Pet
    template_name_suffix = "_update_form"
    fields = "__all__"
    success_url = "/dashboard"
    

class PetDelete(DeleteView):
    model = Pet
    success_url = "/dashboard"

from django.contrib import messages
from django.db.models import Q


def searchpets(req):
    query = req.GET["q"]
    print(query)
    allpets = Pet.objects.filter(
        Q(petname__icontains=query) | Q(description__icontains=query) | Q(gender__icontains=query))
    print(allpets, len(allpets))
    if len(allpets)==0:
        messages.error(req, "No results found!")
        
    context = {"allpets": allpets}
    
    if req.user.is_authenticated:
        return render(req, "dashboard.html", context)
    else:
        return render(req, "index.html", context)
        
def searchbygender(req):
    gender = req.GET["gender"]
    if gender == "male":
        allpets = Pet.objects.filter(gender__exact="Male")
    else:
        allpets = Pet.objects.filter(gender__exact="Female")
    print(allpets)
    context={"allpets":allpets}
    return render(req, "index.html", context)

def req_passwoed(req):
    if req.method=="POST":
        uemail = req.POST["uemail"]
        try:
            user = User.objects.get(email=uemail)
            return render(req, 'dashboard.html')
        except User.DoesNotExist:
            messages.error(req, "No account found with this email id.")
            return render(req, "index.html")
    
    
