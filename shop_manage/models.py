from django.db import models
 
class Pens(models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    price =  models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    sub = models.CharField(max_length=255)

class Erasers(models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    price =  models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    sub = models.CharField(max_length=255)    

class Arts(models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    price =  models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    sub = models.CharField(max_length=255)

class Diys(models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    price =  models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    sub = models.CharField(max_length=255)





