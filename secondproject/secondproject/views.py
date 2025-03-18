from django.shortcuts import HttpResponse

data = f"<hr><a href='/'>Home</a> <a href='/signup'>SignUp</a> <a href='/signin'>SignIn </a>"

def index(req):
    
    return HttpResponse(f"<center><h1>Welcome to my page{data}</h1></center>")

def signup(req):
    global username
    username = input("Enter username: ")
    return HttpResponse(f"<center><h1>Sign Up Page{data}</h1></center>")

def signin(req):
    chkusername = input("Enter username to sign in: ")
    if chkusername == username:
        next = f"<hr><h1><a href='/'>Logout</a>"
        return HttpResponse(f"<center><h1>Welcome {chkusername}!{next}</h1></center>")
    else:
        msg = f"<center><h1> Incorrect Username! Try again</h1></center>"
        next = f"<hr><h1><a href='/'>Click here to go Back</a>"
        return HttpResponse(f"{msg}{next}")
    

