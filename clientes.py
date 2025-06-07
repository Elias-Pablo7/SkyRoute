from db import conectar

def mostrar_clientes():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()

    if not clientes:
        print("No hay clientes registrados.")
    else:
        for c in clientes:
            print(f"ID: {c['id']} | Razón: {c['razon']} | CUIT: {c['cuit']} | Correo: {c['correo']}")


def agregar_cliente():
    razon = input("Razón social: ")
    cuit = input("CUIT: ")
    correo = input("Correo: ").replace("[arroba]", "@")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO clientes (razon, cuit, correo) VALUES (%s, %s, %s)",
        (razon, cuit, correo)
    )
    conn.commit()
    conn.close()
    print("✅ Cliente agregado.")


def modificar_cliente():
    id_cliente = int(input("ID del cliente a modificar: "))
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes WHERE id = %s", (id_cliente,))
    cliente = cursor.fetchone()

    if not cliente:
        print("⚠️ Cliente no encontrado.")
        conn.close()
        return

    razon = input(f"Nueva razón social (actual: {cliente['razon']}): ") or cliente['razon']
    cuit = input(f"Nuevo CUIT (actual: {cliente['cuit']}): ") or cliente['cuit']
    correo = input(f"Nuevo correo (actual: {cliente['correo']}): ").replace("[arroba]", "@") or cliente['correo']

    cursor.execute(
        "UPDATE clientes SET razon = %s, cuit = %s, correo = %s WHERE id = %s",
        (razon, cuit, correo, id_cliente)
    )
    conn.commit()
    conn.close()
    print("✅ Cliente modificado.")


def eliminar_cliente():
    id_cliente = int(input("ID del cliente a eliminar: "))
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
    conn.commit()
    conn.close()
    print("🗑️ Cliente eliminado.")