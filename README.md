# 🚀 Motor Inteligente para Gestión de Inventarios

Sistema empresarial desarrollado en **Python** con una arquitectura modular y limpia para la administración de inventarios, incorporando técnicas de **Machine Learning**, análisis de datos y reglas de negocio inteligentes para apoyar la toma de decisiones.

---

# Objetivo

Desarrollar una plataforma capaz de administrar un inventario completo y generar recomendaciones inteligentes utilizando datos históricos de ventas e inventario.

El sistema no se limita a registrar productos o movimientos; también es capaz de:

* Predecir demanda.
* Recomendar compras.
* Detectar riesgo de quiebre de stock.
* Detectar exceso de inventario.
* Analizar cobertura del inventario.
* Integrar modelos de Machine Learning con reglas de negocio.

---

# Tecnologías utilizadas

## Backend

* Python 3.13
* FastAPI
* SQLAlchemy 2.x
* PostgreSQL
* Pydantic v2
* Alembic

## Machine Learning

* Pandas
* NumPy
* Scikit-Learn
* Joblib

## Arquitectura

* Repository Pattern
* Service Layer
* Dependency Injection
* Clean Architecture
* Modular Monolith

---

# Características principales

## Catálogo

* Gestión de productos
* Categorías
* Marcas
* Proveedores
* Unidades de medida

## Inventario

* Control de existencias
* Entradas
* Salidas
* Stock mínimo
* Stock máximo

## Compras

* Registro de compras
* Actualización automática del inventario

## Ventas

* Registro de ventas
* Descuento automático del inventario

## Analytics

* Indicadores ABC
* Rotación de inventario
* Reportes estadísticos

## Machine Learning

* Construcción de datasets
* Ingeniería de características
* Entrenamiento de modelos
* Predicción de demanda
* Motor inteligente de recomendaciones

## API REST

* CRUD de productos
* Manejo global de excepciones
* CORS
* Validaciones con Pydantic
* Documentación automática con Swagger

---

# Arquitectura del proyecto

```
app/
│
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
│   ├── catalogo/
│   ├── inventario/
│   ├── compras/
│   ├── ventas/
│   ├── analytics/
│   └── ml/
│
└── shared/
```

Cada módulo contiene su propia lógica de negocio, modelos, repositorios, servicios y esquemas, manteniendo un bajo acoplamiento entre componentes.

---

# Arquitectura interna

Cada módulo sigue la misma estructura:

```
modulo/

models/
repositories/
schemas/
services/
```

Esta organización facilita:

* reutilización de código;
* pruebas unitarias;
* mantenimiento;
* escalabilidad.

---

# Flujo de una petición

```
Cliente

↓

FastAPI Router

↓

Service

↓

Repository

↓

SQLAlchemy

↓

PostgreSQL
```

Toda la lógica de negocio reside en la capa **Service**, mientras que los **Repositories** únicamente realizan acceso a datos.

---

# Arquitectura del módulo Machine Learning

```
Dataset Builder

↓

Feature Engineering

↓

Trainer

↓

Modelo (.pkl)

↓

Predictor

↓

Motor Inteligente

↓

Recomendaciones
```

---

# Funcionalidades inteligentes

Actualmente el motor puede:

* estimar demanda futura;
* calcular cobertura de inventario;
* detectar riesgo de quiebre de stock;
* detectar exceso de inventario;
* calcular cantidad sugerida de compra;
* asignar prioridades de compra;
* generar recomendaciones utilizando reglas de negocio.

---

# Base de datos

El proyecto utiliza PostgreSQL como motor principal.

El control de versiones del esquema se realiza mediante Alembic.

---

# API REST

Documentación disponible en:

```
/docs
```

Documentación alternativa:

```
/redoc
```

---

# Instalación

## Clonar repositorio

```bash
git clone <url-del-repositorio>
```

---

## Crear entorno virtual

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

---

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Configurar variables de entorno

Crear un archivo `.env` con la configuración de la base de datos.

Ejemplo:

```env
DATABASE_URL=postgresql+psycopg2://usuario:password@localhost/inventario
```

---

## Ejecutar migraciones

```bash
alembic upgrade head
```

---

## Ejecutar la API

```bash
uvicorn app.api.main:app --reload
```

---

# Machine Learning

Entrenar modelo:

```bash
python -m scripts.entrenar_modelo
```

Generar recomendaciones:

```bash
python -m scripts.recomendar_compras
```

---

# Estado del proyecto

## Finalizado

* Arquitectura del proyecto
* Catálogo
* Inventario
* Compras
* Ventas
* Analytics básico
* Machine Learning inicial
* Motor de recomendaciones
* API REST (CRUD de Productos)

## En desarrollo

* CRUD de Inventario
* CRUD de Compras
* CRUD de Ventas
* Dashboard
* Reportes avanzados
* Modelos predictivos adicionales

---

# Principios utilizados

* SOLID
* DRY
* Clean Code
* Repository Pattern
* Service Layer
* Dependency Injection
* Arquitectura Modular
* Separación de responsabilidades

---

# Autor

Proyecto desarrollado como un sistema empresarial para el aprendizaje y aplicación de:

* Arquitectura de Software
* Desarrollo Backend
* Machine Learning aplicado al negocio
* Diseño de APIs REST
* Buenas prácticas de desarrollo profesional.
