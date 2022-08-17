from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def LoginView(request):
    """ LOGIN VIEW. """
    try:
        template_name="accounts/login.html"
       
        if request.method=="POST":   
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "Your are successfully logedIn...!")
                return redirect("home:home")
            else:
                messages.warning(request, "Invalid username and password.")
                return render(request, template_name)        

        return render(request, template_name)
    
    except Exception as e:
        print(e)
        return HttpResponse("Page not found.")


def RegisterView(request):
    """ REGISTER VIEW. """
    
    template_name="accounts/register.html"
    if request.method=="POST":
        name     = request.POST['name']
        email    = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        print(name, email, password, confirm_password)
        
        if name=="":
            print("Error")
            messages.error(request, "Please fill the name field.")
            return redirect("accounts:register")
        
        elif email=="":
            messages.warning(request, "Please fill the email field.")
            return redirect("accounts:register")
        
        elif password == "" or confirm_password=="":
            messages.warning(request, "Please fill the password field.")
            return redirect("accounts:register")
        
        elif password!=confirm_password:
            messages.warning(request, "Password doesn't match with confirm password.")
            return redirect("accounts:register")
        
        elif password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'Email already exist.')
                return redirect('accounts:register')
          
            else:
                user = User.objects.create_user(first_name=name,email=email,password=password)
                user.save()
                messages.success(request, "Your account has been successfully created.")
                return redirect('accounts:login')
    return render(request, 'accounts/register.html')


@login_required
def LogoutView(request):
    """ LOGOUT VIEW. """
    logout(request)
    messages.success(request, "You are successfully logout.")
    return redirect("home:home")
