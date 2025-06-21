from django.db import models

class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    # Puedes agregar más campos si es necesario

    def __str__(self):
        return self.nombre

class Regla(models.Model):
    descripcion = models.CharField(max_length=200)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)  # Ej: 10.00 para 10%

    def __str__(self):
        return f"{self.descripcion} ({self.porcentaje}%)"

class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    regla = models.ForeignKey(Regla, on_delete=models.CASCADE)

    def __str__(self):
        return f"Venta de {self.vendedor} el {self.fecha} por ${self.monto}"
