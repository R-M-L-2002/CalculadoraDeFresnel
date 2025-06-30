from django.shortcuts import render
from .models import Historial

def truncar_decimales(numero, decimales):
    factor = 10 ** decimales
    return int(numero * factor) / factor


def fresnel_view(request):
    fresnel = None
    resultado = None
    interferencia = None

    # Variables para graficar
    distancia = None
    frecuencia = None
    obstaculo = None

    if request.method == "POST":
            distancia = float(request.POST.get("distancia"))
            frecuencia = float(request.POST.get("frecuencia"))
            obstaculo = float(request.POST.get("obstaculo"))

            if distancia > 0 and frecuencia > 0:
                fresnel = 8.656 * ((distancia / frecuencia) ** 0.5)
                resultado = truncar_decimales(fresnel, 2)

                # Evaluar interferencia 
                if obstaculo > 0.4 * fresnel:
                    interferencia = "⚠️ El obstáculo bloquea más del 40%: riesgo alto de interferencia."
                elif obstaculo > 0.2 * fresnel:
                    interferencia = "⚠️ El obstáculo supera el 20%: puede degradar la señal."
                else:
                    interferencia = "✅ El obstáculo no interfiere significativamente."

                # historial
                Historial.objects.create(
                    distancia=distancia,
                    frecuencia=frecuencia,
                    resultado=resultado
                )


    historial = Historial.objects.order_by('-id')[:10]

    return render(request, "calculadora/fresnel.html", {
        "resultado": resultado,
        "interferencia": interferencia,
        "historial": historial,
        "distancia": distancia,
        "frecuencia": frecuencia,
        "obstaculo": obstaculo,
        "fresnel_raw": fresnel,

    })
