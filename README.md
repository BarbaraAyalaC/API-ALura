# API-ALura

# Tópicos API

Esta es una API RESTful para gestionar "tópicos". Permite a los usuarios crear, leer, actualizar y eliminar tópicos (CRUD). La API también cuenta con autenticación utilizando JWT (JSON Web Tokens).

## Requisitos

- Python 3.8+
- Dependencias (instalar con `pip install -r requirements.txt`)

## Endpoints

### 1. **Crear un tópico**
   - **POST** `/topics/`
   - Body: `{ "title": "Título", "description": "Descripción" }`
   - Requiere autenticación (token JWT).

### 2. **Leer todos los tópicos**
   - **GET** `/topics/`
   - Parámetros de consulta: `skip` (opcional), `limit` (opcional)

### 3. **Leer un tópico específico**
   - **GET** `/topics/{topic_id}`
   - Parámetros: `topic_id` (ID del tópico)

### 4. **Actualizar un tópico**
   - **PUT** `/topics/{topic_id}`
   - Body: `{ "title": "Nuevo título", "description": "Nueva descripción" }`
   - Requiere autenticación (token JWT).

### 5. **Eliminar un tópico**
   - **DELETE** `/topics/{topic_id}`
   - Parámetros: `topic_id` (ID del tópico)
   - Requiere autenticación (token JWT).

## Ejecutar el servidor

```bash
uvicorn app.main:app --reload
