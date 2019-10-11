from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()

class Tree(models.Model):
    ID = models.IntegerField()
    PID = models.IntegerField()
    Name = models.CharField(max_length=80)
    Layer = models.IntegerField()

class XT(models.Model):
    ID = models.IntegerField()
    Name = models.CharField(max_length=80)

class FXT(models.Model):
    ID = models.IntegerField()
    Name = models.CharField(max_length=80)
    Update_time = models.DateTimeField()
    temp1 = models.CharField(max_length=200)
    temp2 = models.CharField(max_length=200)

class ZXT(models.Model):
    ID = models.IntegerField()
    Name = models.CharField(max_length=80)

class DJ(models.Model):
    ID = models.IntegerField()
    Name = models.CharField(max_length=80)

class BZJ(models.Model):
    ID = models.IntegerField()
    Name = models.CharField(max_length=80)

class PTB(models.Model):
    ID = models.IntegerField()
    NO = models.CharField(max_length=80)
    NAME = models.CharField(max_length=80)
    NUM = models.IntegerField()
    DESIGNER = models.CharField(max_length=80)
    PRODUCER = models.CharField(max_length=80)
