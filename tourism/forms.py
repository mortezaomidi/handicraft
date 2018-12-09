from django.contrib.gis import forms as geoforms
from .models import Location, Constrain, BestLocation, Sus
from leaflet.forms.widgets import LeafletWidget




fields_name = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']

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


class SusForm(geoforms.ModelForm):
    class Meta:
        model = Sus
        exclude = ['user']
        widgets = {field: geoforms.RadioSelect for field in fields_name}
