from django.db import models
from django.utils.translation import gettext as _
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 8aa4227d5f1ee6ef6d6cfd271560a0bbc77b0350
class squirrel(modesl.Model):
    Latitude = models.FloatField(help_text=_('Latitude'),
                               max_length=10,)
    Longitude = models.FloatField(help_text=_('Latitude'),
                               max_length=10,)
    Unique_Squirrel_ID = models.IntegerField(primary_key=True) 
    def __str__(self):
      return self.Unique_Squirrel_ID
    Shift = models.CharField(help_text=_('Shift'),max_length=100,)
    Date = models.DateField(
            help_text=_('Date'),
    )
    Age = models.FloatField(
            help_text=_('Age of squirrel'),
            max_length = 100,)
    Fur_Colors = (
            (GRAY, 'Gray'),
            (CINNAMON,'Cinnamon'),
            (BLACK,'Black'),
    )

