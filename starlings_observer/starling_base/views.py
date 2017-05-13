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
<<<<<<< HEAD
=======
from django.db.models import Prefetch
>>>>>>> 7e0164aa9244e90ce1ec04db41098b4b0f7e155d
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
		
		return render (request, 'new_york.html', context)
	return render(request,'search.html',context)

def home(request):
	return render(request,'home_page.html',{})

def add_death(request):
    return render(request,'add_death.html', {})

<<<<<<< HEAD

=======
>>>>>>> 7e0164aa9244e90ce1ec04db41098b4b0f7e155d
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

def starling_detail(request, number):
<<<<<<< HEAD
    this_starling = BirdInfo.objects.get(pk=number)
    context = {'starling': this_starling}

    return render(request, 'observation_detail.html', context)
=======
   starling = BirdInfo.objects.get(pk=number)
   location = Location.objects.get(pk=starling.location_id)
   collection = Collection.objects.get(pk=location.collection_id)
   ident = Identifiers.objects.get(pk=location.identifiers_id)
   preparation = Preparation.objects.get(pk=starling.preparation_id)
   death = Death.objects.get(pk=preparation.death_id)
   preskin = PreSkin.objects.get(pk=starling.pre_skin_id)
   skin = Skin.objects.get(pk=starling.skin_id)
   complex_traits = ComplexTraits.objects.get(pk=starling.complex_traits_id)
   basic_traits = BasicTraits.objects.get(pk=complex_traits.basic_traits_id)


   context = {'starling': starling}
   context["location"] = location
   context['collection'] = collection
   context['identifiers'] = ident
   context['basictraits'] = basic_traits
   context['complextraits'] = complex_traits
   context['death'] = death
   context['preskin'] = preskin
   context['skin'] = skin
   context['preparation'] = preparation

   return render(request, 'observation_detail.html', context)


	
	

>>>>>>> 7e0164aa9244e90ce1ec04db41098b4b0f7e155d
