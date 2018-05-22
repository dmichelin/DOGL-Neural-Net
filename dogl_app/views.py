from django.shortcuts import render
from django.http import HttpResponse
from .DOGLNN import DoglNet
from .services import get_weather_predictions
from datetime import datetime
def index(request):
    print("Just about to train model")
    d = DoglNet()
    d.initModel()
    weather = get_weather_predictions()
    predictions = d.predict(weather)
    roundedPredictions = list(map(lambda x: round(x[1],4), predictions))
    text = list(map(lambda x: "DOGL Probability of " + str(datetime.now().strftime('%B'))+" " + str(x[3]) + " is ",weather))
    text_predictions = [text[i] + str(roundedPredictions[i]) for i in range(len(text))]
    context = {'predictions': text_predictions}
    return render(request, 'dogl/index.html',context)

