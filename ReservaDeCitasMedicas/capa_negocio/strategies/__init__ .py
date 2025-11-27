"""
STRATEGIES
==========

Implementaciones del patrón Strategy (Comportamiento).
Define familias de algoritmos intercambiables.

Clases:
- ValidacionStrategy: Interfaz abstracta para estrategias de validación
- ValidadorCitas: Contexto que usa las estrategias
- ValidacionHorarioEstandar: Estrategia de validación estándar
- ValidacionHorarioEstricto: Estrategia de validación estricta
- ValidacionHorarioFlexible: Estrategia de validación flexible
"""

from capa_negocio.strategies.validacion_strategy import (
    ValidacionStrategy,
    ValidadorCitas
)
from capa_negocio.strategies.implementaciones_strategy import (
    ValidacionHorarioEstandar,
    ValidacionHorarioEstricto,
    ValidacionHorarioFlexible
)

__all__ = [
    'ValidacionStrategy',
    'ValidadorCitas',
    'ValidacionHorarioEstandar',
    'ValidacionHorarioEstricto',
    'ValidacionHorarioFlexible'
]