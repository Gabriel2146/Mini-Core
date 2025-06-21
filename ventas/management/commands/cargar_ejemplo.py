from django.core.management.base import BaseCommand
from ventas.models import Vendedor, Regla, Venta
from datetime import date

class Command(BaseCommand):
    help = 'Carga datos de ejemplo para pruebas'

    def handle(self, *args, **kwargs):
        # Limpiar datos previos
        Venta.objects.all().delete()
        Vendedor.objects.all().delete()
        Regla.objects.all().delete()

        # Crear reglas
        regla_10 = Regla.objects.create(descripcion='10% sobre ventas', porcentaje=10)
        regla_15 = Regla.objects.create(descripcion='15% sobre ventas', porcentaje=15)

        # Crear vendedores
        perico = Vendedor.objects.create(nombre='Perico')
        sola = Vendedor.objects.create(nombre='Sola')
        juan = Vendedor.objects.create(nombre='Juan')

        # Crear ventas para Perico (dentro del rango)
        Venta.objects.create(vendedor=perico, fecha=date(2025, 6, 2), monto=30, regla=regla_10)
        Venta.objects.create(vendedor=perico, fecha=date(2025, 6, 20), monto=50, regla=regla_10)
        # Total: 80, comisión: 8

        # Venta para Sola (fuera del rango)
        Venta.objects.create(vendedor=sola, fecha=date(2025, 5, 29), monto=100, regla=regla_15)

        # Venta para Juan (dentro del rango)
        Venta.objects.create(vendedor=juan, fecha=date(2025, 6, 3), monto=90, regla=regla_15)
        # Total: 90, comisión: 13.5

        self.stdout.write(self.style.SUCCESS('Datos de ejemplo cargados correctamente.'))
