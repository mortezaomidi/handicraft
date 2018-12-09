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
    P1, P2, P3, P4, P5 = (1,2,3,4,5)
    CHOICES = (
        (P1, 'به شدت مخالفم'),
        (P2, 'مخالفم'),
        (P3, 'بی نظر'),
        (P4, 'موافقم'),
        (P5, 'به شدت موافقم'),
    )

    user = geomodel.ForeignKey(User, on_delete=geomodel.CASCADE)
    q1 = geomodel.FloatField(verbose_name="من فکر می کنم این سیستم را به طور مکرر استفاده خواهم نمود", default=3, choices=CHOICES)
    q2 = geomodel.FloatField(verbose_name="من فکر می کنم این سیستم بی خودی پیچیده است و می تواند ساده تر باشد", default=3, choices=CHOICES)
    q3 = geomodel.FloatField(verbose_name="من فکر می کنم استفاده از این سیستم ساده است", default=3, choices=CHOICES)
    q4 = geomodel.FloatField(verbose_name="من فکر می کنم کارکردن با این سیستم نیازمند یک متخصص می باشد", default=3, choices=CHOICES)
    q5 = geomodel.FloatField(verbose_name="من فکر می کنم قابلیت های مختلف در این سیستم به خوبی فراهم شده است", default=3, choices=CHOICES)
    q6 = geomodel.FloatField(verbose_name="من فکر می کنم  دراین سیستم سازگاری زیادی وجود ندارد", default=3, choices=CHOICES)
    q7 = geomodel.FloatField(verbose_name="من فکر می کنم که افراد کار با این سیستم را سریعا یاد می گیرند", default=3, choices=CHOICES)
    q8 = geomodel.FloatField(verbose_name="من فکر می کنم که استفاده از این سیستم سنگین و طاقت فرسا است", default=3, choices=CHOICES)
    q9 = geomodel.FloatField(verbose_name="من احساس اطمینان می کنم از اینکه این سیستم را استفاده می کنم", default=3, choices=CHOICES)
    q10 = geomodel.FloatField(verbose_name="من فکر می کنم که باید با خیلی از ابزارها قبل از استفاده از سیستم اشنایی داشته باشم", default=3, choices=CHOICES)

    def participant_score(self):
        return ((self.q1-1)+(5-self.q2)+(self.q3-1)+(5-self.q4)+(self.q5-1)+(5-self.q6)+(self.q7-1)+(5-self.q8)+(self.q9-1)+(5-self.q10)) * 2.5

    def __str__(self):
        return str(self.user)
