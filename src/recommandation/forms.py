from django import forms
from .models import Activite, Outil

class NomEspaceForm(forms.Form):

    Nom_de_l_espace = forms.CharField(max_length=100)


class AgendaForm(forms.Form):

    global l_acts
    l_acts = list(dict.fromkeys(list(map(lambda a: a.activite, Activite.objects.all()))))
    l_choices = [(l_acts[i],l_acts[i]) for i in range(len(l_acts))]
    
    CHOICES = tuple(l_choices)
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
    global l_acts
    l_acts = list(dict.fromkeys(list(map(lambda a: a.activite, Activite.objects.all()))))
    l_choices = [(l_acts[i],l_acts[i]) for i in range(len(l_acts))]

    CHOICES = tuple(l_choices)
    Activités_ponctuelles = forms.MultipleChoiceField(required=False, choices=CHOICES, widget=forms.CheckboxSelectMultiple())


class OutilsUtiForm(forms.Form):
    global l_outils
    l_outils = list(dict.fromkeys(list(map(lambda a: a.outil, Outil.objects.all()))))
    l_choices = [(l_outils[i],l_outils[i]) for i in range(len(l_outils))]

    CHOICES = tuple(l_choices)
    Outils_utilisés = forms.MultipleChoiceField(required=False, choices=CHOICES, widget=forms.CheckboxSelectMultiple)