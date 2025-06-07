# ventas.py
from db import conectar
from datetime import datetime, timedelta

def registrar_venta():
    try:
        cliente_id = int(input("ID del cliente: "))
        destino_id = int(input("ID del destino: "))
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        estado = "Activa"

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ventas (cliente_id, destino_id, fecha, estado)
            VALUES (%s, %s, %s, %s)
        """, (cliente_id, destino_id, fecha, estado))
        conn.commit()
        conn.close()
        print("✅ Venta registrada con éxito.")
    except Exception as e:
        print(f"❌ Error al registrar venta: {e}")

def ver_ventas():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT v.id, c.razon, d.ciudad, d.pais, v.fecha, v.estado
        FROM ventas v
        JOIN clientes c ON v.cliente_id = c.id
        JOIN destinos d ON v.destino_id = d.id
    """)
    ventas = cursor.fetchall()
    conn.close()

    if not ventas:
        print("No hay ventas registradas.")
    else:
        for v in ventas:
            print(f"ID Venta: {v['id']} | Cliente: {v['razon']} | Destino: {v['ciudad']}, {v['pais']} | Fecha: {v['fecha']} | Estado: {v['estado']}")

def boton_arrepentimiento():
    venta_id = int(input("ID de la venta a anular: "))
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ventas WHERE id = %s", (venta_id,))
    venta = cursor.fetchone()

    if not venta:
        print("⚠️ Venta no encontrada.")
        conn.close()
        return

    fecha_venta = venta["fecha"]
    ahora = datetime.now()
    tiempo_venta = datetime.strptime(str(fecha_venta), "%Y-%m-%d %H:%M:%S")
    diferencia = ahora - tiempo_venta

    if diferencia <= timedelta(minutes=5):
        cursor.execute(
            "UPDATE ventas SET estado = 'Anulada', anulada_en = %s WHERE id = %s",
            (ahora.strftime("%Y-%m-%d %H:%M:%S"), venta_id)
        )
        conn.commit()
        print("🔁 Venta anulada con éxito.")
    else:
        print("⏱️ No se puede anular: han pasado más de 5 minutos.")
    conn.close()

def reporte_ventas_por_destino():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT d.ciudad, d.pais, COUNT(*) AS total_ventas
        FROM ventas v
        JOIN destinos d ON v.destino_id = d.id
        GROUP BY d.id
    """)
    resultados = cursor.fetchall()
    conn.close()

    print("\n📍 Ventas por Destino:")
    for r in resultados:
        print(f"{r['ciudad']}, {r['pais']}: {r['total_ventas']} venta(s)")

def reporte_total_recaudado():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT SUM(d.costo) AS total
        FROM ventas v
        JOIN destinos d ON v.destino_id = d.id
        WHERE v.estado = 'Activa'
    """)
    resultado = cursor.fetchone()
    conn.close()

    total = resultado['total'] if resultado['total'] else 0
    print(f"\n💰 Total recaudado por ventas activas: ${total:.2f}")