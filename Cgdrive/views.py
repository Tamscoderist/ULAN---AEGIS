from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to some homepage after login
        else:
            # Invalid login credentials
            return render(request, 'Cgdrive/index.html', {'error': 'Invalid credentials'})
        
    return render(request, 'Cgdrive/index.html')
