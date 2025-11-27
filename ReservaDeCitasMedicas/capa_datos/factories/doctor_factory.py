# ============================================================================
# CAPA DE DATOS - FACTORIES (PATRÓN CREACIONAL)
# Archivo: capa_datos/factories/doctor_factory.py
# ============================================================================

from abc import ABC, abstractmethod
from typing import List


class DoctorFactory(ABC):
    """
    Factory Method abstracto para crear doctores.
    
    PATRÓN DE DISEÑO: Factory Method (Creacional)
    PRINCIPIOS SOLID:
    - Open/Closed Principle: Abierto a extensión, cerrado a modificación
    - Liskov Substitution Principle: Todas las subclases pueden sustituir al padre
    - Dependency Inversion Principle: Depende de abstracción, no de implementación
    """
    
    @abstractmethod
    def crear_doctores(self) -> List:
        """Crea y retorna lista de doctores de una especialidad"""
        pass
    
    @abstractmethod
    def get_especialidad(self) -> str:
        """Retorna el nombre de la especialidad"""
        pass