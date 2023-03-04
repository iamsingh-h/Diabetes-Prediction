from django.contrib import admin
from .models import Predict


@admin.register(Predict)
class PredictionAdmin(admin.ModelAdmin):
    list_display= ['id','pregnancies','glucose','blood_pressure','skin_thickess','insulin','bmi','diabetes_pedigree_function', 'age','result']

