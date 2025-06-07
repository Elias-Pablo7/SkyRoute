from db import conectar

def mostrar_destinos():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM destinos")
    destinos = cursor.fetchall()
    conn.close()

    if not destinos:
        print("No hay destinos registrados.")
    else:
        for d in destinos:
            print(f"ID: {d['id']} | Ciudad: {d['ciudad']} | País: {d['pais']} | Costo: ${d['costo']:.2f}")


def agregar_destino():
    ciudad = input("Ciudad: ")
    pais = input("País: ")
    costo = float(input("Costo base: "))

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO destinos (ciudad, pais, costo) VALUES (%s, %s, %s)",
        (ciudad, pais, costo)
    )
    conn.commit()
    conn.close()
    print("✅ Destino agregado.")


def modificar_destino():
    id_destino = int(input("ID del destino a modificar: "))
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM destinos WHERE id = %s", (id_destino,))
    destino = cursor.fetchone()

    if not destino:
        print("⚠️ Destino no encontrado.")
        conn.close()
        return

    ciudad = input(f"Nueva ciudad (actual: {destino['ciudad']}): ") or destino['ciudad']
    pais = input(f"Nuevo país (actual: {destino['pais']}): ") or destino['pais']
    costo = input(f"Nuevo costo base (actual: {destino['costo']}): ")
    costo = float(costo) if costo else destino['costo']

    cursor.execute(
        "UPDATE destinos SET ciudad = %s, pais = %s, costo = %s WHERE id = %s",
        (ciudad, pais, costo, id_destino)
    )
    conn.commit()
    conn.close()
    print("✅ Destino modificado.")


def eliminar_destino():
    id_destino = int(input("ID del destino a eliminar: "))
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM destinos WHERE id = %s", (id_destino,))
    conn.commit()
    conn.close()
    print("🗑️ Destino eliminado.")