from django.db import models

# Create your models here.

class Predict(models.Model):
    pregnancies = models.IntegerField()
    glucose = models.IntegerField()
    blood_pressure  = models.IntegerField()
    skin_thickess = models.IntegerField()
    insulin = models.IntegerField()
    bmi = models.FloatField()
    diabetes_pedigree_function = models.FloatField()
    age = models.PositiveIntegerField()
    result = models.TextField(max_length=100)

