# Informe de Pruebas – Agenda de Contactos

## 1. Objetivo
El objetivo de este informe es verificar el correcto funcionamiento de las
funcionalidades principales de la aplicación Agenda de Contactos, asegurando
que el sistema permita registrar, buscar, editar y eliminar contactos sin
errores.

---

## 2. Alcance de las pruebas
Las pruebas realizadas se enfocan en las siguientes funcionalidades:

- Registro de contactos
- Búsqueda de contactos por nombre
- Edición de contactos existentes
- Eliminación de contactos

---

## 3. Entorno de pruebas
- Lenguaje: Python 3
- Sistema: Aplicación de consola
- Entorno de ejecución: Local

---

## 4. Casos de prueba

### Prueba 1: Registro de contacto
**Descripción:** Verificar que un contacto se pueda agregar correctamente a la agenda.

**Datos de entrada:**
- Nombre: Jeanette Zenteno  
- Teléfono: 999999999  
- Email: prueba@example.com  

**Resultado esperado:**
- El contacto queda almacenado en la agenda.

**Resultado obtenido:**
- El contacto se agregó correctamente y puede ser visualizado.

**Estado:** ✔ Prueba exitosa

---

### Prueba 2: Búsqueda de contacto por nombre
**Descripción:** Verificar la búsqueda de un contacto utilizando su nombre.

**Datos de entrada:**
- Nombre buscado: Jeanette

**Resultado esperado:**
- El sistema muestra el contacto correspondiente.

**Resultado obtenido:**
- El contacto fue encontrado correctamente.

**Estado:** ✔ Prueba exitosa

---

### Prueba 3: Edición de contacto
**Descripción:** Verificar que se puedan modificar los datos de un contacto existente.

**Resultado esperado:**
- Los datos del contacto se actualizan correctamente.

**Resultado obtenido:**
- Los datos fueron modificados sin errores.

**Estado:** ✔ Prueba exitosa

---

### Prueba 4: Eliminación de contacto
**Descripción:** Verificar que un contacto pueda ser eliminado de la agenda.

**Resultado esperado:**
- El contacto se elimina del sistema.

**Resultado obtenido:**
- El contacto fue eliminado correctamente.

**Estado:** ✔ Prueba exitosa

---

## 5. Conclusión
Las pruebas realizadas demuestran que las funcionalidades principales de la
aplicación funcionan correctamente, cumpliendo con los requisitos establecidos
para el proyecto.
