from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        errors = {}
        if not email:
            errors['email'] = "Email must be given."
        if not password:
            errors['password'] = "Password must be given."

        auth_user= User.objects.get(email=email)

        if auth_user :        
            user = authenticate(request, username=auth_user.username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request,'auth/login.html')


def register_page(request):
    errors = {}
    if request.method=='POST':
        username= request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        
        if password != confirm_password:
            errors['confirm_password'] = "Password doesn't match."

        if not username:
            errors['username'] = "Username must be given."

        if not errors:
           user = User.objects.create(
                username=username,
                email=email
            )
           user.set_password(password)
           user.save()
           return redirect('login_page')
        else:
            errors['error'] = "Failed to Register"
            return render(request, 'auth/login.html', {'errors':errors})
    return render(request,'auth/register.html')

def logoutpage(request):
        logout(request)
        return redirect('index')
