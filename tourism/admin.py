from django.contrib.gis import admin
from .models import Location, Constrain, BestLocation, Sus

admin.site.register(Location, admin.BingGeoAdmin)
admin.site.register(Constrain, admin.BingGeoAdmin)
admin.site.register(Sus)
