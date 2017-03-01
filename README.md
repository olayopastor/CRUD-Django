# CRUD-django
##A platform CRUD using Django in university

1. Git clone

2. Desde consola: virtualenv "nombre_del_virtualenv"

3. Copiar carpeta creada del virtualenv hacia la carpeta del proyecto

4. Activar virtualenv 

5. Instalar los requerimientos dentro del virtualenv con: pip install -r requirements.txt

6. Ir a carpeta "universidad" y hacer migraciones: python manage.py makemigrations proyecto

7. Despues: python manage.py migrate proyecto

8. Crear superusuario para acceder al admin de Django: python manage.py createsuperuser

Username: admin

Email address: admin@admin.com

Password:

Password (again):

Superuser created successfully.

9. En navegador ir a: http://127.0.0.1:8000/admin

10. Loguearse con usuario y contraseña antes establecidas

11. Agregar un licenciatura - NOTA: Este paso lo hago por que si quiero agregar un 'alumno' el campo de licenciatura es obligatorio y este unicamente se puede añadir desde el panel de control del admin

12. Acceder a http://127.0.0.1:8000/proyecto
