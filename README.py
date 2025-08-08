# QA Project — Urban Routes (ES)

## Descripción del proyecto
Este repositorio contiene las **pruebas automatizadas** para verificar el flujo completo de “pedir un taxi” en la aplicación **Urban Routes**.
Las pruebas siguen el patrón **Page Object Model (POM)** e incluyen localizadores y métodos en `UrbanRoutesPage`, así como los casos de prueba en `TestUrbanRoutes` dentro de `main.py`.

### Cobertura del ejercicio (Ejercicio 1)
Las pruebas automatizadas validan, de extremo a extremo, que un usuario pueda:
1. **Configurar la dirección** de origen y destino.
2. **Seleccionar la tarifa _Comfort_.**
3. **Rellenar el número de teléfono** y confirmar el código.
4. **Agregar una tarjeta de crédito** (ten en cuenta que el botón **link** se activa cuando el campo **CVV** pierde el foco — simular `TAB` o clic fuera).
   - Se usa la función **`retrieve_phone_code()`** (incluida en el repo) para **interceptar el código de confirmación** requerido.
5. **Escribir un mensaje** para el conductor.
6. **Pedir una manta y pañuelos.**
7. **Pedir 2 helados.**
8. Verificar que **aparece el modal de “buscar un taxi”**.

---

## Tecnologías y técnicas utilizadas
- **Python 3.x** — Lenguaje base de las pruebas.
- **pytest** — Framework de testing y orquestación de suites.
- **Selenium WebDriver** (o Playwright, según tu `requirements.txt`) — Automatización del navegador.
- **Page Object Model (POM)** — Encapsula localizadores y acciones en `UrbanRoutesPage`.
- **Esperas explícitas** — Sincronización estable con el DOM.
- **Manejo de modales e inputs** — Cambio de foco (p. ej. enviar `TAB`) para habilitar botones.
- **Utilidades del proyecto** — `retrieve_phone_code()` para interceptar el código de confirmación de teléfono/tarjeta.
- **Git** — Control de versiones y trabajo colaborativo.
- **PyCharm** — IDE recomendado para desarrollo y depuración.

---

## Estructura del repositorio
qa-project-Urban-Routes-es/
├─ data.py # Datos de prueba y/o utilidades (p.ej., retrieve_phone_code)
├─ main.py # UrbanRoutesPage + TestUrbanRoutes (casos del ejercicio 1)
└─ README.md # Este archivo