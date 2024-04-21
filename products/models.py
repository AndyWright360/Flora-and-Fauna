from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendy_name = models.CharField(max_length=254, null=True, black=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name

