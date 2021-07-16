from django.db import models

# Create your models here.

class Espace(models.Model):
    id_espace = models.AutoField(primary_key=True)
    nom_espace = models.TextField()
    acts_ponct = models.JSONField(default=list, blank=True, null=True)
    outils_utilisés = models.JSONField(default=list, blank=True, null=True)
    outils_recommandés = models.JSONField(default=list, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Espace'

class Agenda(models.Model):
    id_espace = models.AutoField(primary_key=True)
    lundi_matin = models.JSONField(default=list, blank=True, null=True)
    lundi_aprem = models.JSONField(default=list, blank=True, null=True)
    mardi_matin = models.JSONField(default=list, blank=True, null=True)
    mardi_aprem = models.JSONField(default=list, blank=True, null=True)
    mercredi_matin = models.JSONField(default=list, blank=True, null=True)
    mercredi_aprem = models.JSONField(default=list, blank=True, null=True)
    jeudi_matin = models.JSONField(default=list, blank=True, null=True)
    jeudi_aprem = models.JSONField(default=list, blank=True, null=True)
    vendredi_matin = models.JSONField(default=list, blank=True, null=True)
    vendredi_aprem = models.JSONField(default=list, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Agenda'


class Activite(models.Model):
    id = models.BigAutoField(primary_key=True)
    activite = models.TextField()
    besoins = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Activite'


class Fonctionnalitebesoin(models.Model):
    id = models.BigAutoField(primary_key=True)
    fonctionnalite = models.TextField()
    besoin = models.TextField()

    class Meta:
        managed = False
        db_table = 'FonctionnaliteBesoin'


class Outil(models.Model):
    id = models.BigAutoField(primary_key=True)
    outil = models.TextField()
    categorie = models.TextField()
    fonctionnalites = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Outil'


class Utilisateur(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    admin_bool = models.IntegerField(default=0, blank=True, null=True)
    ids_espaces = models.JSONField(default=list, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Utilisateur'