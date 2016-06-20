from __future__ import unicode_literals
from django.db import models

class Favorites(models.Model):
    #owner = user.username
    owner = "test"
    favs = models.CharField(max_length=200) #List of symbol names
    def __str__(self):
        return (self.owner + "'s favorites")
