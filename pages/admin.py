from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class Teamadmin(admin.ModelAdmin):
    def thumbnails(self, object):
        return format_html('<img src="{}" width="40" height="40" style="border-radius:50%" />'.format(object.photo.url))
    
    thumbnails.short_description = 'Photo'
    list_display = ('id', 'thumbnails', 'first_name', 'designation', 'crteated_date')
    list_display_links = ('first_name','id','thumbnails',)  #to make it clickable
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)
admin.site.register(Team, Teamadmin)
