
# Create your views here.
from django.shortcuts import render, redirect

# Hardcoded credentials
USERNAME = "coyne_101"
PASSWORD = "dssh_9349"

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == USERNAME and password == PASSWORD:
            return redirect('success')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def success_page(request):
    return render(request, 'success.html')

