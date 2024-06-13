from django.db import models

class Item(models.Model):

    def __str__(self):
        return f"{self.item_name}: {self.item_desc} :${self.item_price}"
    
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=200, default = "https://fakeimg.pl/600x400")
