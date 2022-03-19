from django.db import models

# Create your models here.


class Probleme(models.Model):

    # Création des différents champs

    nom_prenom = models.CharField(max_length=255) # Zone d’édition de texte monoline
    localisation = models.CharField(max_length=255)
    description = models.TextField()
    resolu = models.BooleanField(default=True)

    

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Probleme'
        verbose_name_plural = 'Problemes'

    def __str__(self):
        return self.nom_prenom
