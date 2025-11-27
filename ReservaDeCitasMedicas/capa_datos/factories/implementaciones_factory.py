# ============================================================================
# CAPA DE DATOS - IMPLEMENTACIONES DE FACTORIES
# Archivo: capa_datos/factories/implementaciones_factory.py
# ============================================================================

from typing import List
from capa_datos.factories.doctor_factory import DoctorFactory
from capa_datos.modelos.doctor import Doctor


class DermatologiaFactory(DoctorFactory):
    """Factory concreto para crear doctores de Dermatología"""
    
    def crear_doctores(self) -> List[Doctor]:
        return [
            Doctor("Dr. Carlos Mendoza", "08:00", "14:00", "Dermatología"),
            Doctor("Dra. Ana López", "14:00", "20:00", "Dermatología"),
            Doctor("Dr. Roberto Vargas", "09:00", "15:00", "Dermatología")
        ]
    
    def get_especialidad(self) -> str:
        return "Dermatología"


class GinecologiaFactory(DoctorFactory):
    """Factory concreto para crear doctores de Ginecología"""
    
    def crear_doctores(self) -> List[Doctor]:
        return [
            Doctor("Dra. María Fernández", "07:00", "13:00", "Ginecología y obstetricia"),
            Doctor("Dr. José Ramírez", "13:00", "19:00", "Ginecología y obstetricia"),
            Doctor("Dra. Patricia González", "08:00", "16:00", "Ginecología y obstetricia")
        ]
    
    def get_especialidad(self) -> str:
        return "Ginecología y obstetricia"


class EmergenciaFactory(DoctorFactory):
    """Factory concreto para crear doctores de Medicina de emergencia"""
    
    def crear_doctores(self) -> List[Doctor]:
        return [
            Doctor("Dr. Miguel Torres", "00:00", "08:00", "Medicina de emergencia"),
            Doctor("Dra. Laura Sánchez", "08:00", "16:00", "Medicina de emergencia"),
            Doctor("Dr. Fernando Cruz", "16:00", "23:59", "Medicina de emergencia")
        ]
    
    def get_especialidad(self) -> str:
        return "Medicina de emergencia"


class OdontologiaFactory(DoctorFactory):
    """Factory concreto para crear doctores de Odontología"""
    
    def crear_doctores(self) -> List[Doctor]:
        return [
            Doctor("Dr. Pedro Martínez", "08:00", "14:00", "Odontología"),
            Doctor("Dra. Sofía Herrera", "14:00", "20:00", "Odontología"),
            Doctor("Dr. Luis Castillo", "09:00", "17:00", "Odontología")
        ]
    
    def get_especialidad(self) -> str:
        return "Odontología"


class OftalmologiaFactory(DoctorFactory):
    """Factory concreto para crear doctores de Oftalmología"""
    
    def crear_doctores(self) -> List[Doctor]:
        return [
            Doctor("Dr. Ricardo Flores", "07:00", "13:00", "Oftalmología"),
            Doctor("Dra. Carmen Rojas", "13:00", "19:00", "Oftalmología"),
            Doctor("Dr. Alberto Díaz", "08:00", "14:00", "Oftalmología")
        ]
    
    def get_especialidad(self) -> str:
        return "Oftalmología"


class OtorrinolaringologiaFactory(DoctorFactory):
    """Factory concreto para crear doctores de Otorrinolaringología"""
    
    def crear_doctores(self) -> List[Doctor]:
        return [
            Doctor("Dr. Javier Morales", "08:00", "15:00", "Otorrinolaringología"),
            Doctor("Dra. Elena Vega", "15:00", "22:00", "Otorrinolaringología"),
            Doctor("Dr. Andrés Ortiz", "09:00", "16:00", "Otorrinolaringología")
        ]
    
    def get_especialidad(self) -> str:
        return "Otorrinolaringología"


class TraumatologiaFactory(DoctorFactory):
    """Factory concreto para crear doctores de Traumatología"""
    
    def crear_doctores(self) -> List[Doctor]:
        return [
            Doctor("Dr. Gabriel Ruiz", "07:00", "14:00", "Traumatología y Ortopedia"),
            Doctor("Dra. Mónica Silva", "14:00", "21:00", "Traumatología y Ortopedia"),
            Doctor("Dr. Diego Campos", "08:00", "15:00", "Traumatología y Ortopedia")
        ]
    
    def get_especialidad(self) -> str:
        return "Traumatología y Ortopedia"


class UrologiaFactory(DoctorFactory):
    """Factory concreto para crear doctores de Urología"""
    
    def crear_doctores(self) -> List[Doctor]:
        return [
            Doctor("Dr. Raúl Navarro", "08:00", "14:00", "Urología"),
            Doctor("Dra. Isabel Medina", "14:00", "20:00", "Urología"),
            Doctor("Dr. Francisco Paredes", "09:00", "17:00", "Urología")
        ]
    
    def get_especialidad(self) -> str:
        return "Urología"