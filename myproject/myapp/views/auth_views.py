from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
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