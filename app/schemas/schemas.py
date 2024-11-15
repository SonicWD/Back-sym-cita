from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date, time
from decimal import Decimal

class DocumentTypeBase(BaseModel):
    type: str

class DocumentTypeCreate(DocumentTypeBase):
    pass

class DocumentType(DocumentTypeBase):
    document_type_id: int

    class Config:
        orm_mode = True

class GenderBase(BaseModel):
    gender: str

class GenderCreate(GenderBase):
    pass

class Gender(GenderBase):
    gender_id: int

    class Config:
        orm_mode = True

class PatientBase(BaseModel):
    document_type_id: int
    document_number: str
    first_name: str
    last_name: str
    birth_date: date
    gender_id: int
    residential_address: Optional[str] = None
    occupation: Optional[str] = None
    age: Optional[int] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    health_insurance: Optional[str] = None

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    patient_id: int

    class Config:
        orm_mode = True

class PositionBase(BaseModel):
    position: str

class PositionCreate(PositionBase):
    pass

class Position(PositionBase):
    position_id: int

    class Config:
        orm_mode = True

class StaffBase(BaseModel):
    position_id: int
    document_type_id: int
    document_number: str
    first_name: str
    last_name: str
    phone: str
    email: EmailStr

class StaffCreate(StaffBase):
    pass

class Staff(StaffBase):
    staff_id: int

    class Config:
        orm_mode = True

class AppointmentTypeBase(BaseModel):
    type: str
    price: Decimal

class AppointmentTypeCreate(AppointmentTypeBase):
    pass

class AppointmentType(AppointmentTypeBase):
    appointment_type_id: int

    class Config:
        orm_mode = True

class AppointmentStatusBase(BaseModel):
    status: str

class AppointmentStatusCreate(AppointmentStatusBase):
    pass

class AppointmentStatus(AppointmentStatusBase):
    status_id: int

    class Config:
        orm_mode = True

class AppointmentBase(BaseModel):
    patient_id: int
    staff_id: int
    date: date
    time: time
    appointment_type_id: int
    status_id: int

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    appointment_id: int

    class Config:
        orm_mode = True

class DiagnosisBase(BaseModel):
    appointment_id: int
    description: str
    observations: Optional[str] = None
    recommendations: Optional[str] = None

class DiagnosisCreate(DiagnosisBase):
    pass

class Diagnosis(DiagnosisBase):
    diagnosis_id: int

    class Config:
        orm_mode = True

class TreatmentBase(BaseModel):
    diagnosis_id: int
    medication_list: str
    dosage: str
    frequency: str
    duration: str
    price: Decimal

class TreatmentCreate(TreatmentBase):
    pass

class Treatment(TreatmentBase):
    treatment_id: int

    class Config:
        orm_mode = True

class SupplierBase(BaseModel):
    name: str
    address: str
    phone: str
    email: EmailStr
    supplied_products: str
    main_contact: str

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    supplier_id: int

    class Config:
        orm_mode = True

class MedicationBase(BaseModel):
    name: str
    description: str
    supplier_id: int
    price: Decimal

class MedicationCreate(MedicationBase):
    pass

class Medication(MedicationBase):
    medication_id: int

    class Config:
        orm_mode = True

class PrescriptionBase(BaseModel):
    appointment_id: int
    date: date
    instructions: str

class PrescriptionCreate(PrescriptionBase):
    pass

class Prescription(PrescriptionBase):
    prescription_id: int

    class Config:
        orm_mode = True

class PrescriptionMedicationBase(BaseModel):
    prescription_id: int
    medication_id: int
    quantity: int
    dosage: str
    price: Decimal

class PrescriptionMedicationCreate(PrescriptionMedicationBase):
    pass

class PrescriptionMedication(PrescriptionMedicationBase):
    prescription_medication_id: int

    class Config:
        orm_mode = True

class ExamBase(BaseModel):
    appointment_id: int
    type: str
    results: str
    date: date
    observations: Optional[str] = None
    price: Decimal

class ExamCreate(ExamBase):
    pass

class Exam(ExamBase):
    exam_id: int

    class Config:
        orm_mode = True

class PaymentMethodBase(BaseModel):
    name: str

class PaymentMethodCreate(PaymentMethodBase):
    pass

class PaymentMethod(PaymentMethodBase):
    payment_method_id: int

    class Config:
        orm_mode = True

class InvoiceStatusBase(BaseModel):
    name: str

class InvoiceStatusCreate(InvoiceStatusBase):
    pass

class InvoiceStatus(InvoiceStatusBase):
    invoice_status_id: int

    class Config:
        orm_mode = True

class InvoiceBase(BaseModel):
    appointment_id: int
    total_amount: Decimal
    date: date
    payment_method_id: int
    invoice_status_id: int

class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    invoice_id: int

    class Config:
        orm_mode = True

class MedicationInventoryBase(BaseModel):
    medication_name: str
    quantity: int
    expiration_date: date
    supplier_id: int

class MedicationInventoryCreate(MedicationInventoryBase):
    pass

class MedicationInventory(MedicationInventoryBase):
    inventory_id: int

    class Config:
        orm_mode = True

class RoleBase(BaseModel):
    role_name: str

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    role_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    role_id: int

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True

class WeekDayBase(BaseModel):
    day: str

class WeekDayCreate(WeekDayBase):
    pass

class WeekDay(WeekDayBase):
    week_day_id: int

    class Config:
        orm_mode = True

class ScheduleBase(BaseModel):
    staff_id: int
    week_day_id: int
    start_time: time
    end_time: time
    availability: bool

class ScheduleCreate(ScheduleBase):
    pass

class Schedule(ScheduleBase):
    schedule_id: int

    class Config:
        orm_mode = True