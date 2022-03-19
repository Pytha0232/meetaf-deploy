from django.db import models

# Create your models here.

class LocalisationForage(models.Model):

    # Création des différents champs

    nom = models.CharField(max_length=255) 
    telephone = models.CharField(max_length=255)
    localisation = models.TextField()
    email = models.EmailField(max_length=254)


    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'LocalisationForage'
        verbose_name_plural = 'LocalisationForages'

    def __str__(self):
        return self.nom

class EtatEau(models.Model):

    # Création des différents champs
    CHOIX = [
    ('P', 'POTABLE'),
    ('D', 'DANGE'),
    ]
    choix = models.CharField(max_length=20, choices=CHOIX, default=None,blank=True, null=True)


    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'EtatEau'
        verbose_name_plural = 'EtatEau'

    def __str__(self):
        return self.choix