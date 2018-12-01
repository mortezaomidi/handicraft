from django.contrib.gis.db import models as geomodel
from django.contrib.auth.models import User


class Location(geomodel.Model):
    user = geomodel.ForeignKey(User, on_delete=geomodel.CASCADE)
    create_date = geomodel.DateTimeField(auto_now_add=True, null=True)
    geom = geomodel.MultiPolygonField(srid=4326)

    def __str__(self):
        if self.user:
            return "(%r, %r)" % (self.create_date, self.user.email)
        return "(%r)" % (self.create_date)


class Constrain(geomodel.Model):
    user = geomodel.ForeignKey(User, on_delete=geomodel.CASCADE)
    create_date = geomodel.DateTimeField(auto_now_add=True, null=True)
    geom = geomodel.MultiPolygonField(srid=4326)

    def __str__(self):
        if self.user:
            return "(%r, %r)" % (self.create_date, self.user )
        return "(%r)" % (self.create_date)


class BestLocation(geomodel.Model):
    pass


class Sus(geomodel.Model):
    pass
