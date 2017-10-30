from django.contrib import admin

# Register your models here.
from .models import MovieStar,Starring

class MovieAdmin(admin.ModelAdmin):
  list_display = ('image','id','title', 'director','score','type','country','starring')
  search_fields = ('title', 'director','score',)
  list_filter = ('score',)

class StarringAdmin(admin.ModelAdmin):
  list_display = ('id','actor', 'count','movie')
  search_fields = ('actor', 'count',)
  list_filter = ('count',)

admin.site.register(MovieStar,MovieAdmin)
admin.site.register(Starring,StarringAdmin)