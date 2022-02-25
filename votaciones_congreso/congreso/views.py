from congreso.models import Congreso
from django.shortcuts import render


def hemiciclo(request):
    congreso = Congreso.objects.last()
    return render(request, 'congreso/hemiciclo.html', {'congreso': congreso})
