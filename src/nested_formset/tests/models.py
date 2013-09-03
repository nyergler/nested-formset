from django.db import models


class Block(models.Model):
    description = models.CharField(max_length=255)

class Building(models.Model):
    block = models.ForeignKey(Block)
    address = models.CharField(max_length=255)

class Tenant(models.Model):
    building = models.ForeignKey(Building)
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
