from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from .models import Espace, Agenda, Utilisateur, Outil, Activite, Fonctionnalitebesoin
from .forms import ActsPonctForm, NomEspaceForm, AgendaForm, OutilsUtiForm, LoginForm, DeuxOutilsForm
# Create your views here.



#LOGIN
def login_view(request): #pas une vraie authentification, voir si il faut changer ça
    
    if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                idep = login_form.cleaned_data['IDEP']
                uti_bdd = list(Utilisateur.objects.filter(id=idep))
                print(uti_bdd)
                if uti_bdd == []:
                    u = Utilisateur(id=idep)
                    u.save()
                return redirect('Accueil utilisateur', id=idep)      

    else:
        login_form = LoginForm() 

    return render(request, 'login.html', { 'login_form': login_form })



#ACCUEIL UTILISATEUR
def accueil_uti_view(request, id):
    
    utilisateur = Utilisateur.objects.get(id=id)
    if utilisateur.ids_espaces is not None:
        espaces = Espace.objects.filter(id_espace__in = utilisateur.ids_espaces)
        
    else:
        espaces = None

    context = { 'uti': utilisateur, 'esps': espaces }
    return render(request, 'utilisateur_accueil.html', context)



#CHOIX TYPE CREATION ESPACE
def choix_ini_view(request, id):
    utilisateur = Utilisateur.objects.get(id=id)   

    return render(request, 'choix.html', {'uti': utilisateur })  



#CREATION ESPACE SIMPLE
def espace_create_bis_view(request, id):
    
    if request.method == 'POST':
        nom_espace_form = NomEspaceForm(request.POST)
        if nom_espace_form.is_valid():
                nom_espace = nom_espace_form.cleaned_data['Nom_de_l_espace']
                a = Agenda(lundi_matin=[], lundi_aprem=[], mardi_matin=[], mardi_aprem=[], mercredi_matin=[], 
                mercredi_aprem=[], jeudi_matin=[], jeudi_aprem=[], vendredi_matin=[], vendredi_aprem=[])
                acts_ponct_form = ActsPonctForm(request.POST)
                if acts_ponct_form.is_valid():
                    acts_pct = acts_ponct_form.cleaned_data['Activités_ponctuelles']

                    e = Espace(nom_espace=nom_espace, acts_ponct = acts_pct)
                    e.save()
                    a.save()
                    uti = Utilisateur.objects.get(id=id)
                    uti.ids_espaces.append(e.id_espace)
                    uti.save()

                    return redirect('Recommandation', id_esp = e.id_espace)
                        
    else:
        nom_espace_form = NomEspaceForm()    
        acts_ponct_form = ActsPonctForm()
    
    context = { 'nom_espace_form': nom_espace_form, 'acts_ponct_form': acts_ponct_form}
    return render(request, 'create_simple.html', context)



#CREATION ESPACE AGENDA
def espace_create_view(request, id):

    if request.method == 'POST':
            nom_espace_form = NomEspaceForm(request.POST)
            if nom_espace_form.is_valid():
                nom_espace = nom_espace_form.cleaned_data['Nom_de_l_espace']

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
                    
                    acts_ponct_form = ActsPonctForm(request.POST)
                    if acts_ponct_form.is_valid():
                        acts_pct = acts_ponct_form.cleaned_data['Activités_ponctuelles']

                        e = Espace(nom_espace=nom_espace, acts_ponct = acts_pct)
                        e.save()
                        a.save()
                        uti = Utilisateur.objects.get(id=id)
                        uti.ids_espaces.append(e.id_espace)
                        uti.save()

                        return redirect('Recommandation', id_esp = e.id_espace)
                        
    else:
        nom_espace_form = NomEspaceForm()    
        agenda_form = AgendaForm()
        acts_ponct_form = ActsPonctForm()
    
    context = { 'nom_espace_form': nom_espace_form, 'agenda_form': agenda_form, 'acts_ponct_form': acts_ponct_form}
    return render(request, 'espace_create.html', context)


#CHOIX MODIF ESPACE
def choix_edit_view(request, id_esp):  

    return render(request, 'choix_edit.html', {'id_esp': id_esp})  


#MODIFICATION ESPACE SIMPLE
def espace_edit_bis_view(request, id_esp):

    instance_esp = get_object_or_404(Espace, id_espace = id_esp)
    instance_ag = get_object_or_404(Agenda, id_espace = id_esp)
    
    if request.method == 'POST':
        nom_espace_form = NomEspaceForm(request.POST)
        if nom_espace_form.is_valid():
            nom_espace = nom_espace_form.cleaned_data['Nom_de_l_espace']
            instance_esp.nom_espace = nom_espace

            instance_ag.lundi_matin=[]
            instance_ag.lundi_aprem=[]
            instance_ag.mardi_matin=[]
            instance_ag.mardi_aprem=[]
            instance_ag.mercredi_matin=[]
            instance_ag.mercredi_aprem=[]
            instance_ag.jeudi_matin=[]
            instance_ag.jeudi_aprem=[]
            instance_ag.vendredi_matin=[]
            instance_ag.vendredi_aprem=[]
            
            acts_ponct_form = ActsPonctForm(request.POST)
            if acts_ponct_form.is_valid():
                acts_ponct = acts_ponct_form.cleaned_data['Activités_ponctuelles']
                instance_esp.acts_ponct = acts_ponct
                instance_esp.save()
                instance_ag.save()
                print(instance_esp.acts_ponct)
                return redirect('Recommandation', id_esp = instance_esp.id_espace)
            
    else:
          nom_espace_form = NomEspaceForm(initial={'Nom_de_l_espace': instance_esp.nom_espace})    
          
          acts_ponct_form = ActsPonctForm(initial={'Activités_ponctuelles': instance_esp.acts_ponct})

    context = { 'nom_espace_form': nom_espace_form, 'acts_ponct_form': acts_ponct_form}
    return render(request, 'edit_simple.html', context)



#MODIFICATION ESPACE AGENDA
def espace_edit_view(request, id_esp):

    instance_esp = get_object_or_404(Espace, id_espace = id_esp)
    instance_ag = get_object_or_404(Agenda, id_espace = id_esp)
    
    if request.method == 'POST':
        nom_espace_form = NomEspaceForm(request.POST)
        if nom_espace_form.is_valid():
            nom_espace = nom_espace_form.cleaned_data['Nom_de_l_espace']
            instance_esp.nom_espace = nom_espace

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
                instance_ag.mardi_aprem=mardi_aprem
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
                    print(instance_esp.acts_ponct)
                    return redirect('Recommandation', id_esp = instance_esp.id_espace)
                    

    else:
          nom_espace_form = NomEspaceForm(initial={'Nom_de_l_espace': instance_esp.nom_espace})    
          agenda_form = AgendaForm(initial={'Lundi matin': instance_ag.lundi_matin, 'Lundi après-midi': instance_ag.lundi_aprem,
          'Mardi matin': instance_ag.mardi_matin, 'Mardi après-midi': instance_ag.mardi_aprem,
          'Mercredi matin': instance_ag.mercredi_matin, 'Mercredi après-midi': instance_ag.mercredi_aprem,
          'Jeudi matin': instance_ag.jeudi_matin, 'Jeudi après-midi': instance_ag.jeudi_aprem,
          'Vendredi matin': instance_ag.vendredi_matin, 'Vendredi après-midi': instance_ag.vendredi_aprem})
          acts_ponct_form = ActsPonctForm(initial={'Activités ponctuelles': instance_esp.acts_ponct})

    context = { 'nom_espace_form': nom_espace_form, 'agenda_form': agenda_form, 'acts_ponct_form': acts_ponct_form}
    return render(request, 'espace_edit.html', context)



#SUPRESSION ESPACE
def espace_delete_view(request, id_esp):

    esp = get_object_or_404(Espace, id_espace = id_esp) 
    ag = get_object_or_404(Agenda, id_espace = id_esp)
    uti = Utilisateur.objects.filter(ids_espaces__icontains = esp.id_espace).first()
    
    if request.method == 'POST':      
        esp.delete()
        ag.delete()
        uti.ids_espaces.remove(id_esp)
        uti.save()        
        return redirect('Accueil utilisateur', id=uti.id)
    return render(request, 'espace_delete.html')



#ACCUEIL ESPACE
def espace_detail_view(request,id_esp):
    
    esp = Espace.objects.get(id_espace = id_esp)
    ag = Agenda.objects.get(id_espace = id_esp)
    uti = Utilisateur.objects.filter(ids_espaces__icontains = esp.id_espace).first()
    l = ['lundi_matin', 'lundi_aprem', 'mardi_matin', 'mardi_aprem','mercredi_matin', 'mercredi_aprem',
    'jeudi_matin', 'jeudi_aprem','vendredi_matin', 'vendredi_aprem']
    ag_bool = False
    for dj in l:
        if getattr(ag, dj) != []:
            ag_bool = True
    context = { 'esp': esp,  'ag': ag, 'uti': uti, 'ag_bool': ag_bool }
    return render(request, 'espace_detail.html', context)



#RECOMMANDATION OUTILS
def recommandation_outils_views(request, id_esp):

    esp = Espace.objects.get(id_espace=id_esp)
    ag = Agenda.objects.get(id_espace=id_esp)

    acts = []
    l = ['lundi_matin', 'lundi_aprem', 'mardi_matin', 'mardi_aprem','mercredi_matin', 'mercredi_aprem',
    'jeudi_matin', 'jeudi_aprem','vendredi_matin', 'vendredi_aprem']
    for demij in l:
        for act in getattr(ag, demij):
            if not act in acts:
                acts.append(act)
    acts_pct = getattr(esp, 'acts_ponct').copy()
    for act_pct in acts_pct:
        if act_pct in acts:
            acts_pct.remove(act_pct)
    
    #activités -> besoin
    activites_obj = Activite.objects.filter(activite__in = acts)
    besoins_doublons = list(map(lambda x: x.besoins, activites_obj))
    besoins = list(dict.fromkeys(besoins_doublons))

    activites_ponct_obj = Activite.objects.filter(activite__in = acts_pct)
    besoins_pct_doublons = list(map(lambda x: x.besoins, activites_ponct_obj))
    besoins_pct = list(dict.fromkeys(besoins_pct_doublons))
    for bes_pct in besoins_pct:
        if bes_pct in besoins:
            besoins_pct.remove(bes_pct)
    
    #besoins -> fonctionnalités
    foncsbes = Fonctionnalitebesoin.objects.filter(besoin__in = besoins)
    foncs_doublons = list(map(lambda x: x.fonctionnalite, foncsbes))
    foncs = list(dict.fromkeys(foncs_doublons))

    foncsbes_pct = Fonctionnalitebesoin.objects.filter(besoin__in = besoins_pct)
    foncs_pct_doublons = list(map(lambda x: x.fonctionnalite, foncsbes_pct))
    foncs_pct = list(dict.fromkeys(foncs_pct_doublons))
    for fonc_pct in foncs_pct:
        if fonc_pct in foncs:
            foncs_pct.remove(fonc_pct)
    fonctions = foncs + foncs_pct
    
    #fonctionnalités -> outils
    d = {}
    l_outils = list(dict.fromkeys(list(map(lambda x : x.outil, list(Outil.objects.all())))))
    for nom_outil in l_outils:
        d[nom_outil] = [getattr(Outil.objects.filter(outil=nom_outil).first(), 'categorie')]
        d[nom_outil] += list(map(lambda x: getattr(x,'fonctionnalites'),(list(Outil.objects.filter(outil=nom_outil)))))

    liste_outils=[]
    while fonctions != []:
        out = None
        correspondance = 0
        d_commun = {}
        for nom_outil in d.keys():
            d_commun[nom_outil]=[]
            for fonc in fonctions:
                if fonc in d[nom_outil]:
                    d_commun[nom_outil].append(fonc)
            if len(d_commun[nom_outil])> correspondance:
                correspondance = len(d_commun[nom_outil])
                out = nom_outil
            
        if out is not None:
            for fonc in d_commun[out]:
                fonctions.remove(fonc) 
            liste_outils.append(out)
        else:
            break  
       
    esp.outils_recommandés= liste_outils
    esp.save()

    context = {'esp': esp}
    return render(request, 'recommandation_outils.html', context)



#SELECTION OUTILS UTILISES
def selection_outils_view(request, id_esp):
    
    e = Espace.objects.get(id_espace=id_esp)

    if request.method == 'POST':
            outils_uti_form = OutilsUtiForm(request.POST)
            if outils_uti_form.is_valid():
                outils_uti = outils_uti_form.cleaned_data['Outils_utilisés']
                e.outils_utilisés = outils_uti
                e.save()
                return redirect('Comparaison outils', id_esp = e.id_espace)
    else:
          outils_uti_form = OutilsUtiForm()

    context = { 'outils_uti_form': outils_uti_form, 'esp': e }
    return render(request, 'selection_outils.html', context)



#COMPARAISON OUTILS
def comparaison_outils_view(request, id_esp):

    esp = Espace.objects.get(id_espace=id_esp)
    outilsuti = esp.outils_utilisés

    if outilsuti == []:
        return redirect('Sélection outils', id_esp=esp.id_espace)
        
    else:

        ag = Agenda.objects.get(id_espace=id_esp)

        acts = []
        l = ['lundi_matin', 'lundi_aprem', 'mardi_matin', 'mardi_aprem','mercredi_matin', 'mercredi_aprem',
        'jeudi_matin', 'jeudi_aprem','vendredi_matin', 'vendredi_aprem']
        for demij in l:
            for act in getattr(ag, demij):
                if not act in acts:
                    acts.append(act)
        acts_pct = getattr(esp, 'acts_ponct').copy()
        for act_pct in acts_pct:
            if act_pct in acts:
                acts_pct.remove(act_pct)
        
        #activités -> besoin
        activites_obj = Activite.objects.filter(activite__in = acts)
        besoins_doublons = list(map(lambda x: x.besoins, activites_obj))
        besoins = list(dict.fromkeys(besoins_doublons))

        activites_ponct_obj = Activite.objects.filter(activite__in = acts_pct)
        besoins_pct_doublons = list(map(lambda x: x.besoins, activites_ponct_obj))
        besoins_pct = list(dict.fromkeys(besoins_pct_doublons))
        for bes_pct in besoins_pct:
            if bes_pct in besoins:
                besoins_pct.remove(bes_pct)
        
        #besoins -> fonctionnalités
        foncsbes = Fonctionnalitebesoin.objects.filter(besoin__in = besoins)
        foncs_doublons = list(map(lambda x: x.fonctionnalite, foncsbes))
        foncs = list(dict.fromkeys(foncs_doublons))

        foncsbes_pct = Fonctionnalitebesoin.objects.filter(besoin__in = besoins_pct)
        foncs_pct_doublons = list(map(lambda x: x.fonctionnalite, foncsbes_pct))
        foncs_pct = list(dict.fromkeys(foncs_pct_doublons))
        for fonc_pct in foncs_pct:
            if fonc_pct in foncs:
                foncs_pct.remove(fonc_pct)
        fonctions = foncs + foncs_pct    

        liste_finale_uti = [] #liste de ['outil','catégorie', 'fonctionnalités']
        outilsuti = esp.outils_utilisés
        for outiluti in outilsuti:
            liste_ini = list(Outil.objects.filter(outil=outiluti))
            l_nom_cat = liste_ini[0]
            foncs = list(dict.fromkeys(list(map(lambda a: a.fonctionnalites, liste_ini))))
            liste_finale_uti.append([l_nom_cat.outil, l_nom_cat.categorie, foncs])

        liste_finale_rec = [] #liste de ['outil','catégorie', 'fonctionnalités']
        outilsrec = esp.outils_recommandés
        for outilrec in outilsrec:
            liste_ini = list(Outil.objects.filter(outil=outilrec))
            l_nom_cat = liste_ini[0]
            foncs = list(dict.fromkeys(list(map(lambda a: a.fonctionnalites, liste_ini))))
            liste_finale_rec.append([l_nom_cat.outil, l_nom_cat.categorie, foncs])

        l_foncs_rec = []
        for outil_rec in liste_finale_rec:
            if outil_rec[1] not in l_foncs_rec:
                l_foncs_rec.append(outil_rec[1])
            for fonc in outil_rec[2]:
                if fonc not in l_foncs_rec:
                    l_foncs_rec.append(fonc)
        l_foncs_uti = []
        for outil_uti in liste_finale_uti:
            if outil_uti[1] not in l_foncs_uti:
                l_foncs_uti.append(outil_uti[1])
            for fonc in outil_uti[2]:
                if fonc not in l_foncs_uti:
                    l_foncs_uti.append(fonc)

        foncs_manquantes = []
        for fonc in fonctions:
            if  fonc in l_foncs_rec and fonc not in l_foncs_uti and fonc not in foncs_manquantes:
                        foncs_manquantes.append(fonc)

    context = { 'outils_uti': liste_finale_uti, 'outils_rec': liste_finale_rec, 'esp': esp, 'f_manq': foncs_manquantes }
    return render(request, 'comparaison_outils.html', context)


#SELECTION DE DEUX OUTILS POUR UNE SIMPLE COMPARAISON DES FONCTIONNALITES
def selection_deux_outils_view(request):
    
    if request.method == 'POST':

            deux_outils_form = DeuxOutilsForm(request.POST)
            if deux_outils_form.is_valid():
                nom_outil_1 = deux_outils_form.cleaned_data['Outil_1'][0]
                nom_outil_2 = deux_outils_form.cleaned_data['Outil_2'][0]
                
                return redirect('Comparaison simple', outil1=nom_outil_1, outil2=nom_outil_2)
    else:
          deux_outils_form = DeuxOutilsForm()

    context = { 'deux_outils_form': deux_outils_form }
    return render(request, 'selection_deux_outils.html', context)


#SIMPLE COMPARAISON DES FONCTIONNALITES DE DEUX OUTILS
def comparaison_simple_view(request, outil1, outil2):

    ini_1 = list(Outil.objects.filter(outil=outil1))
    nom_cat_1 = ini_1[0]
    foncs_1 = list(dict.fromkeys(list(map(lambda a: a.fonctionnalites, ini_1))))
    outil_1 = [nom_cat_1.outil, nom_cat_1.categorie, foncs_1]

    ini_2 = list(Outil.objects.filter(outil=outil2))
    nom_cat_2 = ini_2[0]
    foncs_2 = list(dict.fromkeys(list(map(lambda a: a.fonctionnalites, ini_2))))
    outil_2 = [nom_cat_2.outil, nom_cat_2.categorie, foncs_2]

    nom1, nom2 = outil_1[0], outil_2[0]
    manq1 = []
    for f2 in [outil_2[1]] + foncs_2:
        if f2 not in foncs_1:
            manq1.append(f2)
    manq2 = []
    for f1 in [outil_1[1]] + foncs_1:
        if f1 not in foncs_2:
            manq2.append(f1)

    context = {'outil1': outil_1, 'outil2': outil_2, 'nom1': nom1, 'nom2': nom2, 'manq1': manq1, 'manq2': manq2}
    return render(request, 'comparaison_simple.html', context)