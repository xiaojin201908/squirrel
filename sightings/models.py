from django.db import models

<<<<<<< HEAD
class squirrel(modesl.Model):
    name = models.CharField(
            help_text=_('Latitude'),
    )
=======
from django.utils.translation import gettext as _
class sighting(models.Model):
    Latitude = models.FloatField(help_text=_('Latitude'),
                               max_length=10,)
    Longitude = models.FloatField(help_text=_('Latitude'),
                               max_length=10,)
    Unique_Squirrel_ID = models.IntegerField(primary_key=True) 
    def __str__(self):
      return self.Unique_Squirrel_ID

   
>>>>>>> 015401899814cf97bd667cf32b58f984765febb3
