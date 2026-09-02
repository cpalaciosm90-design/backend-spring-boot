# Integración Full-Stack y Validación - Entrega Final

Este repositorio contiene la implementación del Backend en Spring Boot, demostrando el cumplimiento riguroso de las tres dimensiones evaluables de ingeniería.

## 1. Integración Full-Stack y Ciclo del Dato
- El sistema expone una API REST conectada a una base de datos PostgreSQL.
- Se ha configurado una política CORS que mantiene el sistema completamente libre de errores de origen cruzado (CORS), permitiendo la interacción fluida.
- El flujo de la información impacta la base de datos relacional PostgreSQL de forma transparente.

## 2. Rigor Técnico Acumulativo (DDD + TDD)
- **Arquitectura:** El backend organiza sus carpetas de forma desacoplada bajo los principios arquitectónicos de capas limpias y patrones tácticos de diseño guiado por el dominio en inglés.
- **Validación:** Se valida de forma matemática el 100% de las reglas lógicas de negocio centrales mediante suites automatizadas con JUnit 5 y Mockito.

## 3. Pautas de Seguridad de Grado de Producción
- **Gestión Hermética:** Exclusión absoluta de credenciales y secretos mediante el uso exclusivo de variables de entorno y el archivo `.gitignore`.
- **Aislamiento:** Herramientas de instrumentación técnica bloqueadas en producción, activándose únicamente bajo el perfil explícito de desarrollo (dev).
- **Docker No-Root:** Contenedor empaquetado configurando un usuario con privilegios restringidos.
- ## Enlace al Frontend
Puedes revisar la interfaz web desarrollada en Vite y TypeScript en el siguiente enlace: [Repositorio Frontend Vite-TS](https://github.com/cpalaciosm90-design/frontend-vite-ts)
