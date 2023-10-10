from django.db import models

# Create your models here.
class MyModel(models.Model):
    text=models.TextField(max_length=100)
    image=models.ImageField(upload_to='image')

    def image_tag(self):
            return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'