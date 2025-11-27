"""
MODELOS
=======

Entidades de dominio del sistema.

Clases:
- Doctor: Modelo que representa a un doctor
- Cita: Modelo que representa una cita médica
"""

from capa_datos.modelos.doctor import Doctor
from capa_datos.modelos.cita import Cita

__all__ = ['Doctor', 'Cita']