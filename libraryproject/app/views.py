from django.shortcuts import render, HttpResponse, redirect
from .models import Book
from datetime import datetime

# Create your views here.

# def index(req):
#     allbooks = Book.objects.all()
#     print(allbooks)
#     return HttpResponse(f'All Books: {allbooks}')

def index(req):
    allbooks = Book.objects.all()
    print(allbooks)
    # context = {'myname': "ITV"}
    # return render(req, "index.html", context)
    myname = "Tushar"
    print(datetime.now())
    curdate = datetime.now()
    hour = datetime.now().hour
    print(hour)
    context = {"myname": myname, "curdate":curdate, "hour":hour, "allbooks":allbooks}
    return render(req, "index.html", context)

def signup(req):
    print(req.method)
    if req.method=="GET":
        return render(req, 'signup.html')
    else:
        print(req.method)
        uname=req.POST["uname"]
        upass=req.POST["upass"]
        ucpass=req.POST["ucpass"]
        print(uname, upass, ucpass)
        if upass != ucpass:
            errmsg='Password and Confirm password must be same'
            context={'errmsg':errmsg}
            return render(req, 'signup.html', context)
        else:
            return redirect("signin")


def signin(req):
    print(req.method)
    return render(req, 'signin.html')



