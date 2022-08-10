from django.shortcuts import render
from django.http import HttpResponse
from AppPrimerMVT.models import Familiar

def familiar(request):

      # familiar = Familiar(nombre = "Luciano", edad = "27", fecha_nac = "1994-2-21")
      # familiar.save()
      # familiar_obj = Familiar.objects.get(id=1)
      # documentoDeTexto = f"--->Nombre:{familiar.nombre}, Edad:{familiar.edad}, Fecha de nacimiento:{familiar.fecha_nac}"
      # return HttpResponse(familiar_obj)
      familiar_obj = Familiar.objects.all()
      return render(request, "index.html", {"familiares": familiar_obj})
