from django.shortcuts import render
from .models import Genero , Usuario


# Create your views here.

def index(request):
    request.session["usuario"]="profe"
    context = {}
    return render(request,"usuariosT/index.html",context)

def crud(request):
    usuarios = Usuario.objects.all()    
    context = {"usuarios":usuarios}
    return render(request,"usuariosT/lista.html",context)


def regis_usuario(request):
    if request.method != "POST":
        #No es un post, por lo tanto se muestra el formulario para agregar
        generos = Genero.objects.all()
        context = { "generos" : generos }
        return render(request,"usuariosT/registrar.html", context)
    else:
        generos = Genero.objects.all()
        #Es un post , por ende se recuperan los datos DEL FORMULARIO y 
        #se graban en la tabla
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero = genero)
        obj = Usuario.objects.create(
            rut = rut,
            nombre = nombre,
            apellido_paterno = aPaterno,
            apellido_materno = aMaterno,
            fecha_nacimiento = fechaNac,
            id_genero = objGenero,
            telefono = telefono,
            email = email,
            direccion = direccion,
            activo=1
        )
        obj.save()
        context = { "mensaje": "Usuario guardado satisfactoriamente", "generos":generos }
        return render(request,"usuariosT/registrar.html",context)