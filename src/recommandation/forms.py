from django import forms

from recommandation.models import Utilisateur

class NomEspaceForm(forms.Form):
    Nom_de_l_espace = forms.CharField(max_length=100)

class AgendaForm(forms.Form):

    CHOICES = (('a','a'),('b','b'),('c','c')) #à remplacer par la liste des activités
    Lundi_matin = forms.MultipleChoiceField(required=False, choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    Lundi_après_midi = forms.MultipleChoiceField(required=False, choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    Mardi_matin = forms.MultipleChoiceField(required=False, choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    Mardi_après_midi = forms.MultipleChoiceField(required=False, choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    Mercredi_matin = forms.MultipleChoiceField(required=False, choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    Mercredi_après_midi = forms.MultipleChoiceField(required=False, choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    Jeudi_matin = forms.MultipleChoiceField(required=False, choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    Jeudi_après_midi = forms.MultipleChoiceField(required=False, choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    Vendredi_matin = forms.MultipleChoiceField(required=False, choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    Vendredi_après_midi = forms.MultipleChoiceField(required=False, choices=CHOICES, widget=forms.CheckboxSelectMultiple())

class ActsPonctForm(forms.Form):
    CHOICES = (('a','a'),('b','b')) #à remplacer par la liste des activités
    Activités_ponctuelles = forms.MultipleChoiceField(required=False, choices=CHOICES, widget=forms.CheckboxSelectMultiple())
