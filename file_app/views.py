from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import FileUploadForm
from django.contrib.auth.decorators import login_required
from .models import UploadedFile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('login')  
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('file_upload')  
        else:
            error_message = "Invalid login credentials. Please try again."
            return render(request, 'registration/login.html', {'error_message': error_message})    
    
    return render(request, 'registration/login.html')


def home(request):
    return render(request, 'home.html')



def user_logout(request):
    logout(request)
    return redirect('login') 


@login_required
def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    
    return render(request, 'file_upload.html', {'form': form})


@login_required
def file_list(request):
    files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'file_list.html', {'files': files})
