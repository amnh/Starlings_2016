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
	birds= BirdInfo.objects.all().order_by('number')
	locations= Location.objects.order_by('state')
	
	context = {'birds':birds,'locations':locations}
	
	if request.method == 'POST':
		this_location = Location.objects.get(state=request.POST['location'])
		context['location']= this_location
		return render(request, 'new_york.html',context)
	else:
		context['error_message'] = "It didn't work"
		return render(request, 'search.html',context)
	