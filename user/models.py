
from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid

class Profil(models.Model):
    id = models.UUIDField(primary_key = True, default= uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isim = models.CharField(max_length = 100)
    resim = models.FileField(upload_to = 'profiller/')

    slug = models.SlugField(null=True,blank = True, editable= False)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.isim)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.isim


class Hesap(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    resim = models.FileField(upload_to = 'hesaplar')
    tel = models.IntegerField()

    def __str__(self):
        return self.user.username