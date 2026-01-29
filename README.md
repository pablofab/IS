# 🏐 Volleyball Team Maker – Matchmaking Web App

Aplicación web desarrollada con **Django** para la gestión y matchmaking de voleibol. El sistema distingue entre **usuarios normales** y **administradores**, permitiendo una gestión controlada de equipos, jugadores y partidos.

---

## 🚀 Funcionalidades principales

### 👥 Usuarios normales

* Registro e inicio de sesión
* Al registrarse, el usuario aparece automáticamente como **jugador**
* Visualización de:

  * Lista de jugadores
  * Lista de equipos
  * Lista de partidos
* **No pueden crear ni editar** equipos, jugadores ni partidos

> ⚠️ La restricción de creación está aplicada a nivel de **templates (HTML)**, ocultando las interfaces de creación para usuarios no administradores.

---

### 🛠️ Administradores

Los administradores tienen acceso completo a la gestión del sistema:

* Crear, editar y eliminar **jugadores**

  * Datos numéricos (saque, recepción, etc.)
  * Datos característicos (posición, género, etc.)
* Crear, editar y eliminar **equipos**

  * Asignar jugadores a cada equipo
* Crear, editar y eliminar **partidos**

  * Asignar equipos previamente creados

Toda esta gestión se realiza mediante las vistas propias del proyecto y/o el **panel de administración de Django**.

---

## 🧰 Tecnologías utilizadas

* **Python 3**
* **Django**
* **HTML** (templates)
* **SQLite** (base de datos por defecto)
* **Pillow** (manejo de imágenes, por ejemplo fotos de jugadores)
* **Bootstrap** y **django-crispy-forms** (mejora visual y estructural de formularios)

---

## 👤 Crear un administrador (Superuser)

Antes de ejecutar el proyecto, se recomienda crear un usuario administrador.

Desde la raíz del proyecto (donde está `manage.py`):

```bash
python manage.py createsuperuser
```

Completa:

* Nombre de usuario
* Email (opcional)
* Contraseña

Luego podrás acceder al panel admin y configurarte como usuario admin en:

```
http://127.0.0.1:8000/admin/
```

---

## ▶️ Cómo ejecutar el proyecto

### 1️⃣ Crear y activar entorno virtual

```bash
python -m venv venv
```

Activar:

* **Windows (Git Bash / PowerShell)**

```bash
source venv/Scripts/activate
```

---

### 2️⃣ Instalar dependencias

```bash
pip install django
```

---

### 3️⃣ Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 4️⃣ Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

```
http://127.0.0.1:8000/
```

---

## 📁 Estructura relevante del proyecto

```
app/
├── media/
├── volley_team_maker/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── __init__.py
├── manage.py
└── db.sqlite3
```

---

## 🔐 Sobre permisos y restricciones

* Las restricciones para **crear** equipos, jugadores y partidos están implementadas en los **templates HTML**
* Los usuarios no administradores **no ven** las interfaces de creación
* Los administradores sí tienen acceso completo

> ⚠️ Nota: La seguridad está enfocada a nivel de interfaz (templates), no mediante decoradores de vistas.

---

## 📌 Notas finales

* `db.sqlite3` se usa como base de datos local
* Proyecto orientado a uso académico / demostrativo

