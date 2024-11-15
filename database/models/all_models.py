from sqlalchemy import (
    Column, Integer, String, ForeignKey, Date, Time, Boolean, Text, DECIMAL, Enum
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TipoDocumento(Base):
    __tablename__ = "TipoDocumento"
    id_tipo_documento = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(50), unique=True, nullable=False)
    pacientes = relationship("Paciente", back_populates="tipo_documento")
    personal = relationship("Personal", back_populates="tipo_documento")

class Genero(Base):
    __tablename__ = "Genero"
    id_genero = Column(Integer, primary_key=True, autoincrement=True)
    genero = Column(String(255), nullable=False)
    pacientes = relationship("Paciente", back_populates="genero")

class Paciente(Base):
    __tablename__ = "Paciente"
    id_paciente = Column(Integer, primary_key=True, autoincrement=True)
    id_tipo_documento = Column(Integer, ForeignKey("TipoDocumento.id_tipo_documento"))
    numero_documento = Column(String(255), unique=True, nullable=False)
    nombre = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    id_genero = Column(Integer, ForeignKey("Genero.id_genero"))
    direccion_de_residencia = Column(String(255))
    ocupacion = Column(String(255))
    edad = Column(Integer)
    telefono = Column(String(20))
    email = Column(String(255), unique=True)
    eps = Column(String(255))

    tipo_documento = relationship("TipoDocumento", back_populates="pacientes")
    genero = relationship("Genero", back_populates="pacientes")
    citas = relationship("Cita", back_populates="paciente")

class Cargo(Base):
    __tablename__ = "Cargo"
    id_cargo = Column(Integer, primary_key=True, autoincrement=True)
    cargo = Column(String(50), unique=True, nullable=False)
    personal = relationship("Personal", back_populates="cargo")

class Personal(Base):
    __tablename__ = "Personal"
    id_personal = Column(Integer, primary_key=True, autoincrement=True)
    id_cargo = Column(Integer, ForeignKey("Cargo.id_cargo"))
    id_tipo_documento = Column(Integer, ForeignKey("TipoDocumento.id_tipo_documento"))
    numero_documento = Column(String(255), unique=True, nullable=False)
    nombre = Column(String(50))
    apellido = Column(String(50))
    telefono = Column(String(20))
    email = Column(String(50), unique=True)

    cargo = relationship("Cargo", back_populates="personal")
    tipo_documento = relationship("TipoDocumento", back_populates="personal")
    citas = relationship("Cita", back_populates="personal")

class TipoCita(Base):
    __tablename__ = "TipoCita"
    id_tipo_cita = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(50), unique=True, nullable=False)
    precio = Column(DECIMAL(10, 0), nullable=False)
    citas = relationship("Cita", back_populates="tipo_cita")

class EstadoCita(Base):
    __tablename__ = "EstadoCita"
    id_estado = Column(Integer, primary_key=True, autoincrement=True)
    estado = Column(String(50), unique=True, nullable=False)
    citas = relationship("Cita", back_populates="estado")

class Cita(Base):
    __tablename__ = "Cita"
    id_cita = Column(Integer, primary_key=True, autoincrement=True)
    id_paciente = Column(Integer, ForeignKey("Paciente.id_paciente"))
    id_personal = Column(Integer, ForeignKey("Personal.id_personal"))
    fecha = Column(Date)
    hora = Column(Time)
    id_tipo_cita = Column(Integer, ForeignKey("TipoCita.id_tipo_cita"))
    id_estado = Column(Integer, ForeignKey("EstadoCita.id_estado"))

    paciente = relationship("Paciente", back_populates="citas")
    personal = relationship("Personal", back_populates="citas")
    tipo_cita = relationship("TipoCita", back_populates="citas")
    estado = relationship("EstadoCita", back_populates="citas")
    diagnosticos = relationship("Diagnostico", back_populates="cita")
    recetas = relationship("Receta", back_populates="cita")
    examenes = relationship("Examen", back_populates="cita")

class Diagnostico(Base):
    __tablename__ = "Diagnostico"
    id_diagnostico = Column(Integer, primary_key=True, autoincrement=True)
    id_cita = Column(Integer, ForeignKey("Cita.id_cita"))
    descripcion = Column(Text)
    observaciones = Column(Text)
    recomendaciones = Column(Text)

    cita = relationship("Cita", back_populates="diagnosticos")
    tratamientos = relationship("Tratamiento", back_populates="diagnostico")

class Tratamiento(Base):
    __tablename__ = "Tratamiento"
    id_tratamiento = Column(Integer, primary_key=True, autoincrement=True)
    id_diagnostico = Column(Integer, ForeignKey("Diagnostico.id_diagnostico"))
    lista_medicamentos = Column(Text)
    dosis = Column(String(50))
    frecuencia = Column(String(50))
    duracion = Column(String(50))
    precio = Column(DECIMAL(10, 0), nullable=False)

    diagnostico = relationship("Diagnostico", back_populates="tratamientos")

class Proveedor(Base):
    __tablename__ = "Proveedor"
    id_proveedor = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    direccion = Column(String(100))
    telefono = Column(String(20))
    email = Column(String(50))
    productos_suministrados = Column(Text)
    contacto_principal = Column(String(50))

    medicamentos = relationship("Medicamento", back_populates="proveedor")
    inventarios = relationship("InventarioMedicamentos", back_populates="proveedor")

class Medicamento(Base):
    __tablename__ = "Medicamento"
    id_medicamento = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    descripcion = Column(Text)
    id_proveedor = Column(Integer, ForeignKey("Proveedor.id_proveedor"))
    precio = Column(DECIMAL(10, 0), nullable=False)

    proveedor = relationship("Proveedor", back_populates="medicamentos")

class Receta(Base):
    __tablename__ = "Receta"
    id_receta = Column(Integer, primary_key=True, autoincrement=True)
    id_cita = Column(Integer, ForeignKey("Cita.id_cita"))
    fecha = Column(Date)
    instrucciones = Column(Text)

    cita = relationship("Cita", back_populates="recetas")
    medicamentos = relationship("RecetaMedicamento", back_populates="receta")

class RecetaMedicamento(Base):
    __tablename__ = "RecetaMedicamento"
    id_receta_medicamento = Column(Integer, primary_key=True, autoincrement=True)
    id_receta = Column(Integer, ForeignKey("Receta.id_receta"))
    id_medicamento = Column(Integer, ForeignKey("Medicamento.id_medicamento"))
    cantidad = Column(Integer)
    dosis = Column(String(50))
    precio = Column(DECIMAL(10, 0), nullable=False)

    receta = relationship("Receta", back_populates="medicamentos")
    medicamento = relationship("Medicamento")

class Examen(Base):
    __tablename__ = "Examen"
    id_examen = Column(Integer, primary_key=True, autoincrement=True)
    id_cita = Column(Integer, ForeignKey("Cita.id_cita"))
    tipo = Column(Text)
    resultados = Column(Text)
    fecha = Column(Date)
    observaciones = Column(Text)
    precio = Column(DECIMAL(10, 0), nullable=False)

    cita = relationship("Cita", back_populates="examenes")

class MetodoPago(Base):
    __tablename__ = "MetodoPago"
    id_metodo_pago = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True)

class EstadoFactura(Base):
    __tablename__ = "EstadoFactura"
    id_estado_factura = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True)

class Factura(Base):
    __tablename__ = "Factura"
    id_factura = Column(Integer, primary_key=True, autoincrement=True)
    id_cita = Column(Integer, ForeignKey("Cita.id_cita"))
    monto_total = Column(DECIMAL(10, 0))
    fecha = Column(Date)
    id_metodo_pago = Column(Integer, ForeignKey("MetodoPago.id_metodo_pago"))
    id_estado_factura = Column(Integer, ForeignKey("EstadoFactura.id_estado_factura"))

    cita = relationship("Cita")
    metodo_pago = relationship("MetodoPago")
    estado_factura = relationship("EstadoFactura")

class InventarioMedicamentos(Base):
    __tablename__ = "InventarioMedicamentos"
    id_inventario = Column(Integer, primary_key=True, autoincrement=True)
    nombre_medicamento = Column(String(50))
    cantidad = Column(Integer)
    fecha_caducidad = Column(Date)
    id_proveedor = Column(Integer, ForeignKey("Proveedor.id_proveedor"))

    proveedor = relationship("Proveedor", back_populates="inventarios")

class Rol(Base):
    __tablename__ = "Rol"
    id_rol = Column(Integer, primary_key=True, autoincrement=True)
    nombre_rol = Column(String(50), unique=True)

class Usuario(Base):
    __tablename__ = "Usuario"
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre_usuario = Column(String(50), unique=True)
    contrasena = Column(String(255))
    id_rol = Column(Integer, ForeignKey("Rol.id_rol"))

    rol = relationship("Rol")

class DiaSemana(Base):
    __tablename__ = "DiaSemana"
    id_dia_semana = Column(Integer, primary_key=True)
    dia = Column(Enum('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'), unique=True)

class Horario(Base):
    __tablename__ = "Horario"
    id_horario = Column(Integer, primary_key=True, autoincrement=True)
    id_personal = Column(Integer, ForeignKey("Personal.id_personal"))
    id_dia_semana = Column(Integer, ForeignKey("DiaSemana.id_dia_semana"))
    hora_inicio = Column(Time)
    hora_fin = Column(Time)
    disponibilidad = Column(Boolean)

    personal = relationship("Personal")
    dia_semana = relationship("DiaSemana")
