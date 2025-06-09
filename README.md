# SkyRoute - Sistema de Gestión de Pasajes Aéreos

Proyecto integrador para la Tecnicatura en Ciencia de datos e IA.  
Este sistema simula al de una aerolínea, permitiendo gestionar clientes, destinos y ventas de los vuelos.

---

👩‍💻 Autores

- Juan Martin Rosello dal molin
- Erica Melisa Paredes
- Pablo Francisco Elías
- Florencia Belén Dussman
- Lisi Daniela Gonzalez

---
## Funcionalidad

SkyRoute permite:

- ✔ Gestión de **clientes** (alta, baja, modificación, listado)
- ✔ Gestión de **destinos** (ciudad, país, costo base)
- ✔ Registro y consulta de **ventas** (cliente, destino, fecha)
- ✔ **Botón de arrepentimiento**: permite anular ventas recientes
- ✔ **Reportes**:
  - Ventas por destino
  - Total recaudado por ventas activas

---
🛠️ Requisitos

- Python 3.9 o superior
- Terminal compatible (CMD, PowerShell, Bash o Terminal de VSCode)

---

▶️ ¿Cómo ejecutar el programa?

Descargá o cloná el repositorio.

Abrí una terminal en la carpeta del proyecto.

Ejecutá el archivo principal:
python main.py

---

🗺️ Diagrama Entidad-Relación

A continuación se muestra el modelo ER del sistema de gestión de pasajes:

<img width="612" alt="Captura de pantalla 2025-06-08 a la(s) 20 01 41" src="https://github.com/user-attachments/assets/cbc92a32-a79b-4751-9bbe-fdb40bfebf38" />

---

⚖️ Consideraciones Éticas y Legales

🧩 1. Implementación de la Ley 11.723 - Propiedad Intelectual

Proponemos:

Documentar y visibilizar que el proyecto es de uso educativo y no comercial.

Si en un futuro se decide convertirlo o utilizarlo de forma comercial deberiamos registrar el software previamente.

Incluir en el código fuente un aviso de autoría y licencia de uso. 


🔐 2. Implementación de la Ley 25.326 - Protección de Datos Personales

En SkyRoute, los datos sensibles como nombre de cliente, CUIT, correo deberan:	

Ser almacenados de forma segura (base de datos protegida con usuario/clave); no ser compartidos ni exportados sin consentimiento y ademas, incluir en el sistema una cláusula de consentimiento y aviso de privacidad si se llegara a publicar.


🌍 3. Convenio de Budapest - Cibercriminalidad internacional

Cooperación entre países miembros para investigar los delitos informáticos.

Como grupo lo que propondriamos es disponer y activar el protocolo de respuesta ante este incidente (bloqueo, auditoría, denuncia). Tambien la asistencia a autoridades nacionales/internacionales si fuera requerido.

