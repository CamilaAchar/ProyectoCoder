


from django.shortcuts import render
from .models import Curso, Profesor, Estudiante
from ..forms import ProfesorForm, RegistroUsuarioForm
from django.http import HttpResponse


def curso(request):
    return render(request, "AppCoder/curso.html")

def estudiante(request):
    return render(request, "AppCoder/estudiante.html")

def profesor(request):
    return render(request, "AppCoder/profesor.html")

-----

def cursoFormulario (request):
   if request.method == "POST":
      
      curso = Curso(request.post["curso"],(request.post["camada"]))

      curso.save()

      return render(request, "AppCoder/inicio.html")
   
   return render(request, "AppeCoder/cursoFormulario.html")   

----

def cursoForm (request): 
   if request.method == "POST":
      
      miFormulario = cursoForm(request.POST)
      print(miFormulario)

      if miFormulario.is_valid: 
         informacion=miFormulario.cleaned_data

         curso=curso (nombre=informacion["curso"], camada=informacion["camada"])
         
         curso.save()
         
         return render(request, "AppCoder/inicio.html")
      
      else:
         
         miFormulario=cursoFormulario()
   
   return render(request, "AppeCoder/cursoFormulario.html", {"miFormulario":miFormulario})   
   

##para buscar 

def profesores(request):

    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = Profesor()
            profesor.nombre = form.cleaned_data['nombre']
            profesor.apellido = form.cleaned_data['apellido']
            profesor.email = form.cleaned_data['email']
            profesor.profesion = form.cleaned_data['profesion']
            profesor.save()
            form = ProfesorForm()
    else:
        form = ProfesorForm()

    profesores = Profesor.objects.all() #Profesor.objects.filter(nombre__icontains="P").all()
    
    return render(request, "AppCoder/profesores.html", {"profesores": profesores, "form" : form})

def busquedaComision(request):
    return render(request, "AppCoder/busquedaComision.html")

def buscar(request):
    
    comision= request.GET["comision"]
    if comision!="":
        cursos= Curso.objects.filter(comision__icontains=comision)#buscar otros filtros en la documentacion de django
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos})
    else:
        return render(request, "AppCoder/busquedaComision.html", {"mensaje": "Che Ingresa una comision para buscar!"})
