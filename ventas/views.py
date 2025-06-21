from django.shortcuts import render
from .models import Vendedor, Venta
from .forms import FiltroFechaForm
from django.db.models import Sum, F

def calcular_comisiones(request):
    comisiones = []
    total_general = 0
    form = FiltroFechaForm(request.GET or None)
    if form.is_valid():
        fecha_inicio = form.cleaned_data['fecha_inicio']
        fecha_fin = form.cleaned_data['fecha_fin']
        vendedores = Vendedor.objects.all()
        for vendedor in vendedores:
            ventas = Venta.objects.filter(vendedor=vendedor, fecha__range=(fecha_inicio, fecha_fin))
            total_ventas = ventas.aggregate(total=Sum('monto'))['total'] or 0
            if ventas.exists():
                regla = ventas.first().regla
                porcentaje = regla.porcentaje
                comision = total_ventas * (porcentaje / 100)
            else:
                porcentaje = 0
                comision = 0
            comisiones.append({
                'vendedor': vendedor.nombre,
                'total_ventas': total_ventas,
                'porcentaje': porcentaje,
                'comision': comision
            })
            total_general += comision
    else:
        form = FiltroFechaForm()
    return render(request, 'ventas/comisiones.html', {
        'form': form,
        'comisiones': comisiones,
        'total_general': total_general
    })
