from django.db import models
from django.db.models import Q

class EntryManager(models.Manager):
    """ procedimiento para entrada """
    
    def cover_entry(self):
        return self.filter(
            public = True,
            cover = True,
        ).order_by('-modified').first()
    
    def in_home_entry(self):
        # Devuleve las últimas 4 entradas en home
        return self.filter(
            public = True,
            in_home = True,
        ).order_by('-modified')[:4]
        
    def recent_entry(self):
        # Devuelve las últimas 6 entradas recientes
        return self.filter(
            public=True,           
        ).order_by('-modified')[:6]
        
    def search_entry(self, kword, category):
        # Hacemos una consulta en base a un kword o categoria proporcionada por el usuario
        if len(category) > 0:
            return self.filter(
                category__name = category,
                public = True
            ).filter(
                Q(title__icontains=kword) | Q(resume__icontains=kword),
            ).order_by('-modified')
        else:
            return self.filter(
                public = True
            ).filter(
                Q(title__icontains=kword) | Q(resume__icontains=kword),
            ).order_by('-modified')
            
    def entries_user(self, user):
        if not user.is_anonymous:
            return self.filter(
                entry_favorites__user = user
            )
        else:
            return None


class CommentManager(models.Manager):
    
    def add_comment(self, comment, user, current_entry):
        return self.create(
            user = user,
            entry = current_entry,
            message = comment
        )