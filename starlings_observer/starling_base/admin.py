from django.contrib import admin
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

admin.site.register(Collection)
admin.site.register(BasicTraits)
admin.site.register(ComplexTraits)
admin.site.register(Death)
admin.site.register(Identifiers)
admin.site.register(Location)
admin.site.register(PreSkin)
admin.site.register(Preparation)
admin.site.register(Skin)
admin.site.register(BirdInfo)