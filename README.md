# Grupo-1B
Proyecto Integrador
Paso 1:
Creacion de base de datos:
CREATE TABLE proyectos (
  id_proyecto INT AUTO_INCREMENT PRIMARY KEY,
  nombre_proyecto VARCHAR(30) NOT NULL,
  descripcion TEXT,
  anio YEAR
);

CREATE TABLE alumnos (
  id_alumno INT AUTO_INCREMENT PRIMARY KEY,
  nombres VARCHAR(25) NOT NULL,
  apellidos VARCHAR(25) NOT NULL,
  seccion VARCHAR(5),
  id_proyecto INT,
  FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto)
);
