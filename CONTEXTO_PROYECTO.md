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

Actualmente existen:

* auth.py
* usuarios.py
* productos.py
* inventario.py
* compras.py
* ventas.py

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
│   ├── ml/
│   │
│   └── usuarios/
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
* ConflictException

FastAPI las transforma automáticamente en respuestas HTTP mediante handlers globales.

Las reglas de negocio de Inventario, Compras y Ventas reutilizan estas excepciones para devolver respuestas HTTP controladas (`404` o `409`) en lugar de errores internos `500`.

---

## Inyección de dependencias

Cada router recibe su Service mediante `Depends(...)`. Existen dependencias para Catálogo, Inventario, Compras, Ventas, Analytics y ML.

Ejemplo:

```python
service: Annotated[
    CatalogoService,
    Depends(get_catalogo_service),
]
```

---

## Respuestas estándar exitosas

Las respuestas exitosas de la API siguen este formato genérico:

```json
{
  "success": true,
  "message": "Mensaje descriptivo.",
  "data": {}
}
```

Se implementan mediante `ApiResponse[T]` y el helper `success_response(...)`.

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

API REST de Productos completada y validada.

---

## Inventario

Implementado y expuesto por API REST.

Incluye movimientos, Kardex y reportes.

---

## Compras

Implementado y expuesto por API REST.

Incluye creación, confirmación y consultas por ID y proveedor.

---

## Ventas

Implementado y expuesto por API REST.

Incluye creación, confirmación, reporte de productos más vendidos y consulta por ID.

---

## Analytics

Implementado y expuesto por API REST.

Incluye cálculos iniciales, dashboard general, rotación de inventarios, clasificación ABC de productos, y compras y ventas acumuladas por mes.

---

## Machine Learning

Implementado y expuesto por API REST.

* Dataset Builder
* Feature Engineering
* Entrenamiento
* Predictor de demanda por producto y fecha
* Motor de recomendaciones de compra inteligente
* Detección de exceso y riesgo de quiebre
* Cobertura de inventario en días

Validado mediante scripts:
* `python -m scripts.recomendar_compras`
* `python -m scripts.predecir_demanda`

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

Estado: probado y validado.

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

Estado: probado y validado.

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

Estado: probado y validado.

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

Estado: probado y validado.

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

# 10. Estado de la Fase 9 — API REST

## Infraestructura API

Completada y validada.

* FastAPI, CORS y Swagger.
* Handlers globales para `NotFoundException`, `DuplicateException` y `ConflictException`.
* Respuestas exitosas estándar mediante `ApiResponse[T]`.
* Inyección de dependencias para los Services de todos los módulos.

## Productos — completado

```text
GET   /productos
GET   /productos/{id}
GET   /productos/codigo/{codigo}
POST  /productos
PUT   /productos/{id}
PATCH /productos/{id}/desactivar
```

## Inventario — completado

```text
POST /inventario/entradas
POST /inventario/salidas
POST /inventario/ajustes

GET  /inventario/{producto_id}/kardex
GET  /inventario/reportes/stock-bajo
GET  /inventario/reportes/sin-stock
GET  /inventario/reportes/valor
GET  /inventario/reportes/valor-total
```

Validaciones comprobadas:

* producto inexistente: `404 Not Found`;
* stock insuficiente: `409 Conflict`;
* Kardex con trazabilidad de entradas, salidas y ajustes.

## Compras — completado

```text
POST  /compras
PATCH /compras/{compra_id}/confirmar
GET   /compras/{compra_id}
GET   /compras?proveedor_id={proveedor_id}
```

Al confirmar una compra se registran automáticamente entradas en Inventario. También se validaron documentos duplicados y confirmaciones repetidas con `409 Conflict`.

## Ventas — en progreso

Implementado y validado:

## Ventas — completado

```text
POST  /ventas
PATCH /ventas/{venta_id}/confirmar
GET   /ventas/reportes/productos-mas-vendidos
GET   /ventas/{venta_id}



Analytics mediante API REST.

  GET /analytics/dashboard
  GET /analytics/ventas-mes
  GET /analytics/compras-mes
  GET /analytics/rotacion
  GET /analytics/abc


Motor Inteligente y predicciones de Machine Learning mediante API REST.

  GET /ml/prediccion
  GET /ml/recomendaciones



---

### Bloque 3: Limpiar Pendientes Recomendados (Sección 11)

Busca la Sección 11 (líneas 815 a 826) y reemplázala por los pendientes actuales del proyecto:

```markdown
# 11. Pendientes recomendados

1. Decidir e implementar consultas adicionales de Ventas y Compras si son necesarias (por ejemplo, listados detallados con filtros).
2. Añadir pruebas automatizadas unitarias y de integración para todos los endpoints ya implementados.
3. ~~Incorporar autenticación y autorización (login y tokens JWT para proteger endpoints).~~ Completado — ver Sección 14.
4. Desarrollar un Dashboard o interfaz frontend (tecnología a definir).

---

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

En desarrollo avanzado.

Sprints completados:

* Sprint 9.4: CRUD de Productos validado.
* Sprint 9.5: inyección de dependencias para Services.
* Sprint 9.5.5: respuestas exitosas estándar.
* Sprint 10.1: movimientos de Inventario.
* Sprint 10.2: Kardex y manejo de errores de Inventario.
* Sprint 10.3: reportes de Inventario.
* Sprint 11.1: creación y confirmación de Compras.
* Sprint 11.2: consultas de Compras.
* Sprint 12.1: creación y confirmación de Ventas.
* Sprint 12.2: reporte de productos más vendidos.
* Sprint 12.3: endpoint de consulta de Ventas por ID validado.
* Sprint 13.1: endpoints de Analytics expuestos en la API REST.
* Sprint 13.2: endpoints de Machine Learning expuestos en la API REST y corrección en la firma de predicción de demanda de `MLService`.


---

# 14. Autenticación y Autorización

Completada la primera versión de autenticación basada en tokens JWT.

## Tecnologías

* `PyJWT` para creación y validación de tokens.
* `pwdlib` + `argon2-cffi` para hashing de contraseñas (Argon2id).

## Módulo Usuarios

Ubicación:

```text
app/modules/usuarios/
```

Contiene:

* `enums/rol_usuario.py` — `RolUsuario` (ADMIN, USUARIO).
* `exceptions/` — `CredencialesInvalidasException`, `TokenInvalidoException`, `UsuarioInactivoException`, `AccesoDenegadoException`.
* `models/usuario.py` — tabla `usuarios`.
* `repositories/usuario_repository.py` — acceso a datos.
* `value_objects/password.py` — hash y verificación Argon2id.
* `services/token_service.py` — creación y decodificación JWT.
* `services/auth_service.py` — autenticación de usuarios.
* `services/usuario_service.py` — CRUD de usuarios.
* `schemas/usuario_schema.py` — schemas del dominio.

## Endpoints

```text
POST /auth/login      # público — devuelve access token JWT + datos del usuario
GET  /auth/me         # autenticado — información del usuario actual
GET    /usuarios              # solo ADMIN
GET    /usuarios/{id}         # solo ADMIN
POST   /usuarios              # solo ADMIN
PUT    /usuarios/{id}         # solo ADMIN
PATCH  /usuarios/{id}/desactivar  # solo ADMIN
```

## Protección de endpoints

Todos los routers (excepto `health` y `auth/login`) exigen autenticación:

* Se aplica mediante `dependencies=[Depends(get_current_user)]` al registrar cada router en `app/api/main.py`.
* Swagger dispone del botón *Authorize* (header `Authorization: Bearer <token>`).

Restricciones por rol (solo ADMIN):

* Crear, actualizar y desactivar productos.
* Entradas, salidas y ajustes de inventario.
* Confirmar compras y ventas.
* Endpoints de Analytics.
* Endpoints de Machine Learning.
* Gestión de usuarios.

Dependencias ubicadas en:

```text
app/api/dependencies/auth.py
app/api/dependencies/usuarios.py
```

## Manejo de errores

Nuevos handlers en `app/api/exceptions/handlers.py`:

* 401 — credenciales inválidas / token inválido o expirado.
* 403 — usuario inactivo / sin el rol requerido.

## Configuración

Variables de entorno:

```env
JWT_SECRET_KEY=clave_secreta_para_firma_jwt_debe_tener_al_menos_32_bytes
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30
ADMIN_EMAIL=admin@sistema.com
ADMIN_PASSWORD=...
```

## Base de datos y migraciones

* Tabla `usuarios` + enum PostgreSQL `rolusuario`.
* Revisión Alembic: `89cc0911a465_crear_modulo_usuarios`.
* Seeder del administrador inicial:

```bash
python -m scripts.seed_usuario_admin
```

## Pruebas

* `tests/conftest.py` — fixture con SQLite en memoria y override de `get_db`.
* `tests/test_auth.py` — 11 pruebas: login exitoso, credenciales incorrectas, usuario inactivo, endpoint sin token (401), token inválido, `/auth/me`, rol requerido (403) y usuario duplicado (409).

```bash
pytest tests/
```

---

# 15. Autenticación en el Frontend

Implementada la integración del frontend (React + Vite + MUI + TanStack Query) con la autenticación del backend.

## Motivación

Los endpoints ahora exigen token JWT. Antes de esta integración, el frontend no enviaba el token, por lo que cualquier petición protegida (por ejemplo, `GET /productos`) devolvía `401 Unauthorized`.

## Flujo implementado

1. `POST /auth/login` devuelve `access_token` y datos del usuario.
2. El token y el usuario se guardan en `localStorage`.
3. Un interceptor de axios adjunta `Authorization: Bearer <token>` a cada petición.
4. Si el backend responde `401`, el interceptor limpia la sesión y redirige a `/login`.
5. Al cargar la app, si existe token, se valida con `GET /auth/me` para restaurar la sesión.

## Archivos

### Nuevos

```text
frontend/src/
├── features/auth/
│   ├── types/auth.ts              # Usuario, LoginRequest, LoginResponse
│   ├── services/auth.service.ts   # login(), obtenerUsuarioActual(), cerrarSesion()
│   ├── authContext.ts             # Contexto de autenticación
│   ├── AuthProvider.tsx           # Proveedor: estado global + restauración de sesión
│   └── hooks/useAuth.ts           # Hook useAuth()
├── services/auth/token.ts         # Persistencia en localStorage
└── routes/ProtectedRoute.tsx      # Redirige a /login si no hay sesión
```

### Modificados

```text
frontend/src/
├── services/api/client.ts         # Interceptor de autorización y manejo de 401
├── pages/LoginPage.tsx            # Formulario real de email/contraseña (MUI)
├── pages/DashboardPage.tsx        # Muestra usuario/rol + botón "Cerrar sesión"
├── routes/AppRoutes.tsx           # Rutas protegidas con ProtectedRoute
└── App.tsx                        # Envuelve la app con AuthProvider
```

## Comportamiento

* Sin sesión: cualquier ruta protegida redirige a `/login`.
* Login exitoso: guarda token y redirige a `/`.
* `401`: limpia sesión y redirige a `/login` (token expirado o inválido).
* `403`: los usuarios con rol `USUARIO` no pueden acceder a endpoints de solo-ADMIN.
* El token expira según `JWT_ACCESS_TOKEN_EXPIRE_MINUTES` (30 min por defecto).

## Cómo ejecutar

```bash
# Backend
.venv/Scripts/python.exe -m uvicorn app.api.main:app --reload

# Frontend
cd frontend && npm run dev
```

Acceso en `http://localhost:5173` (redirige a `/login`). Credenciales iniciales: `admin@sistema.com` / `Admin12345`.

## Notas de configuración

* La URL del backend se define en `frontend/.env` mediante `VITE_API_URL` (por defecto `http://127.0.0.1:8000`).
* CORS en el backend ya permite los orígenes `http://localhost:5173` y `http://127.0.0.1:5173`.
* Verificación: `npm run build` (tsc + vite) y `npm run lint` (oxlint) sin errores.
