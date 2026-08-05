# CONTEXTO_PROYECTO.md

# Motor Inteligente para Gestión de Inventarios

## Documento de contexto para relevo del proyecto

Este documento resume el estado actual del proyecto para que otro asistente de IA pueda continuar el desarrollo sin perder el contexto ni modificar las decisiones arquitectónicas ya tomadas.

---

# 1. Resumen del objetivo del proyecto

El proyecto consiste en desarrollar un sistema empresarial de gestión de inventarios utilizando Python, PostgreSQL y FastAPI, siguiendo una arquitectura limpia y modular.

El objetivo principal no es únicamente administrar productos e inventario, sino construir un **Motor Inteligente** capaz de analizar información histórica y apoyar la toma de decisiones mediante técnicas de Machine Learning y reglas de negocio.

El sistema debe ser capaz de:

* administrar el catálogo de productos;
* controlar inventario;
* registrar compras;
* registrar ventas;
* generar indicadores;
* entrenar modelos de Machine Learning;
* predecir demanda;
* recomendar compras;
* detectar riesgo de quiebre de stock;
* detectar exceso de inventario;
* integrarse mediante una API REST profesional.

---

# 2. Tecnologías utilizadas

## Backend

* Python 3.13
* FastAPI
* SQLAlchemy 2.x
* PostgreSQL
* Alembic
* Pydantic v2
* Uvicorn

## Machine Learning

* Pandas
* NumPy
* Scikit-Learn
* Joblib

## Logging

* Loguru

## Arquitectura

* Clean Architecture
* Repository Pattern
* Service Layer
* Modular Monolith

---

# 3. Arquitectura utilizada

El proyecto está organizado por módulos.

Cada módulo posee su propia lógica de negocio.

## API

Ubicación:

```text
app/api/
```

Responsabilidades:

* definir endpoints;
* recibir solicitudes HTTP;
* validar request;
* devolver response;
* no contiene lógica de negocio.

---

## Routers

Ubicación:

```text
app/api/routers/
```

Actualmente existe:

* productos.py

Los routers únicamente llaman al Service correspondiente.

---

## Schemas API

Ubicación:

```text
app/api/schemas/
```

Se utilizan para:

* request HTTP
* response HTTP

No contienen lógica del dominio.

---

## Services

Ubicación:

```text
app/modules/*/services/
```

Contienen toda la lógica de negocio.

Regla importante:

Toda regla del negocio vive aquí.

Los routers nunca implementan reglas.

---

## Repositories

Ubicación:

```text
app/modules/*/repositories/
```

Responsabilidades:

* acceso a datos
* consultas SQLAlchemy

No contienen lógica del negocio.

---

## Models

Ubicación:

```text
app/modules/*/models/
```

Modelos SQLAlchemy.

Representan las tablas de PostgreSQL.

---

## Database

Ubicación:

```text
app/database/
```

Contiene:

* Session
* Engine
* Base

---

## Alembic

Se utiliza para administrar las migraciones de la base de datos.

Las migraciones ya están configuradas.

---

# 4. Estructura relevante

```text
app/

├── api/
│   ├── main.py
│   ├── routers/
│   ├── schemas/
│   ├── dependencies/
│   ├── middleware/
│   └── exception_handlers/
│
├── config/
│
├── database/
│
├── modules/
│
│   ├── catalogo/
│   │
│   ├── inventario/
│   │
│   ├── compras/
│   │
│   ├── ventas/
│   │
│   ├── analytics/
│   │
│   └── ml/
│
└── shared/
```

---

# 5. Configuración local

## Crear entorno virtual

Windows

```bash
python -m venv .venv
```

Activar

```bash
.venv\Scripts\activate
```

---

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Variables de entorno

Existe un archivo `.env`.

Ejemplo:

```env
DATABASE_URL=postgresql+psycopg2://usuario:password@localhost/inventario
LOG_LEVEL=INFO
```

Las credenciales reales no forman parte de este documento.

---

## Base de datos

Motor:

PostgreSQL

---

## Migraciones

```bash
alembic upgrade head
```

---

## Ejecutar FastAPI

```bash
uvicorn app.api.main:app --reload
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

# 6. Decisiones técnicas importantes

Durante todo el proyecto se decidió mantener las siguientes reglas:

## Toda lógica de negocio vive en Services

Los Routers solamente:

* reciben request
* llaman al Service
* devuelven response

Nunca contienen lógica.

---

## Repository Pattern

Los repositories solamente realizan consultas.

No contienen reglas.

---

## Schemas separados

Se decidió separar:

Schemas del dominio

de

Schemas de la API.

Motivo:

Permitir modificar la API sin afectar el dominio.

---

## Excepciones

Se utilizan excepciones propias.

Ejemplos:

* NotFoundException
* DuplicateException

FastAPI las transforma automáticamente en respuestas HTTP mediante handlers globales.

---

## Desactivación lógica

Los productos no se eliminan.

Se desactivan mediante:

```
activo = False
```

---

## Machine Learning desacoplado

Se separó en:

* datasets
* feature engineering
* trainer
* predictor
* engine
* reglas de negocio

---

# 7. Estado de los módulos

## Catálogo

Estado:

Muy avanzado.

Incluye:

* Productos
* Categorías
* Marcas
* Proveedores
* Unidades de medida

CRUD de productos vía API prácticamente completo.

---

## Inventario

Implementado.

Control de stock.

Pendiente API REST.

---

## Compras

Implementado a nivel de dominio.

Pendiente API REST.

---

## Ventas

Implementado a nivel de dominio.

Pendiente API REST.

---

## Analytics

Implementado.

Incluye cálculos iniciales.

---

## Machine Learning

Muy avanzado.

Implementado:

* Dataset Builder
* Feature Engineering
* Entrenamiento
* Predictor
* Motor de recomendaciones
* Detección de exceso
* Detección de riesgo de quiebre
* Cobertura de inventario

Validado mediante script:

```bash
python -m scripts.recomendar_compras
```

---

# 8. Estado del módulo Productos

## Modelo

Implementado.

Tabla SQLAlchemy completa.

---

## Schemas

Implementados.

Incluyen:

* ProductoCreate
* ProductoUpdate
* ProductoResponse
* ProductoCreateRequest
* ProductoUpdateRequest

---

## Repository

Implementado.

Responsable únicamente del acceso a datos.

---

## Service

Implementado.

Incluye:

* crear_producto
* obtener_producto_por_id
* obtener_producto_por_codigo
* listar_productos
* actualizar_producto
* desactivar_producto

Se añadieron validaciones de existencia para:

* categoría
* proveedor
* marca
* unidad de medida

antes de actualizar.

---

## Router

Implementado.

Ubicación:

```
app/api/routers/productos.py
```

---

## Validaciones

Se validan:

* códigos duplicados
* SKU duplicado
* relaciones existentes

---

## Manejo de errores

Se utilizan:

* NotFoundException
* DuplicateException

Convertidas automáticamente a respuestas HTTP.

---

# 9. Estado del Sprint 9.4

## GET /productos

Estado:

Probado.

Ruta:

```
GET /productos
```

Devuelve listado paginado.

HTTP:

```
200 OK
```

---

## GET /productos/{id}

Estado:

Probado.

Ruta:

```
GET /productos/{producto_id}
```

Devuelve un producto.

Si no existe:

```
404
```

---

## GET /productos/codigo/{codigo}

Estado:

Implementado.

Pendiente de confirmar si ya fue probado en Swagger.

Ruta:

```
GET /productos/codigo/{codigo}
```

Devuelve un producto por código.

Si no existe:

```
404
```

---

## POST /productos

Estado:

Probado.

Ruta:

```
POST /productos
```

Body:

```json
{
  "categoria_id": 1,
  "proveedor_id": 1,
  "marca_id": 1,
  "unidad_medida_id": 1,
  "codigo": "P000010",
  "sku": "SKU-10",
  "nombre": "Producto",
  "descripcion": "Descripción",
  "precio_compra_actual": 10,
  "precio_venta_actual": 15,
  "stock_minimo": 5,
  "stock_maximo": 20
}
```

HTTP esperado:

```
201 Created
```

Errores:

```
404
409
```

---

## PUT /productos/{id}

Estado:

Probado.

Ruta:

```
PUT /productos/{producto_id}
```

Ejemplo:

```json
{
  "nombre": "Laptop Dell Inspiron 16",
  "stock_minimo": 8
}
```

Respuesta:

```
200 OK
```

Se detectó inicialmente un problema por enviar IDs con valor `0` desde Swagger. Se resolvió utilizando únicamente los campos necesarios y agregando validaciones en `CatalogoService.actualizar_producto()`.

---

## PATCH /productos/{id}/desactivar

Estado:

Implementado.

Probado: pendiente de confirmar explícitamente.

Ruta:

```
PATCH /productos/{producto_id}/desactivar
```

Función:

Desactiva lógicamente un producto (`activo = false`).

HTTP esperado:

```
200 OK
```

---

# 10. Problemas o limitaciones pendientes

* Refactorizar la creación manual de `CatalogoService` en los routers mediante inyección de dependencias (`Depends(get_catalogo_service)`), mejora planificada pero aún no implementada.
* Completar la API REST para Inventario, Compras, Ventas, Analytics y ML.
* Añadir pruebas automatizadas (pendiente).

---

# 11. Próximos pasos recomendados

1. Finalizar oficialmente el Sprint 9.4 verificando todos los endpoints.
2. Crear dependencias para inyección de servicios en FastAPI.
3. Reutilizar el patrón CRUD implementado en Productos para Inventario.
4. Implementar CRUD de Compras.
5. Implementar CRUD de Ventas.
6. Exponer Analytics mediante API.
7. Exponer el Motor Inteligente mediante API.
8. Incorporar autenticación/autorización (pendiente de definir).
9. Crear pruebas unitarias e integración.
10. Desarrollar un Dashboard web (pendiente de definir la tecnología frontend).

---

# 12. Convenciones del proyecto

* Código tipado mediante type hints.
* Uso consistente de Pydantic v2.
* Nombres de clases en PascalCase.
* Nombres de archivos en snake_case.
* Cada módulo contiene:

  * models
  * repositories
  * schemas
  * services
* Los routers no contienen lógica de negocio.
* Los repositories no contienen reglas del negocio.
* Toda regla vive en Services.
* Se utilizan excepciones propias para errores del dominio.
* Se realizan commits únicamente al finalizar un sprint o un bloque funcional importante.

---

# 13. Historial resumido de sprints

## Fase 8 — Machine Learning

Completada.

Incluyó:

* Arquitectura ML.
* Dataset Builder.
* Feature Engineering.
* Entrenamiento del modelo.
* Persistencia del modelo (.pkl).
* Predictor de demanda.
* Motor de recomendaciones.
* Detección de riesgo de quiebre.
* Detección de exceso de inventario.
* Cálculo de cobertura.
* Integración de reglas de negocio.
* Script `python -m scripts.recomendar_compras` validado correctamente.

## Fase 9 — API REST

En desarrollo.

Completado hasta ahora:

* Configuración inicial de FastAPI.
* CORS.
* Manejo global de excepciones.
* CRUD de Productos prácticamente terminado.
* Documentación automática mediante Swagger.

Los siguientes módulos (Inventario, Compras, Ventas, Analytics y ML) deberán implementarse reutilizando exactamente la misma arquitectura utilizada para Productos.
