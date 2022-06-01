from django.contrib import admin
from .models import Brew, Recipie
from .forms import AddBrew

class BrewAdmin(admin.ModelAdmin):

    add_form = AddBrew
    form = AddBrew
    model= Brew
    list_display = ('__str__', 'brewDate',)
    list_filter = ('brewDate', 'brew_method', 'roastDate',)
    fieldsets = (
        ('Roast Info', {'fields': ('roastID', 'roastDate')}),
        ('Brew Info', {'fields': ('brew_method','bestRecipieID')}),
    )
    ordering = ('roastDate', 'brew_method',)

admin.site.register(Brew, BrewAdmin)
admin.site.register(Recipie)
