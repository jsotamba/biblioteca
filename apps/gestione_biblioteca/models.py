from django.db import models


# Create your models here.
class Autore(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Autore'
        verbose_name_plural = 'Autori'

    def __str__(self):
        return f"{self.nome} {self.cognome}"


class Editore(models.Model):
    ragione_sociale = models.CharField(max_length=200)
    indirizzo = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = 'Editore'
        verbose_name_plural = 'Editori'

    def __str__(self):
        return self.ragione_sociale


class Libro(models.Model):
    titolo = models.CharField(max_length=200)
    autori = models.ManyToManyField(Autore)  # Un libro può avere più autori
    editore = models.ForeignKey(Editore, on_delete=models.CASCADE)
    anno_edizione = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libri'

    def __str__(self):
        return self.titolo
