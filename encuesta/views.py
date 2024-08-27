from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Desde la vista de encuestas!")
# views.py
from django.http import HttpResponse

def calcular(request, pago, num_horas):
    # Convertir los parámetros a números flotantes
    pago = float(pago)
    num_horas = float(num_horas)

    if num_horas <= 40:
        total = num_horas * pago
    else:
        horas_normales = 40
        horas_extras = num_horas - 40
        total = (horas_normales * pago) + (horas_extras * pago * 2)
    
    # Retornar el resultado
    return HttpResponse(f'El pago total es: {total:.2f}')

