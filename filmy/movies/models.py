from django.db import models
 
# Create your models here.
 
class Film(models.Model):
    nazev = models.CharField(max_length=200)
    rok = models.IntegerField()
    reziser = models.ForeignKey('Director', on_delete=models.CASCADE, related_name="filmy")
    zanr = models.CharField(max_length=100)
    hodnoceni = models.FloatField()
    obrazek = models.ImageField(null=True, blank=True, upload_to="images/")
 
    def __str__(self):
        return f"{self.nazev} ({self.rok})"
   
class Director(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    rok_narozeni = models.IntegerField()
 
    def __str__(self):
        return f'{self.jmeno} {self.prijmeni} ({self.rok_narozeni})'
 