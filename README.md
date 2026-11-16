# 🚗 Sistema de Gestión de Estacionamientos — Backend

## Descripción

API REST desarrollada con Python, Django y Django REST Framework para administrar vehículos, estacionamientos y reservas.

El sistema permite registrar vehículos, gestionar espacios de estacionamiento y crear reservas asociadas a vehículos y estacionamientos existentes.

## Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- SQLite
- Postman (pruebas de la API)

## Requisitos previos

Antes de ejecutar el proyecto, se necesita:

- Python instalado (preferentemente una versión compatible con las dependencias del proyecto).
- Git instalado.
- Un editor de código como Visual Studio Code.

## Instalación y ejecución

### 1. Clonar el repositorio

Abrir una terminal y ejecutar:

```bash
git clone URL_DEL_REPOSITORIO
cd backend-proyecto-desarrollo-web
```

Reemplazar `URL_DEL_REPOSITORIO` por la dirección real del repositorio de GitHub.

### 2. Crear un entorno virtual

En Windows:

```powershell
python -m venv venv
```

### 3. Activar el entorno virtual

En PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
source venv/bin/activate
```

### 4. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

### 5. Preparar la base de datos

El proyecto utiliza SQLite.

Ejecutar las migraciones:

```bash
python manage.py migrate
```

Esto crea las tablas necesarias en la base de datos.

### 6. Iniciar el servidor

```bash
python manage.py runserver
```

El servidor estará disponible en:

http://127.0.0.1:8000/

**Nota:** la API se consulta a través de sus endpoints. La dirección raíz `/` no necesariamente tiene una página configurada.

## Endpoints de la API

### Vehículos

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/api/vehiculos/` | Listar vehículos |
| POST | `/api/vehiculos/` | Registrar vehículo |
| GET | `/api/vehiculos/{id}/` | Consultar vehículo |
| PUT/PATCH | `/api/vehiculos/{id}/` | Actualizar vehículo |
| DELETE | `/api/vehiculos/{id}/` | Eliminar vehículo |

### Estacionamientos

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/api/estacionamientos/` | Listar estacionamientos |
| POST | `/api/estacionamientos/` | Crear estacionamiento |
| GET | `/api/estacionamientos/{id}/` | Consultar estacionamiento |
| PUT/PATCH | `/api/estacionamientos/{id}/` | Actualizar estacionamiento |
| DELETE | `/api/estacionamientos/{id}/` | Eliminar estacionamiento |

### Reservas

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/api/reservas/` | Listar reservas |
| POST | `/api/reservas/` | Crear reserva |
| GET | `/api/reservas/{id}/` | Consultar reserva |
| PUT/PATCH | `/api/reservas/{id}/` | Actualizar reserva |
| DELETE | `/api/reservas/{id}/` | Eliminar reserva |

## Ejemplos de solicitudes

### Registrar un vehículo

POST `/api/vehiculos/`

```json
{
  "patente": "ABCD12",
  "marca": "Toyota",
  "modelo": "Corolla",
  "color": "Blanco"
}
```

### Registrar un estacionamiento

POST `/api/estacionamientos/`

```json
{
  "numero": "A01",
  "ubicacion": "Piso 1",
  "disponible": true,
  "precio_hora": 1500
}
```

### Crear una reserva

POST `/api/reservas/`

```json
{
  "vehiculo": 1,
  "estacionamiento": 1,
  "fecha_inicio": "2026-11-20T10:00:00-03:00",
  "fecha_fin": "2026-11-20T12:00:00-03:00"
}
```

Los IDs de vehículo y estacionamiento deben existir previamente en la base de datos.

## Reglas de negocio

El sistema incorpora validaciones para las reservas:

- La fecha de término debe ser posterior a la fecha de inicio.
- No se permiten reservas con horarios superpuestos en el mismo estacionamiento.
- Las reservas canceladas se excluyen de la búsqueda de conflictos.
- Se valida la existencia de los vehículos y estacionamientos asociados.

## Pruebas

Los endpoints pueden probarse mediante Postman o la interfaz navegable de Django REST Framework.

Respuestas HTTP habituales:

| Código | Significado |
|---|---|
| 200 | Solicitud exitosa |
| 201 | Recurso creado |
| 204 | Recurso eliminado |
| 400 | Datos inválidos |
| 404 | Recurso no encontrado |

## Estructura del proyecto

```text
backend-proyecto-desarrollo-web/
├── config/
│   ├── settings.py
│   └── urls.py
├── inicio/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Consideraciones

- El entorno virtual `venv/` no debe subirse a GitHub.
- Las dependencias se instalan utilizando `requirements.txt`.
- Si la base de datos SQLite no se incluye en el repositorio, se creará una nueva al ejecutar las migraciones, sin registros iniciales.
- Este proyecto está preparado para ejecutarse localmente con fines académicos y de desarrollo.