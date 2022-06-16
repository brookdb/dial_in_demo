from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.apps import apps
from apps.users.models import CustomUser
from apps.roast.models import Roast
from django.template.defaultfilters import slugify
from django.db.models import Q

LABEL_CHOICES = [
    ('Hario V60', 'Hario V60'),
    ('ChemX', 'ChemX'),
    ('Origami', 'Origami'),
    ('Melitta', 'Melitta'),
    ('Kalita', 'Kalita'),
    ('Bee House', 'Bee House'),
]
default_recipie = {
    'id': 0,
    'dose': 10.0,
    'output': 360,
    'grind': 12.0,
    'TSD_score': 5,
}
class Recipie(models.Model):
    dose = models.DecimalField(max_digits=4, decimal_places=2) #coffee ground amount in grams
    output = models.DecimalField(max_digits=5, decimal_places=1)#total liquid output from brew
    grind = models.DecimalField(max_digits=4, decimal_places=1)#relative courseness of ground
    TSD_score = models.IntegerField()#relative score of total soluiable disolved
    flavor_score = models.IntegerField() #relative score of brew |<--sour---sweet---bitter-->|
    brewID = models.ForeignKey('Brew', on_delete=models.CASCADE,)#brew ID of brew this instance of recipie is for
    comment = models.TextField(max_length=555, default=None)
    #is_best = models.BooleanField(default=False) #best recipie for this particular brew

    def __str__(self):
        name = str(self.dose)+"g @ "+str(self.grind)
        return name

    class Meta:
        app_label = 'brew'

class Brew(models.Model):
    userID = models.ForeignKey(CustomUser, related_name='user', on_delete=models.CASCADE,blank=False)#user who is making this brew
    roastID = models.ForeignKey(Roast, related_name='roast', on_delete=models.CASCADE,blank=False)#roast being used for this brew
    bestRecipieID = models.ForeignKey(Recipie, related_name='recipie', on_delete=models.CASCADE, null=True, blank=True)
    roastDate = models.DateField()#day the beans were roasted
    brewDate = models.DateField(default=timezone.now)#The day this brew was added to app
    brew_method = models.CharField(max_length=256, choices=LABEL_CHOICES)#Label Choices
    slug= models.SlugField(max_length=200, blank=True)

    #bestRecipieID

    def display_name(self):
        return self.__str__(self)

    def __str__(self):
        name = self.roastID.name +" on "+ self.brew_method
        return name

    def save(self, *args, **kwargs):
        tmp_slug = self.__str__() + " "+str(self.brewDate)
        self.slug = slugify(tmp_slug)
        super(Brew, self).save(*args, **kwargs)

        return self.slug

    def setBestRecipie(self, recipie):
        self.bestRecipieID = recipie
        self.save()

    class Meta:
        app_label = 'brew'
        ordering = ['brewDate']
