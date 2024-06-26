from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Item(models.Model):

    def __str__(self):
        return f"{self.item_name}: {self.item_desc} :${self.item_price}"
    
    user_name = models.ForeignKey(User, on_delete= models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=200, default = "https://fakeimg.pl/600x400")

    def get_absolute_url(self):
        return reverse('menu:detail', kwargs={ 'pk' : self.pk })