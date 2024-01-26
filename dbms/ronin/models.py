from django.db import models

# Create your models here.
class dropdown(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class cricket(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    year  = models.IntegerField()


    
    class Meta:
        managed= False
        db_table = 'cricket'

class kabadi(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    year  = models.IntegerField()


    class Meta:
        managed= False
        db_table = 'kabadi'

class football(models.Model): 
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    year  = models.IntegerField()


    class Meta:
        managed= False
        db_table = 'football'

class basketball(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    year  = models.IntegerField()
 

    class Meta:
        managed= False
        db_table = 'basketball'

class khokho(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    year  = models.IntegerField()

    class Meta:
        managed= False
        db_table = 'khokho'

class all_students_info(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    year = models.IntegerField()
    sports_tag =models.CharField(max_length=20)
    
    class Meta:
        managed= False
        db_table = 'all_student_info'
    
    
