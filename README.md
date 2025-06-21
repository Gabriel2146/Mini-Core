# Mini-Core: Sistema de Cálculo de Comisiones de Ventas

Este proyecto es una aplicación web desarrollada con Django y PostgreSQL que permite filtrar ventas por rango de fechas y calcular la comisión de cada vendedor según reglas definidas. El sistema está inspirado en el ejemplo y la transcripción de video proporcionados para el semestre.

## Características principales
- **Filtrado de ventas por rango de fechas**
- **Cálculo automático de comisiones** según la regla asignada a cada venta
- **Interfaz web moderna** con Bootstrap
- **Datos de ejemplo precargados** para pruebas rápidas

## Estructura del proyecto
- **minicore/**: Configuración principal del proyecto Django
- **ventas/**: Aplicación principal con modelos, vistas, formularios y comandos de carga de datos
- **templates/ventas/**: Plantillas HTML para la interfaz

## Modelos principales
- **Vendedor**: Representa a cada vendedor
- **Regla**: Define el porcentaje de comisión
- **Venta**: Relaciona vendedor, monto, fecha y regla de comisión

## Cómo usar
1. **Clona el repositorio** y navega a la carpeta del proyecto
2. **Configura tus credenciales de base de datos** en `minicore/settings.py`
3. **Crea el entorno virtual y activa**:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
4. **Instala dependencias**:
   ```powershell
   pip install django psycopg2-binary
   ```
5. **Aplica migraciones**:
   ```powershell
   python manage.py migrate
   ```
6. **Carga datos de ejemplo**:
   ```powershell
   python manage.py cargar_ejemplo
   ```
7. **Inicia el servidor**:
   ```powershell
   python manage.py runserver
   ```
8. **Accede a la app** en [http://localhost:8000/](http://localhost:8000/) y filtra por fechas (ejemplo: 2025-06-02 a 2025-06-26)

## Ejemplo de funcionamiento
- Vendedor "Perico" tiene dos ventas en el rango, suma $80, su comisión es 10% ($8)
- Vendedor "Sola" tiene ventas fuera del rango, no recibe comisión
- Vendedor "Juan" tiene una venta de $90, su comisión es 15% ($13.5)

## Arquitectura y patrón MVC
- **Modelos**: Definidos en `ventas/models.py`
- **Vistas**: Lógica en `ventas/views.py`, renderiza plantilla y procesa formulario
- **Controlador**: Django maneja el ruteo y la lógica de negocio en las vistas
- **Plantillas**: HTML en `ventas/templates/ventas/comisiones.html`

## Recursos y documentación
- [Documentación oficial de Django](https://docs.djangoproject.com/en/5.2/)
- [Documentación oficial de PostgreSQL](https://www.postgresql.org/docs/)
- [Video explicativo del patrón MVC en Django](https://www.youtube.com/watch?v=F5mRW0jo-U4)
- [Bootstrap](https://getbootstrap.com/)

## Despliegue
Puedes desplegar este proyecto en cualquier servidor compatible con Django y PostgreSQL (Heroku, Railway, Render, etc.).

## Contacto
- Nombre: [Tu Nombre]
- Email: [tu.email@ejemplo.com]

---

**Repositorio GitHub:** [Agrega aquí el link de tu repo]
**Video explicativo:** [Agrega aquí el link de tu video Loom o YouTube]
**Enlace deployado:** [Agrega aquí el link de tu despliegue si aplica]
