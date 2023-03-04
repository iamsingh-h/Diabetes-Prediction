from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from .models import Predict
import numpy as np



def home(request):
    return render(request,'home.html')

def predict(request):
    return render(request,'predict.html')    


def result(request):
    data = pd.read_csv(r"/Users/harsimarsingh/Desktop/project/diabetes/diabetes.csv")

    X = data.drop("Outcome",axis = 1)
    Y = data['Outcome']

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)
    
    
    model = LogisticRegression(max_iter=3000)
    model.fit(X_train,Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    pred = model.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])
    result2 = ""
    
    if pred ==[1]:
        result1 = "Positive"
    else:
        result1 = "Negative"


    prediction = Predict()
    prediction.pregnancies = val1
    prediction.glucose = val2
    prediction.blood_pressure = val3
    prediction.skin_thickess = val4
    prediction.insulin = val5
    prediction.bmi = val6
    prediction.diabetes_pedigree_function = val7
    prediction.age = val8
    prediction.result = result1
    prediction.save()

    return render(request,'predict.html',{"result2":result1})


def results(request):
    pred = Predict.objects.all()
    context = {"predict":pred,}    
    return render(request,'results.html',context)
    


