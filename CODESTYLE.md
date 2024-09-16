Markdown

\# Estilo de Codificación

Este documento establece las pautas de estilo de codificación que deben seguir todos los miembros del equipo para garantizar la coherencia y legibilidad del código.

\## Nombres de Variables y Funciones

* \*\*Variables:\*\*
* Utilizar `camelCase` para nombres de variables (e.g., `miVariable`, `nombreUsuario`).
* Evitar nombres demasiado cortos o genéricos.
* \*\*Funciones y Clases:\*\*
* Usar `PascalCase` para nombres de funciones y clases (e.g., `calcularPrecioTotal`, `ClaseVehiculo`).
* Los nombres deben ser descriptivos y reflejar la funcionalidad.

\## Indentación

* Utilizar \*\*4 espacios\*\* por nivel de indentación.
* \*\*No usar tabuladores.\*\*

\## Longitud Máxima de Líneas

* Mantener una longitud máxima de \*\*80 caracteres\*\* por línea para mejorar la legibilidad.
* En caso de líneas muy largas, utilizar saltos de línea o refactorizar el código.

\## Comentarios

* \*\*Comentarios en línea:\*\* Utilizar `//` para comentarios cortos y concisos.
* \*\*Comentarios de bloque:\*\* Utilizar `/\* \*/` para comentarios más largos y descriptivos.
* \*\*Documentación:\*\* Documentar funciones y clases con comentarios que expliquen su propósito, parámetros y valor de retorno.

\## Nombres de Commits

* Seguir la convención de \*\*Conventional Commits:\*\*
* `tipo: descripción del cambio`
* \*\*Tipos permitidos:\*\*
* `feat`: Nuevas funcionalidades.
* `fix`: Correcciones de errores.
* `docs`: Cambios en la documentación.
* `style`: Cambios de formato o estilo.
* `refactor`: Refactorizaciones de código.
* `test`: Nuevos tests o cambios en tests existentes.
* `chore`: Tareas de mantenimiento (e.g., actualizar dependencias).
* \*\*Ejemplos:\*\*
* `feat: agregar funcionalidad de filtrado por marca`
* `fix: corregir error en cálculo de impuestos`
* `docs: actualizar README.md`

\## Nombres de Ramas

* Utilizar una convención basada en el tipo de cambio:
* `feat/`: Nuevas funcionalidades.
* `fix/`: Correcciones de errores.
* `docs/`: Cambios en la documentación.
* `feature/`: Para ramas más grandes o complejas.
* `bugfix/`: Para ramas dedicadas a corregir errores.
* \*\*Ejemplos:\*\*
* `feat/implementar-login`
* `fix/resolver-conflicto-de-merge`

\## Otros Aspectos

* \*\*Espacios en blanco:\*\* Utilizar espacios en blanco de forma consistente para mejorar la legibilidad.
* \*\*Declaración de variables:\*\* Declarar las variables al principio del bloque donde se utilizan.
* \*\*Evitar código muerto:\*\* Eliminar código que no se utiliza.
* \*\*Nombrar constantes:\*\* Utilizar MAYÚSCULAS con guiones bajos para constantes (e.g., `MAX\_USUARIOS`).

\*\*Recomendaciones adicionales:\*\*

* \*\*Linter:\*\* Utilizar una herramienta de linting como ESLint o Pylint para automatizar la verificación del estilo de código.
* \*\*Formateador:\*\* Utilizar un formateador de código como Prettier para aplicar automáticamente el estilo de formato.
* \*\*Revisores de código:\*\* Realizar revisiones de código para asegurar que se cumplan las pautas establecidas.

\*\*Ejemplo de función documentada:\*\*

def calcular_precio_total(precio_base, impuesto):
  """
  Calcula el precio total de un vehículo.

  Args:
      precio_base (float): Precio base del vehículo.
      impuesto (float): Tasa de impuesto aplicable (en formato decimal, por ejemplo, 0.19 para un 19%).

  Returns:
      float: Precio total del vehículo.
  """

  precio_total = precio_base * (1 + impuesto)
  return precio_total
