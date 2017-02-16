from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request,'profile.html',{})

def search(request):
    return render(request,'search.html',{})

def add_death(request):
    return render(request,'add_death.html',{})

def home(request):
	return render(request, 'home_page.html',{})