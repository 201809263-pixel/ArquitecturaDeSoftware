"""
FACTORIES
=========

Implementaciones del patrón Factory Method (Creacional).
Delega la creación de objetos a subclases especializadas.

Clases:
- DoctorFactory: Factory abstracto para crear doctores
- DermatologiaFactory: Factory para doctores de dermatología
- GinecologiaFactory: Factory para doctores de ginecología
- EmergenciaFactory: Factory para doctores de emergencia
- OdontologiaFactory: Factory para doctores de odontología
- OftalmologiaFactory: Factory para doctores de oftalmología
- OtorrinolaringologiaFactory: Factory para doctores de otorrinolaringología
- TraumatologiaFactory: Factory para doctores de traumatología
- UrologiaFactory: Factory para doctores de urología
"""

from capa_datos.factories.doctor_factory import DoctorFactory
from capa_datos.factories.implementaciones_factory import (
    DermatologiaFactory,
    GinecologiaFactory,
    EmergenciaFactory,
    OdontologiaFactory,
    OftalmologiaFactory,
    OtorrinolaringologiaFactory,
    TraumatologiaFactory,
    UrologiaFactory
)

__all__ = [
    'DoctorFactory',
    'DermatologiaFactory',
    'GinecologiaFactory',
    'EmergenciaFactory',
    'OdontologiaFactory',
    'OftalmologiaFactory',
    'OtorrinolaringologiaFactory',
    'TraumatologiaFactory',
    'UrologiaFactory'
]