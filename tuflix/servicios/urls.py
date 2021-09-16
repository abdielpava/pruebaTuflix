from servicios.views import vistaEjemplo 
from django.urls import path
   

#crear aplicacion servicios 
 
urlpatterns = [
    path('Ejemplo', vistaEjemplo)
]

