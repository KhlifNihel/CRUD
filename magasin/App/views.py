from django.urls import reverse
from django.shortcuts import render,redirect
from App.models import Client,Marque,Produit,Commande,LigneCommande
from django.http import HttpResponseRedirect
from .forms import *
"""========================================================== CLIENT ============================================
================================================================================================================="""
#Home
def home(request):
    context={
        'clients' : Client.objects.all()
    }
    
    return render(request, 'home.html',context)

#Addclient
def add_client(request):
    if request.method == "POST":
        if request.POST.get('nom') \
            and request.POST.get('adresse') \
            and request.POST.get('telephone') :

            client=Client()
            client.nom = request.POST.get('nom')
            client.adresse = request.POST.get('adresse')
            client.telephone = request.POST.get('telephone')
            
            client.save()
            return HttpResponseRedirect('/')
    else:
        return render(request,'add.html')


#view client individually
def client(request,client_id):
    client=Client.objects.get(id = client_id)
    if client != None:
        return render(request,'edit.html',{'client':client})

#Edit client 
def edit_client(request):
    if request.method == 'POST':
        client = Client.objects.get(id = request.POST.get('id'))
        if client != None:
            client.nom = request.POST.get('nom')
            client.adresse = request.POST.get('adresse')
            client.telephone = request.POST.get('telephone')
            
            client.save()
            return HttpResponseRedirect('/')




#delete client
def delete_client(request,client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
    return HttpResponseRedirect('/')


"""======================================================== Marque =========================================================
============================================================================================================================"""

#homeMarque
def home_marque(request):
    context={
        'clients' : Client.objects.all(),
        'marques':Marque.objects.all()

    }
    
    return render(request, 'home_marque.html/', context)

#AddMarque
def add_marque(request):
    if request.method == "POST":
        if request.POST.get('designation'):
            marque=Marque()
            marque.designation = request.POST.get('designation')
            marque.save()
            return redirect('home_marque')
    else:
        return render(request,'add_marque.html/')
    
#view marque individually
def marque(request,marque_id):

    marque=Marque.objects.get(id_marque = marque_id)
    if marque != None:
        return render(request,'edit_marque.html/',{'marque':marque})
    
#Edit marque 
def edit_marque(request):
    if request.method == 'POST':
        marque = Marque.objects.get(id_marque = request.POST.get('id_marque'))
        if marque != None:
            marque.designation = request.POST.get('designation')
            marque.save()
            return HttpResponseRedirect('home_marque')
        
#delete marque
def delete_marque(request,marque_id):
    marque = Marque.objects.get(id_marque = marque_id)
    marque.delete()
    return HttpResponseRedirect('/')


"""=========================================================== PRODUIT ==================================================
========================================================================================================================"""
#HomeProduit
def home_produit(request):
    context={
        'clients' : Client.objects.all(),
        'marques':Marque.objects.all(),
        'produits':Produit.objects.all(),

    }
  
    return render(request, 'home_produit.html',context)

#AddProduit
def add_produit(request):
    produit=Produit()
    if request.method == "POST":
        if request.POST.get('designation') \
            and request.POST.get('prix') \
            and request.POST.get('marque_select') :
        
            marque_id =request.POST.get('marque_select')
            produit.designation = request.POST.get('designation')
            produit.prix = request.POST.get('prix')
            produit.marque = Marque.objects.get(id_marque = marque_id)
            
            produit.save()
            return HttpResponseRedirect('home_produit')
    else:
        marques =produit.marque_choices
        return render(request,'add_produit.html/',{'marques':marques})


#view produit individually
def produit(request,produit_id):
    produit=Produit.objects.get(id_produit = produit_id)
    if produit != None:
        return render(request,'edit_produit.html',{'produit':produit})

#Edit produit 
def edit_produit(request):
    produit = Produit.objects.get(id_produit=request.POST.get('produit_id'))
    marques = Marque.objects.all()
    if request.method == 'POST':
        nouvelle_designation = request.POST.get('designation')
        nouveau_prix = request.POST.get('prix')
        nouvelle_marque_id = request.POST.get('marque_select')

    produit.designation = nouvelle_designation
    produit.prix = nouveau_prix
    produit.marque = Marque.objects.get(id_marque=nouvelle_marque_id)
    produit.save()

    context = {
        'produit': produit,
        'marques': marques,
    }

    return render(request, 'edit_produit.html', context)
            
   


#delete produit
def delete_produit(request,produit_id):
    produit = Produit.objects.get(id_produit=produit_id)
    produit.delete()
    return HttpResponseRedirect('/')

"""========================================================== COMMANDE ============================================
==================================================================================================================="""
#Home_commande
def home_commande(request):
    context={
        'clients' : Client.objects.all(),
        'marques':Marque.objects.all(),
        'produits':Produit.objects.all(),
        'commandes':Commande.objects.all(),
    }
    
    return render(request, 'home_commande.html',context)

#Addcommande
def add_commande(request):
    commande=Commande()
    if request.method == "POST":
        if request.POST.get('dateC') \
            and request.POST.get('montant') \
            and request.POST.get('client_select') :    

            commande.dateC = request.POST.get('dateC')
            commande.montant = request.POST.get('montant')
            commande.client = Client.objects.get(id=request.POST.get('client_select'))
            
            commande.save()
            return HttpResponseRedirect('home_commande')
    else:
        clients =commande.client_choices
        return render(request,'add_commande.html/',{'clients':clients})
        


#view commande individually
def commande(request,commande_id):
    commande=Commande.objects.get(id_commande = commande_id)
    if commande != None:
        return render(request,'edit_commande.html',{'commande':commande})

#Edit commande 
def edit_commande(request):
    if request.method == 'POST':
        commande = Commande.objects.get(id_commande = request.POST.get('id_commande'))
        if commande != None:

            commande.dateC = request.POST.get('dateC')
            commande.montant = request.POST.get('montant')
            commande.client = request.POST.get('client_select')
            
            commande.save()
            
            return HttpResponseRedirect('home_commande')




#delete commande
def delete_commande(request,commande_id):
    commande = Commande.objects.get(id_commande=commande_id)
    commande.delete()
    return HttpResponseRedirect('/')



"""========================================================== LIGNE COMMANDE ============================================
================================================================================================================="""


#Home_ligneCommandeommande
def home_ligneCommande(request):
    context={
        'clients' : Client.objects.all(),
        'marques':Marque.objects.all(),
        'produits':Produit.objects.all(),
        'commandes':Commande.objects.all(),
        'ligneCommande':LigneCommande.objects.all()
    }
    
    return render(request, 'home_ligneCommande.html',context)

#Addcommande
def add_ligneCommande(request):
    if request.method == "POST":
        if request.POST.get('commande') \
            and request.POST.get('produit') \
            and request.POST.get('date')  \
            and request.POST.get('prix') :

            ligneCommande=LigneCommande()
            ligneCommande.commande = request.POST.get('commande')
            ligneCommande.produit = request.POST.get('produit')
            ligneCommande.date= request.POST.get('date')
            ligneCommande.prix= request.POST.get('prix')
            ligneCommande.save()
            return HttpResponseRedirect('home_ligneCommande')
    else:
        return render(request,'add_ligneCommande.html')

#view LigneCommande individually
def ligneCommande(request,ligneCommande_id):
    ligneCommande=LigneCommande.objects.get(id_ligneCommande = ligneCommande_id)
    if ligneCommande != None:
        return render(request,'edit_ligneCommande.html',{'ligneCommande':ligneCommande})

#Edit ligneCommande 
def edit_ligneCommande(request):
    if request.method == 'POST':
        ligneCommande = LigneCommande.objects.get(id_ligneCommande = request.POST.get('id_ligneCommande'))
        if ligneCommande != None:
            ligneCommande.commande = request.POST.get('commande')
            ligneCommande.produit = request.POST.get('produit')
            ligneCommande.date = request.POST.get('date')
            ligneCommande.prix = request.POST.get('prix')
            
            ligneCommande.save()
            return HttpResponseRedirect('home_ligneCommande')

#delete ligneCommande
def delete_ligneCommande(request,ligneCommande_id):
    ligneCommande = LigneCommande.objects.get(id_ligneCommande=ligneCommande_id)
    ligneCommande.delete()
    return HttpResponseRedirect('/')

