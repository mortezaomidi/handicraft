from django.contrib.gis import forms as geoforms
from .models import Location, Constrain, BestLocation

from leaflet.forms.widgets import LeafletWidget

class LocationForm(geoforms.ModelForm):
    class Meta:
        model = Location
        exclude = ['user', 'create_date']
        widgets = {'geom': LeafletWidget()}


class ConstrainForm(geoforms.ModelForm):
    class Meta:
        model = Constrain
        exclude = ['user', 'create_date']
        widgets = {'geom': LeafletWidget()}
