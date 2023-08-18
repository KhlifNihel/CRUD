from django import forms
from .models import *




class Marqueform(forms.ModelForm):
    class Meta:
        model =Marque
        
        fields = '__all__'
   
        widgets = {
            'designation': forms.TextInput(attrs={'class': 'form-control','name':'designation','maxlength':'40','placeholder':'designation de la marque'}),
            }



class Clientform(forms.ModelForm):
    class Meta:
        model =Client
        
        fields = '__all__'
   
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control','name':'nom','maxlength':'40','placeholder':'nom client'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control','name':'adresse','maxlength':'40','placeholder':'adresse du client'}),
            'telephone': forms.Select(attrs={'class': 'form-select','name':'telephone','maxlength':'40','placeholder':'telephone du client'}),
            }

class Produitform(forms.ModelForm):
    class Meta:
        model =Produit
        
        fields = '__all__'
   
        widgets = {
            'designation': forms.TextInput(attrs={'class': 'form-control','name':'designation','maxlength':'40','placeholder':'designation produit'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control','name':'prix','maxlength':'40','placeholder':'prix produit'}),
            'marque': forms.Select(attrs={'class': 'form-select','name':'marque','maxlength':'40','placeholder':'marque produit'}),
            }


class Commandeform(forms.ModelForm):
    class Meta:
        model =Commande
        
        fields = '__all__'
   
        widgets = {
            'dateC': forms.DateInput(attrs={'class': 'form-control','name':'dateC','maxlength':'40','placeholder':'dateC produit'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control','name':'montant','maxlength':'40','placeholder':'montant produit'}),
            'client': forms.Select(attrs={'class': 'form-select','name':'client','maxlength':'40','placeholder':'client_commande'}),
            }

class ligneCommandeform(forms.ModelForm):
    class Meta:
        model =LigneCommande    
        fields = '__all__'
   
        widgets = {
            'commande': forms.Select(attrs={'class': 'form-control','name':'commande','maxlength':'40','placeholder':'commande'}),
            'produit': forms.Select(attrs={'class': 'form-control','name':'produit','maxlength':'40','placeholder':' produit'}),
            'date': forms.DateInput(attrs={'class': 'form-select','name':'date ','maxlength':'40','placeholder':'date'}),
            'prix': forms.NumberInput(attrs={'class': 'form-select','name':'prix','maxlength':'40','placeholder':'prix'}),
            
            }
