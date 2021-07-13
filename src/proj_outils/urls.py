"""proj_outils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recommandation import views

urlpatterns = [
    path('admin/', admin.site.urls, name='Admin'),
    path('espace/<int:id_esp>/', views.espace_detail_view, name='Détail espace'),
    path('create/<str:id>/', views.espace_create_view, name='Création espace'),
    path('espace_edit/<int:id_esp>/', views.espace_edit_view, name='Modification espace'),
    path('login/', views.login_view, name='Connexion'),
    path('accueil/<int:id>/', views.accueil_uti_view, name='Accueil utilisateur'),
    path('delete/<int:id_esp>/', views.espace_delete_view, name='Supprimer espace'),
    path('selection_outils/<int:id_esp>/', views.selection_outils_view, name='Sélection outils'),
    path('comparaison_outils/<int:id_esp>/', views.comparaison_outils_view, name='Comparaison outils'),
    
]
