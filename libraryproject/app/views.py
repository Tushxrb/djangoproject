from django.shortcuts import render, HttpResponse
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