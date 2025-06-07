-- ====================================
-- CREACIÓN DE LA BASE DE DATOS
-- ====================================

CREATE DATABASE IF NOT EXISTS skyroute;
USE skyroute;

-- ====================================
-- TABLA CLIENTES
-- ====================================
CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    razon VARCHAR(100),
    cuit VARCHAR(20),
    correo VARCHAR(100)
);

-- ====================================
-- TABLA DESTINOS
-- ====================================
CREATE TABLE IF NOT EXISTS destinos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ciudad VARCHAR(50),
    pais VARCHAR(50),
    costo DECIMAL(10,2)
);

-- ====================================
-- TABLA VENTAS
-- ====================================
CREATE TABLE IF NOT EXISTS ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    destino_id INT,
    fecha DATETIME,
    estado VARCHAR(20) DEFAULT 'Activa',
    anulada_en DATETIME DEFAULT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (destino_id) REFERENCES destinos(id)
);

-- ====================================
-- INSERCIÓN DE DATOS DE EJEMPLO
-- ====================================

-- Clientes de ejemplo
INSERT INTO clientes (razon, cuit, correo) VALUES
('ACME SS.A.', '30-12345678-9', 'contacto@acme.com'),
('Tech SRL', '30-87654321-0', 'info@tech.com'),
('Servicios Atma', '20-11223344-5', 'atma@servicios.com');

-- Destinos de ejemplo
INSERT INTO destinos (ciudad, pais, costo) VALUES
('Salta', 'Argentina', 35000.00),
('Santiago', 'Chile', 42000.00),
('San Pablo', 'Brasil', 51000.00);

-- Ventas de ejemplo
INSERT INTO ventas (cliente_id, destino_id, fecha, estado) VALUES
(1, 1, '2025-06-01 10:30:00', 'Activa'),
(2, 2, '2025-06-02 15:45:00', 'Anulada'),
(3, 3, '2025-06-04 09:00:00', 'Activa');

-- ====================================
-- CONSULTAS RELEVANTES (SELECT)
-- ====================================

-- 1️ Listar todos los clientes
SELECT * FROM clientes;

-- 2️ Mostrar las ventas realizadas en una fecha específica
SELECT * FROM ventas WHERE DATE(fecha) = '2025-06-02';

-- 3️ Obtener la última venta de cada cliente
SELECT cliente_id, MAX(fecha) AS ultima_venta
FROM ventas
GROUP BY cliente_id;

-- 4️ Listar todos los destinos que empiezan con "S"
SELECT * FROM destinos WHERE ciudad LIKE 'S%';

-- 5️ Mostrar cuántas ventas se realizaron por país
SELECT d.pais, COUNT(*) AS total_ventas
FROM ventas v
JOIN destinos d ON v.destino_id = d.id
GROUP BY d.pais;