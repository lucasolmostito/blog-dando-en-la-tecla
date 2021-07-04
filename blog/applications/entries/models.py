from datetime import timedelta, datetime

from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy

# Apps de Terceros
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
# managers
from .managers import EntryManager, CommentManager

class Category(TimeStampedModel):   
    """ Categoría de una entrada """

    short_name = models.CharField('Nombre corto', max_length=15, unique=True)
    name = models.CharField('Nombre', max_length=30)
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorias'
         
    def __str__(self):
        return self.name
    
class Tag(TimeStampedModel):
    """ Etiquetas de un artículo del blog """
    
    name = models.CharField('Nombre', max_length=30)
    
    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
    
    def __str__(self):
        return self.name
    

class Entry(TimeStampedModel):
    """ Modelo para entradas o artículos """
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    title = models.CharField('Título', max_length=200)
    resume = models.TextField('Resumen')
    content = RichTextUploadingField('Contenido')
    public = models.BooleanField(default=False)
    image = models.ImageField('Imagen', upload_to='Entry')
    cover = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)
    
    objects = EntryManager()
    
    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'      
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy(
            'app_entry:entry-detail',
            kwargs={
                'slug': self.slug
            }
        )
    
    def save(self, *args, **kwargs):
        # Calculamos el total de segundos de la hora actual
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' %(self.title, str(seconds))
        
        self.slug = slugify(slug_unique)
        
        super(Entry, self).save(*args, **kwargs)
        

class Comments(TimeStampedModel):
    """ Modelo para representar los comentarios """
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    adjective = models.CharField('Adjetivo', max_length=50, blank=True)
    message = models.CharField('Mensaje', max_length=400)
    
    objects = CommentManager()
    
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentario'
        
    def __str__(self):
        return self.adjective