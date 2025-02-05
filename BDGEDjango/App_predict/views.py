from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from App_build.models import CsvUpload, ClassifierInfo
from django.contrib.auth.decorators import login_required
import pickle
import sklearn



@login_required
def pred1(request):
    buildmodels = ClassifierInfo.objects.all()
    return render(request, 'App_predict/pred1.html', {'buildmodels': buildmodels})
# custom method for generating predictions
def getPredictions(model, scaled, sepal_length, sepal_width, petal_length, petal_width):
    prediction = model.predict(scaled.transform([[sepal_length, sepal_width, petal_length, petal_width]]))
    return prediction

# our result page view
def pred2(request):
    import sklearn
    import pickle
    sepal_length = float(request.GET['sepal_length'])
    sepal_width = float(request.GET['sepal_width'])
    petal_length = float(request.GET['petal_length'])
    petal_width = float(request.GET['petal_width'])
    classifier = request.GET['classifier']

    model = pickle.load(open("media/" + classifier, "rb"))
    scaled = pickle.load(open("media/" + "scaler" + classifier, "rb"))

    result = getPredictions(model, scaled, sepal_length, sepal_width, petal_length, petal_width)

    return render(request, 'App_predict/pred2.html', {'result': result})