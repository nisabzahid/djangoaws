from django.contrib import admin
from .models import MyModel
from django.utils.html import format_html
# Register your models here.
class MyModelAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['text','image_tag',]

admin.site.register(MyModel, MyModelAdmin)