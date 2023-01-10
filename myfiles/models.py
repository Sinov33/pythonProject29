from django.db import models

# Create your models here.
class Tur(models.Model):
    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi

class Portfolio(models.Model):
    nomi = models.CharField(max_length=20)
    cleant_nomi = models.CharField(max_length=20)
    date = models.DateField()
    link = models.CharField(max_length=100)
    tur = models.ForeignKey(Tur,on_delete=models.CASCADE)
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media',null=True,blank=True)
    rasm3 = models.ImageField(upload_to='media',null=True,blank=True)
    malumot = models.TextField()
    vaqt = models.DateTimeField(auto_now=True)

class Servise(models.Model):
    nomi = models.CharField(max_length=20)
    rasm1 = models.ImageField(upload_to='media')
    malumot = models.TextField()
    vaqt = models.DateTimeField(auto_now=True)

class Team(models.Model):
    ism = models.CharField(max_length=20)
    lavozim = models.CharField(max_length=20)
    link_Twiter = models.CharField(max_length=100)
    link_Facebook = models.CharField(max_length=100)
    link_Instagram = models.CharField(max_length=100)
    link_Index = models.CharField(max_length=100)
    rasm1 = models.ImageField(upload_to='media')
    malumot = models.TextField()
    vaqt = models.DateTimeField(auto_now=True)


class Murojaat(models.Model):
    name = models.CharField(max_length=40)
    gmail = models.CharField(max_length=80)
    title = models.CharField(max_length=40)
    textt = models.TextField()
    date = models.DateField()


class Gmail(models.Model):
    gmailii = models.CharField(max_length=80)

class Portgmail(models.Model):
    gmaili = models.CharField(max_length=80)