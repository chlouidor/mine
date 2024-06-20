
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('administrador/', admin.site.urls),
    path('usuarios/' , include("usuarios.urls")),
    path('zapatos/' , include("zapatosApp.urls")),
    path('admin/' , include("admini.urls")),

    path('accounts/' , include("django.contrib.auth.urls"))

]
