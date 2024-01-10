from django.contrib import admin
from .models import genre,Movie
# Register your models here.
class genreadmin(admin.ModelAdmin):
    list_display=('id','name')
    
class movieadmin(admin.ModelAdmin):
    list_display=('id','genre1','release_yeat')
    
    
admin.site.register(genre,genreadmin)
admin.site.register(Movie,movieadmin)

