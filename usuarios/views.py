from django.shortcuts import render
from usuarios.models import Genero , Usuario
from usuarios.forms import GeneroForm




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
    
def usuarios_del(request,pk):
    context= {}
    try:
        usuario = Usuario.objects.get(rut=pk)
        usuario.delete()

        mensaje = "Usuario eliminado satisfactoriamente"
        usuarios = Usuario.objects.all()
        context = {"usuarios":usuarios,"mensaje":mensaje}
        return render(request,"usuariosT/lista.html",context)
    except:
        mensaje = "Error al eliminar"
        usuarios = Usuario.objects.all()
        context = {"usuarios":usuario,"mensaje":mensaje}
        return render(request,"usuariosT/lista.html",context)

def usuarios_findEdit(request,pk):
    
    if pk != "":
        usuario = Usuario.objects.get(rut=pk)
        generos = Genero.objects.all()

        context = {"usuario":usuario,"generos":generos}

        if usuario:
            return render(request,"usuariosT/editar.html",context)
        else:
            context = {"mensaje":"Error , el rut no existe"}
            return render(request,"usuariosT/editar.html",context)


def usuariosUpdate(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]

        objGenero = Genero.objects.get(id_genero = genero)

        usuario = Usuario()
        usuario.rut = rut
        usuario.nombre = nombre
        usuario.apellido_paterno = aPaterno
        usuario.apellido_materno = aMaterno
        usuario.fecha_nacimiento = fechaNac
        usuario.id_genero = objGenero
        usuario.telefono = telefono
        usuario.email = email
        usuario.direccion = direccion
        usuario.activo = 1

        usuario.save()

        generos = Genero.objects.all()
        context = {"mensaje":"Datos actualizados satisfactoriamente","generos":generos,"usuario":usuario}
        return render(request,"usuariosT/editar.html",context)
    else:
        #No es un post, entoncres se muestra un formulario para acer un add(insert)
        usuario = Usuario.objects.all
        context = {"usuario":usuario}
        return render(request,"usuariosT/editar.html",context)
    
def crud_generos(request):
    generos = Genero.objects.all()
    context = {"generos":generos}
    return render(request,"generos/listarG.html",context)

def generosAdd(request):
    context= {}
    if request.method == "POST":
        form = GeneroForm(request.POST)
        if form.is_valid:
            form.save()

            #Limpiar mi form
            form = GeneroForm()

            context = {"mensaje":"Genero guardado satisfactoriamente","form":form}
            return render(request,"generos/agregarG.html",context)
    else:
        form = GeneroForm()
        context = {"form":form}
        return render(request,"generos/agregarG.html",context)


def generos_del(request,pk):
    mensajes = []
    errores = []
    generos = Genero.objects.all()
    try:
        genero = Genero.objects.get(id_genero = pk)
        if genero:
            genero.delete()
            mensajes.append("Genero eliminado correctamente")
            context = {"generos":generos,"mensajes":mensajes}
            return render(request,"generos/listarG.html",context)
    except:
        genero = Genero.objects.all()
        mensaje = "Error , id inexistente"
        context = {"mensaje":mensaje,"generos":generos}
        return render(request,"generos/listarG.html",context)

def generos_edit(request,pk):
    try:
        genero = Genero.objects.get(id_genero = pk)
        context = {}
        if genero:
            if request.method == "POST":
                form = GeneroForm(request.POST, instance=genero)
                form.save()
                mensaje = "Genero Actualizado Correctamente"
                context = {"genero": genero , "form":form , "mensaje":mensaje}
                return render(request,"generos/editarG.html",context)
            else:
                form = GeneroForm(instance=genero)
                mensaje=""
                context = {"genero":genero, "form":form, "mensaje":mensaje}
                return render(request,"generos/editarG.html",context)
    except:
        generos = Genero.objects.all()
        mensajes = "Error, el id no existe"
        context = {"mensaje":mensajes, "generos":generos}
        return render(request,"generos/listarG.html",context)