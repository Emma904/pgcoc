from django.contrib import admin
from .models import Espace, Agenda, Activite, Fonctionnalitebesoin, Outil, Utilisateur

# Register your models here.

admin.site.register(Espace)
admin.site.register(Agenda)
admin.site.register(Activite)
admin.site.register(Fonctionnalitebesoin)
admin.site.register(Outil)
admin.site.register(Utilisateur)