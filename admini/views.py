from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from usuarios.models import Usuario
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def menu(request):
    request.session["usuario"] = "christ"
    usuario = request.session["usuario"]
    context = {"usuario":usuario}
    return render(request,"admin/menu.html",context)

def reporte_alumnos(request):
    usuarios = Usuario.objects.all()
    context = {"usuarios":usuarios}
    return render(request,"admin/menu.html",context)

def home(request):
    context={}
    return render(request,"admin/home.html",context)