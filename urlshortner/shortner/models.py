from django.db import models

# Create your models here. creating database name as Url and they have two columns link and uuid
class Url(models.Model):
    link = models.CharField(max_length=10000)    #some links are very long and link is used for link we have to shorten
    uuid = models.CharField(max_length=10)       #uuid is for specific is id to pass that link
