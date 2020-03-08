from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    if request.method =='POST':
        # Get form values
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        username =request.POST['username']
        email =request.POST['email']
        password =request.POST['password']
        password2 =request.POST['password2']

        #check if password match
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                     messages.error(request,'email already exists!')
                     return redirect('register')
                else:
                    #looks good register
                    user = User.objects.create_user(username=username, password=password, email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(request,'You are now registered and can login')
                    return redirect('login')
        else:
            #message
            messages.error(request,'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method =='POST':
        #Login user
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')
    

def logout(request):
    if request.method =='POST':
        auth.logout(request)
        messages.success(request,'You are logged out')
        return redirect('index')

def dashboard(request):

    return render(request, 'accounts/dashboard.html')