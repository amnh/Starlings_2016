from django.shortcuts import render
from .models import Collection
from .models import BasicTraits
from .models import ComplexTraits
from .models import Death
from .models import Identifiers
from .models import Location
from .models import PreSkin
from .models import Preparation
from .models import Skin
from .models import BirdInfo
# Create your views here.

def profile(request):
    return render(request,'profile.html',{})

def search(request):
    return render(request,'search.html',{})

def add_death(request):
    return render(request,'add_death.html',{})

def home(request):
	return render(request, 'home_page.html',{})

def state(request):
	return render(request, 'new_york.html',{})
	westchester= BirdInfo.objects.filter(number__contains='location_id = 1')
	ulster= BirdInfo.objects.filter(number__contains='location_id = 8')
