from django.db import models
from django.conf import settings
# apps de terceros
from model_utils.models import TimeStampedModel

# 
from applications.entries.models import Entry
# managers
from .managers import FavoritesManager

class Favorites(TimeStampedModel):
    """ Modelo para representar las entradas favoritas de los usuarios """
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_favorites', on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, related_name='entry_favorites', on_delete=models.CASCADE)
    
    objects = FavoritesManager()

    class Meta:
        unique_together = ('user', 'entry')
        verbose_name = 'Entrada Favorita'
        verbose_name_plural = 'Entradas Favoritas'
        
    def __str__(self):
        return self.entry.title