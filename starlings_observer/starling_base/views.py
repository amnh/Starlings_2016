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
from django.db.models import Prefetch
# Create your views here.

def profile(request):
    return render(request,'profile.html',{})

def search(request):
	locations= Location.objects.values('state').distinct()
	context={'locations_list':locations}
	if request.method == 'POST':
		this_location = request.POST['location']
		context['this_location'] = this_location
		context['birds']= BirdInfo.objects.filter(location__in=Location.objects.filter(state = request.POST['location'])).order_by('number')
		place= Location.objects.values('county').distinct()
		context['counties']= Location.objects.filter(state=request.POST['location'])
		
		"""if (request.POST['location'] == "NY"):
			context['birds_found']= birds
						'location': this_location,
						} 
		""" 
		return render (request, 'new_york.html', context)
	return render(request,'search.html',context)

def home(request):
	return render(request,'home_page.html',{})

def starling_detail(request):
	return render(request, 'observation_detail.html', {})

def add_death(request):
    return render(request,'add_death.html', {})

def add_collection(request):
    return render(request,'add_collection.html', {})

def add_identifiers(request):
    return render(request,'add_identifiers.html',{})

def add_complex_traits(request):
    return render(request,'add_complex_traits.html',{})

def add_preparation(request):
    return render(request,'add_preparation.html',{})

def add_location(request):
    return render(request,'add_location.html',{})

def add_skin(request):
    return render(request,'add_skin.html',{})

def add_pre_skin(request):
    return render(request,'add_pre_skin.html/add_pre_skin.html',{})



	
	

