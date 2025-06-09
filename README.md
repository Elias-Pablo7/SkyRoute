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

Nuestro proyecto cumple con la normativa vigente hasta la fecha. A continuación, se aclara el mismo de forma clara. 

El proyecto cumple con la implementación del Botón de Arrepentimiento a nivel programación y base de datos.
    
A nivel programación se implementó una función que permite anular la venta mas reciente. Establecimos el limite de tiempo de 5 minutos.  Para que el usuario pueda arrepentirse de su compra. Se cambia el estado de la venta a "Anulada" y registra la fecha y hora de la anulación.

En Base de datos, relacionado a esto se crea una tabla que registra las ventas y su estado, incluyendo la fecha y hora de la anulación. La misma está vinculada a las demás tablas. 

Con respecto al marco normativo proponemos: 

1. 🧩 	Documentar y visibilizar que el proyecto es de uso educativo y no comercial. Si en un futuro se decide convertirlo o utilizarlo de forma comercial deberíamos registrar el software previamente. Incluir en el código fuente un aviso de autoría y licencia de uso. Todo esto corresponde a la Propiedad Intelectual de la Implementación de la Ley 11723.

El código desarrollado respeta los derechos de autor y no infringe la propiedad intelectual de terceros.

2. 🔐  En SkyRoute, los datos sensibles como nombre de cliente, CUIT, correo deben:
   
•	Ser almacenados de forma segura (base de datos protegida con usuario/clave).
•	No ser compartidos ni exportados sin consentimiento
•	Incluir en el sistema una cláusula de consentimiento y aviso de privacidad si se llegara a publicar.

Lo mencionado corresponde a la Implementación de la Ley 25.326 con relación a la Protección de Datos Personales. La ley define términos clave como datos personales, datos sensibles, archivo, registro, base o banco de datos, tratamiento de datos, responsable de archivo, datos informatizados, titular de los datos, usuario de datos, y disociación de datos.

3. 🌍	 En el caso que se desarrolle una sucursal en España y un cliente argentino presenta un inconveniente de seguridad y hay denuncia de por medio. Debemos actuar de la siguiente manera, aplicando El Convenio Internacional sobre Cibercriminalidad o convenio de Budapest el cual tiene como objetivo facilitar la cooperación internacional en la investigación y persecución de delitos informáticos, así como la protección de los datos.
   
Implementar medidas de seguridad para proteger el sistema contra ciberataques y garantizar la integridad de los datos. 

Los pasos a seguir son: 

a)	Establecer contactos con las autoridades competentes de ambos países miembros del Convenio de Budapest. Esto incluye agencias de seguridad, fuerzas de policía y organismos judiciales.

b)	Facilitar el intercambio de información relevante sobre incidentes y para eso usar canales seguros para compartir datos y evidencia.

c)	Asistencia mutua en la investigación y persecución de delitos informáticos. Realizar una colaboración en operaciones, búsqueda de sospechosos y la ejecución de órdenes judiciales.

d)	Debemos participa en programas de capacitación y educación sobre ciberseguridad y cibercriminalidad. Esto nos ayudaría a mejorar la capacidad de respuesta y la efectividad de las investigaciones.

e)	Desarrollaremos pruebas de protocolos de respuesta (simulacros) para asegurarnos que como equipo estamos preparados para manejar cualquier situación de inseguridad de manera efectiva.


4.	En el desarrollo de este proyecto como es en Argentina, si aplicamos Inteligencia Artificial debemos aclarar que  actualmente no existe una ley específica que regule de forma directa esta tecnología. Sin embargo, aplicamos normativas vigentes como la Ley 25.326 sobre Protección de los Datos Personales, la Ley 11.723 de Propiedad Intelectual y los principios generales de la Ley de Defensa del Consumidor.
   
Aplicar principalmente buenas prácticas como la transparencia en los algoritmos, la protección de datos y la ética en el uso de la IA. Esto incluye la explicación clara de cómo funciona la IA, la garantía de que los datos utilizados son seguros y la consideración de los impactos éticos de la IA en los usuarios y la sociedad.

