from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Client)
admin.site.register(Marque)
admin.site.register(Produit)
admin.site.register(Commande)
admin.site.register(LigneCommande)
