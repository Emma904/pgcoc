from django.shortcuts import get_object_or_404, render
from .models import Espace, Agenda
from .forms import ActsPonctForm, NomEspaceForm, AgendaForm
# Create your views here.

def espace_edit_view(request, id_esp):

    if request.method == 'POST':
        instance_esp = get_object_or_404(Espace, id_espace = id_esp)
        nom_espace_form = NomEspaceForm(request.POST)
        if nom_espace_form.is_valid():
            nom_espace = nom_espace_form.cleaned_data['Nom_de_l_espace']
            instance_esp.nom_espace = nom_espace

            instance_ag = get_object_or_404(Agenda, id_espace = id_esp)
            agenda_form = AgendaForm(request.POST)
            if agenda_form.is_valid():
                lundi_matin = agenda_form.cleaned_data['Lundi_matin']
                lundi_aprem = agenda_form.cleaned_data['Lundi_après_midi']
                mardi_matin = agenda_form.cleaned_data['Mardi_matin']
                mardi_aprem = agenda_form.cleaned_data['Mardi_après_midi']
                mercredi_matin = agenda_form.cleaned_data['Mercredi_matin']
                mercredi_aprem = agenda_form.cleaned_data['Mercredi_après_midi']
                jeudi_matin = agenda_form.cleaned_data['Jeudi_matin']
                jeudi_aprem = agenda_form.cleaned_data['Jeudi_après_midi']
                vendredi_matin = agenda_form.cleaned_data['Vendredi_matin']
                vendredi_aprem = agenda_form.cleaned_data['Vendredi_après_midi']

                instance_ag.lundi_matin=lundi_matin
                instance_ag.lundi_aprem=lundi_aprem
                instance_ag.mardi_matin=mardi_matin
                instance_ag.mardi_aprem=mardi_aprem,
                instance_ag.mercredi_matin=mercredi_matin
                instance_ag.mercredi_aprem=mercredi_aprem
                instance_ag.jeudi_matin=jeudi_matin
                instance_ag.jeudi_aprem=jeudi_aprem
                instance_ag.vendredi_matin=vendredi_matin
                instance_ag.vendredi_aprem=vendredi_aprem
            
                acts_ponct_form = ActsPonctForm(request.POST)
                if acts_ponct_form.is_valid():
                    acts_ponct = acts_ponct_form.cleaned_data['Activités_ponctuelles']
                    instance_esp.acts_ponct = acts_ponct
                    instance_esp.save()
                    instance_ag.save()
                    
    else:
          nom_espace_form = NomEspaceForm()    
          agenda_form = AgendaForm()
          acts_ponct_form = ActsPonctForm()

    context = { 'nom_espace_form': nom_espace_form, 'agenda_form': agenda_form, 'acts_ponct_form': acts_ponct_form}
    return render(request, 'recommandation/espace_edit.html', context)



def espace_create_view(request):

    if request.method == 'POST':
        nom_espace_form = NomEspaceForm(request.POST)
        if nom_espace_form.is_valid():
            nom_espace = nom_espace_form.cleaned_data['Nom_de_l_espace']
            e = Espace(nom_espace=nom_espace)

            agenda_form = AgendaForm(request.POST)
            if agenda_form.is_valid():
                lundi_matin = agenda_form.cleaned_data['Lundi_matin']
                lundi_aprem = agenda_form.cleaned_data['Lundi_après_midi']
                mardi_matin = agenda_form.cleaned_data['Mardi_matin']
                mardi_aprem = agenda_form.cleaned_data['Mardi_après_midi']
                mercredi_matin = agenda_form.cleaned_data['Mercredi_matin']
                mercredi_aprem = agenda_form.cleaned_data['Mercredi_après_midi']
                jeudi_matin = agenda_form.cleaned_data['Jeudi_matin']
                jeudi_aprem = agenda_form.cleaned_data['Jeudi_après_midi']
                vendredi_matin = agenda_form.cleaned_data['Vendredi_matin']
                vendredi_aprem = agenda_form.cleaned_data['Vendredi_après_midi']
                a = Agenda(lundi_matin=lundi_matin, lundi_aprem=lundi_aprem, mardi_matin=mardi_matin, mardi_aprem=mardi_aprem,
                mercredi_matin=mercredi_matin, mercredi_aprem=mercredi_aprem, jeudi_matin=jeudi_matin, jeudi_aprem=jeudi_aprem,
                vendredi_matin=vendredi_matin, vendredi_aprem=vendredi_aprem)
                e.save()
                a.save()

                instance_esp = get_object_or_404(Espace, id_espace = e.id_espace)
                acts_ponct_form = ActsPonctForm(request.POST)
                if acts_ponct_form.is_valid():
                    acts_ponct = acts_ponct_form.cleaned_data['Activités_ponctuelles']
                    instance_esp.acts_ponct = acts_ponct
                    instance_esp.save()
                    
    else:
          nom_espace_form = NomEspaceForm()    
          agenda_form = AgendaForm()
          acts_ponct_form = ActsPonctForm()

    context = { 'nom_espace_form': nom_espace_form, 'agenda_form': agenda_form, 'acts_ponct_form': acts_ponct_form}
    return render(request, 'recommandation/espace_create.html', context)



def espace_detail_view(request,id_esp):
    
    esp = Espace.objects.get(id_espace = id_esp)
    ag = Agenda.objects.get(id_espace = id_esp)

    context = { 'esp': esp,  'ag': ag }
    return render(request, 'recommandation/espace_detail.html', context)
