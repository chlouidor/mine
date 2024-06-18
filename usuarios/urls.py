from django.urls import path
from usuarios import views

urlpatterns = [ 
    path('index/' , views.index , name="index" ),
    path('crud/', views.crud, name="crud"),
    path('registrar/', views.regis_usuario, name="regis_usuario"),

]