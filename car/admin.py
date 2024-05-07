from django.contrib import admin
from django.utils.html import format_html
from .models import Car
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnails(self, object):
        return format_html('<img src="{}" width="40" height="40" style="border-radius:50%" />'.format(object.car_photo.url))
    
    thumbnails.short_description = 'Car Image'
    list_display= ('id', 'thumbnails',  'car_title', 'color','model', 'body_style', 'fuel_type', 'is_featured' , 'city')
    list_editable=('is_featured',)
    search_fields= ('id', 'car_title', 'city', 'model', 'body_style', 'fuel_type',)
    list_filter=('city', 'model', 'body_style', 'fuel_type')
admin.site.register(Car, CarAdmin)
