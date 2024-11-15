from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time, Text, Enum, DECIMAL
from sqlalchemy.orm import relationship
from database.connection import Base

class DocumentType(Base):
    __tablename__ = "document_type"

    document_type_id = Column(Integer, primary_key=True, index=True)
    type = Column(String(50), unique=True, nullable=False)

class Gender(Base):
    __tablename__ = "gender"

    gender_id = Column(Integer, primary_key=True, index=True)
    gender = Column(String(255), nullable=False)

class Patient(Base):
    __tablename__ = "patient"

    patient_id = Column(Integer, primary_key=True, index=True)
    document_type_id = Column(Integer, ForeignKey("document_type.document_type_id"))
    document_number = Column(String(255), unique=True, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    birth_date = Column(Date, nullable=False)
    gender_id = Column(Integer, ForeignKey("gender.gender_id"))
    residential_address = Column(String(255))
    occupation = Column(String(255))
    age = Column(Integer)
    phone = Column(String(20))
    email = Column(String(255), unique=True)
    health_insurance = Column(String(255))

    document_type = relationship("DocumentType")
    gender = relationship("Gender")

class Position(Base):
    __tablename__ = "position"

    position_id = Column(Integer, primary_key=True, index=True)
    position = Column(String(50), unique=True, nullable=False)

class Staff(Base):
    __tablename__ = "staff"

    staff_id = Column(Integer, primary_key=True, index=True)
    position_id = Column(Integer, ForeignKey("position.position_id"))
    document_type_id = Column(Integer, ForeignKey("document_type.document_type_id"))
    document_number = Column(String(255), unique=True, nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone = Column(String(20))
    email = Column(String(50), unique=True)

    position = relationship("Position")
    document_type = relationship("DocumentType")

class AppointmentType(Base):
    __tablename__ = "appointment_type"

    appointment_type_id = Column(Integer, primary_key=True, index=True)
    type = Column(String(50), unique=True, nullable=False)
    price = Column(DECIMAL(10, 0), nullable=False)

class AppointmentStatus(Base):
    __tablename__ = "appointment_status"

    status_id = Column(Integer, primary_key=True, index=True)
    status = Column(String(50), unique=True, nullable=False)

class Appointment(Base):
    __tablename__ = "appointment"

    appointment_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patient.patient_id"))
    staff_id = Column(Integer, ForeignKey("staff.staff_id"))
    date = Column(Date)
    time = Column(Time)
    appointment_type_id = Column(Integer, ForeignKey("appointment_type.appointment_type_id"))
    status_id = Column(Integer, ForeignKey("appointment_status.status_id"))

    patient = relationship("Patient")
    staff = relationship("Staff")
    appointment_type = relationship("AppointmentType")
    appointment_status = relationship("AppointmentStatus")

class Diagnosis(Base):
    __tablename__ = "diagnosis"

    diagnosis_id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey("appointment.appointment_id"))
    description = Column(Text)
    observations = Column(Text)
    recommendations = Column(Text)

    appointment = relationship("Appointment")

class Treatment(Base):
    __tablename__ = "treatment"

    treatment_id = Column(Integer, primary_key=True, index=True)
    diagnosis_id = Column(Integer, ForeignKey("diagnosis.diagnosis_id"))
    medication_list = Column(Text)
    dosage = Column(String(50))
    frequency = Column(String(50))
    duration = Column(String(50))
    price = Column(DECIMAL(10, 0), nullable=False)

    diagnosis = relationship("Diagnosis")

class Supplier(Base):
    __tablename__ = "supplier"

    supplier_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    address = Column(String(100))
    phone = Column(String(20))
    email = Column(String(50))
    supplied_products = Column(Text)
    main_contact = Column(String(50))

class Medication(Base):
    __tablename__ = "medication"

    medication_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(Text)
    supplier_id = Column(Integer, ForeignKey("supplier.supplier_id"))
    price = Column(DECIMAL(10, 0), nullable=False)

    supplier = relationship("Supplier")

class Prescription(Base):
    __tablename__ = "prescription"

    prescription_id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey("appointment.appointment_id"))
    date = Column(Date)
    instructions = Column(Text)

    appointment = relationship("Appointment")

class PrescriptionMedication(Base):
    __tablename__ = "prescription_medication"

    prescription_medication_id = Column(Integer, primary_key=True, index=True)
    prescription_id = Column(Integer, ForeignKey("prescription.prescription_id"))
    medication_id = Column(Integer, ForeignKey("medication.medication_id"))
    quantity = Column(Integer)
    dosage = Column(String(50))
    price = Column(DECIMAL(10, 0), nullable=False)

    prescription = relationship("Prescription")
    medication = relationship("Medication")

class Exam(Base):
    __tablename__ = "exam"

    exam_id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey("appointment.appointment_id"))
    type = Column(Text)
    results = Column(Text)
    date = Column(Date)
    observations = Column(Text)
    price = Column(DECIMAL(10, 0), nullable=False)

    appointment = relationship("Appointment")

class PaymentMethod(Base):
    __tablename__ = "payment_method"

    payment_method_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)

class InvoiceStatus(Base):
    __tablename__ = "invoice_status"

    invoice_status_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)

class Invoice(Base):
    __tablename__ = "invoice"

    invoice_id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey("appointment.appointment_id"))
    total_amount = Column(DECIMAL(10, 0))
    date = Column(Date)
    payment_method_id = Column(Integer, ForeignKey("payment_method.payment_method_id"))
    invoice_status_id = Column(Integer, ForeignKey("invoice_status.invoice_status_id"))

    appointment = relationship("Appointment")
    payment_method = relationship("PaymentMethod")
    invoice_status = relationship("InvoiceStatus")

class MedicationInventory(Base):
    __tablename__ = "medication_inventory"

    inventory_id = Column(Integer, primary_key=True, index=True)
    medication_name = Column(String(50))
    quantity = Column(Integer)
    expiration_date = Column(Date)
    supplier_id = Column(Integer, ForeignKey("supplier.supplier_id"))

    supplier = relationship("Supplier")

class Role(Base):
    __tablename__ = "role"

    role_id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(50), unique=True)

class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    password = Column(String(255))
    role_id = Column(Integer, ForeignKey("role.role_id"))

    role = relationship("Role")

class WeekDay(Base):
    __tablename__ = "week_day"

    week_day_id = Column(Integer, primary_key=True)
    day = Column(Enum('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'), unique=True, nullable=False)

class Schedule(Base):
    __tablename__ = "schedule"

    schedule_id = Column(Integer, primary_key=True, index=True)
    staff_id = Column(Integer, ForeignKey("staff.staff_id"))
    week_day_id = Column(Integer, ForeignKey("week_day.week_day_id"))
    start_time = Column(Time)
    end_time = Column(Time)
    availability = Column(Boolean)

    staff = relationship("Staff")
    week_day = relationship("WeekDay")