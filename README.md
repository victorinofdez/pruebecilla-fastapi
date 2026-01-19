# 🚀 API Básica con FastAPI

Este es un proyecto sencillo hecho con **FastAPI** que expone algunos endpoints de ejemplo y permite crear usuarios usando un modelo con **Pydantic**.  
Perfecto como introducción a FastAPI o como base para proyectos más grandes.

## 📁 Estructura del proyecto

```
.
├── main.py
└── README.md
```

## 🧠 Descripción

La API incluye:

- Un endpoint raíz (`/`) que devuelve un mensaje de bienvenida.
- Un endpoint `/caffe` con un mensaje simple.
- Un endpoint `/usuarios` que permite crear un usuario enviando datos en formato JSON.

## ⚙️ Requisitos

- Python 3.8 o superior
- pip

## 📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

2. Instala las dependencias:

```bash
pip install fastapi uvicorn
```

## ▶️ Ejecución

Ejecuta la aplicación con:

```bash
uvicorn main:app --reload
```

## 📌 Endpoints disponibles

### 🔹 GET `/`

Devuelve un mensaje de saludo.

**Respuesta:**

```json
{
  "message": "Buenos días grupo."
}
```

---

### 🔹 GET `/caffe`

Devuelve un mensaje relacionado con el café ☕.

**Respuesta:**

```json
{
  "message": "el caffe esta bueno"
}
```

---

### 🔹 POST `/usuarios`

Crea un usuario enviando un JSON con nombre y edad.

**Body (JSON):**

```json
{
  "name": "Juan",
  "edad": 25
}
```

**Respuesta:**

```json
{
  "usuario": {
    "name": "Juan",
    "edad": 25
  },
  "name": "Juan",
  "edad": 25
}
```

## 📚 Documentación automática

FastAPI genera documentación automáticamente:

- **Swagger UI:**  
  http://127.0.0.1:8000/docs

- **ReDoc:**  
  http://127.0.0.1:8000/redoc

## 🛠️ Tecnologías usadas

- FastAPI
- Pydantic
- Uvicorn
