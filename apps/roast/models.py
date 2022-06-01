from django.db import models
from django.template.defaultfilters import slugify

class Roast(models.Model):
    name = models.CharField(max_length=100)
    slug= models.SlugField(max_length=200, blank=True)
    region = models.CharField(max_length=100)
    variatal = models.CharField(max_length=100)
    process = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    notes = models.TextField(max_length=555, default=None)
    thumb = models.ImageField(default='main/images/pixelated-coffee-bag.png', blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def notes_as_list(self):
        return self.notes.split(',')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Roast, self).save(*args, **kwargs)

    class Meta:
        app_label = 'roast'
        ordering = ['name']


#python manage.py makemigrations
#python manage.py migrate
