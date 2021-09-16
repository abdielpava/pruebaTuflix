from django.db import models

# Create your models here.
class CarritoCompras(models.Model):
    #conexion con usuario 
    #conexion con productos
    usuario = models.CharField(max_length=100)
    dcto = models.FloatField(blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)

    #items = []


class Producto(models.Model):
    categorias = (
        ("Frutas", "F"),
        ("Verduras", "V")
        )
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    categoria = models.CharField(choices=categorias, max_length=10)
    codigo = models.CharField(max_length=100, null=True, blank=True)
    foto = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.nombre 


class Item(models.Model):
     #item = {"sandalias":3}
     carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE) #si se borra el carrito se borran los items
     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
     precio = models.IntegerField()
     cantidad = models.IntegerField()

     def __str__(self):
        return self.producto.nombre+" - "+self.carrito.usuario 