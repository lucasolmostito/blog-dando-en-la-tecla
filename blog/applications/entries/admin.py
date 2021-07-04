from django.contrib import admin
from .models import Category, Tag, Entry, Comments
# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Entry)
admin.site.register(Comments)
