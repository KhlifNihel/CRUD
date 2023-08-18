from django.db import models
import datetime

class Client(models.Model):
    id=models.IntegerField(primary_key=True)
    nom=models.CharField(max_length=50,null=True,blank=True)
    adresse=models.CharField(max_length=50,null=True,blank=True)
    telephone=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self) -> str:
        return self.nom
    
class Marque(models.Model):
    id_marque=models.IntegerField(primary_key=True)
    designation=models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.designation
    

class Produit(models.Model):
    id_produit=models.IntegerField(primary_key=True)
    designation=models.CharField(max_length=50,null=True,blank=True)
    prix=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    marque=models.ForeignKey(Marque,on_delete=models.PROTECT,null=True,blank=True)

    def __str__(self):
        return self.designation
    
    def marque_choices(self):
        marques = Marque.objects.all().values_list('id_marque', 'designation')
        return marques


class Commande(models.Model):
    id_commande = models.IntegerField(primary_key=True)
    dateC = models.DateField(default=datetime.date.today)
    montant = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    client = models.ForeignKey(Client,on_delete=models.PROTECT,null=True,blank=True)

    def __str__(self):
        return str(self.id_commande)
    
    def client_choices(self):
        clients = Client.objects.all().values_list('id', 'nom')
        return clients


class LigneCommande(models.Model):
    id_ligneCommande=models.IntegerField(primary_key=True)
    commande=models.ForeignKey(Commande,on_delete=models.PROTECT,null=True,blank=True)
    produit=models.ForeignKey(Produit,on_delete=models.PROTECT,null=True,blank=True)
    date=models.DateField(default=datetime.date.today)
    prix=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    
    def __str__(self):
        return str(self.id_ligneCommande)