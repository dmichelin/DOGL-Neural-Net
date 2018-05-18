from django.shortcuts import render
from django.http import HttpResponse
from .DOGLNN import DoglNet
def index(request):
    d = DoglNet()
    d.initModel()
    return HttpResponse(d.predict([[0,78,5,23]]))
