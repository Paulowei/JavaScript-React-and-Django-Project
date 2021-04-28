from django.contrib import admin

# Register your models here.
from models import Shoe,ShoeInstance,Brand,Type
#admin.site.register(shoef)

admin.site.register(Shoef)
admin.site.register(ShoeInstance)
admin.site.register(Brand)
admin.site.register(Type)
#admin.site.register(shoef)
class ShoefAdmin(admin.ModelAdmin):
    admin.site.register(Shoef,ShoefAdmin)
    list_display=("name","price","brand","description","colour")
class BrandAdmin(admin.ModelAdmin):
    list_display=("inaug_date","email","name","location")
    admin.site.register(Brand,BrandAdmin)
class TypeAdmin(admin.ModelAdmin):
    admin.site.register(Type,TypeAdmin)
    def display_Brand():
        return ", ".join(Brand.name for Brand in self.Brand.all())
        display_Brand.short_description="Brand"
    def display_Shoe():
        return ", ".join(Shoe.name for Shoe in self.Shoe.all())
        display_Brand.short_description="Shoe"
    list_display=("name","display_Shoe","display_Brand")

    
