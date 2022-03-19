from django.db import models

# Create your models here.

class Information(models.Model):

    # Création des différents champs

    nom = models.CharField(max_length=255) # Zone d’édition de texte monoline
    ville = models.CharField(max_length=255)
    commune = models.CharField(max_length=255)
    secteur = models.CharField(max_length=255)
    duree = models.DurationField()
    # Attributs obligatoires (Convention de NaN)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Information'
        verbose_name_plural = 'Information'

    def __str__(self):
        return self.nom
