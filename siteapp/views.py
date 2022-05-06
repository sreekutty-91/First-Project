from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.core.checks import messages
from django.contrib import messages
from django.contrib.auth import authenticate,login



# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')

def loginpage(request):
    return render(request,'login.html')        

def about(request):
    return render(request,'about.html')  

def Register(request):
   if request.method=='POST':
      first_name=request.POST['first_name']
      last_name=request.POST['last_name']
      username=request.POST['Username']
      password1=request.POST['password1']
      password2=request.POST['password2']
      email=request.POST['email']
      if password1==password2:
         if User.objects.filter(username=username).exists():
            messages.info(request,'Username already taken')
            return redirect('signup')
         elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already taken')
            return redirect('signup')
         else:      
            user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save()
         print('user created')
      else:
         message.info(request,'password not matching')      
         return redirect('signup')
      return redirect('login')
   else:
      return render(request,'signup.html')

def login(request):
 if request.method=="POST":
      username=request.POST['username']
      password=request.POST['password']
      user=auth.authenticate(username=username,password=password)
      
      if user is not None:
         auth.login(request,user)
         messages.info(request, f'Welcome {username}')
         return redirect('about')
      else:
         messages.info(request, 'Invalid Credentials.Try again.')
         return redirect('loginpage')
 else:
		#messages.info(request, 'Oops, Something went wrong.')
		return redirect('loginpage')


def logout(request):
   auth.logout(request)
   return redirect('home') 





