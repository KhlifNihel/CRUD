from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    #Home
    path('',views.home,name='home'),
    #Add_client
    path('add_client',views.add_client,name='add_client'),
    #view Client
    path('client/<str:client_id>',views.client,name='client'),
    #Edit client
    path('edit_client',views.edit_client,name='edit_client'),
    #Delete client
    path('delete_client/<str:client_id>',views.delete_client,name='delete_client'),
    
    #HomeMarque
    path('home_marque',views.home_marque,name='home_marque'),
    #Add_marque
    path('add_marque',views.add_marque,name='add_marque'),
    #view marque
    path('marque/<str:marque_id>',views.marque,name='marque'),
    #Edit marque
    path('edit_marque',views.edit_marque,name='edit_marque'),
    #Delete marque
    path('delete_marque/<str:marque_id>',views.delete_marque,name='delete_marque'),

    #HomeProduit
    path('home_produit',views.home_produit,name='home_produit'),
    #Add_produit
    path('add_produit',views.add_produit,name='add_produit'),
    #view produit
    path('produit/<str:produit_id>',views.produit,name='produit'),
    #Edit produit
    path('edit_produit',views.edit_produit,name='edit_produit'),
    #Delete produit
    path('delete_produit/<str:produit_id>',views.delete_produit,name='delete_produit'),

    #Homecommande
    path('home_commande',views.home_commande,name='home_commande'),
    #Add_commande
    path('add_commande',views.add_commande,name='add_commande'),
    #view commande
    path('commande/<str:commande_id>',views.commande,name='commande'),
    #Edit commande
    path('edit_commande',views.edit_commande,name='edit_commande'),
    #Delete commande
    path('delete_commande/<str:commande_id>',views.delete_commande,name='delete_commande'),

    #HomeLignecommande
    path('home_ligneCommande',views.home_ligneCommande,name='home_ligneCommande'),
    #addLignecommande
    path('add_ligneCommande',views.add_ligneCommande,name='add_ligneCommande'),
    #view commande
    path('ligneCommande/<str:ligneCommande_id>',views.ligneCommande,name='ligneCommande'),
    #Edit ligneCommande
    path('edit_ligneCommande',views.edit_ligneCommande,name='edit_ligneCommande'),
    #Delete lignecommande
    path('delete_ligneCommande/<str:ligneCommande_id>',views.delete_ligneCommande,name='delete_ligneCommande'),

    
]
