# ============================================================================
# CAPA DE NEGOCIO - SERVICIO DE VALIDACIÓN
# Archivo: capa_negocio/servicios/servicio_validacion.py
# ============================================================================

from datetime import datetime
from capa_negocio.strategies.validacion_strategy import ValidadorCitas
from capa_negocio.strategies.implementaciones_strategy import (
    ValidacionHorarioEstandar,
    ValidacionHorarioEstricto,
    ValidacionHorarioFlexible
)


class ServicioValidacion:
    """
    Servicio para gestionar validaciones de horarios.
    
    PRINCIPIO SOLID: Single Responsibility Principle (SRP)
    - Responsabilidad única: Validar horarios y formatos
    """
    
    def __init__(self):
        """Inicializa el servicio con validación estándar por defecto"""
        self._validador = ValidadorCitas(ValidacionHorarioEstandar())
        self._estrategias_disponibles = {
            "1": ValidacionHorarioEstandar(),
            "2": ValidacionHorarioEstricto(),
            "3": ValidacionHorarioFlexible()
        }
    
    def cambiar_estrategia(self, tipo: str) -> bool:
        """
        Cambia la estrategia de validación.
        
        Args:
            tipo: Tipo de estrategia ("1", "2", o "3")
            
        Returns:
            bool: True si se cambió exitosamente
        """
        if tipo in self._estrategias_disponibles:
            self._validador.set_strategy(self._estrategias_disponibles[tipo])
            return True
        return False
    
    def validar_formato_hora(self, hora_str: str) -> bool:
        """
        Valida que la hora tenga formato HH:MM correcto.
        
        Args:
            hora_str: String de hora a validar
            
        Returns:
            bool: True si el formato es válido
        """
        try:
            datetime.strptime(hora_str, "%H:%M")
            return True
        except ValueError:
            return False
    
    def validar_horario_disponible(self, hora_cita: str, doctor) -> bool:
        """
        Valida que el horario esté disponible según la estrategia activa.
        
        Args:
            hora_cita: Hora solicitada
            doctor: Doctor para validar
            
        Returns:
            bool: True si está disponible
        """
        return self._validador.es_horario_valido(hora_cita, doctor)
    
    def obtener_estrategias_disponibles(self) -> dict:
        """Retorna diccionario con estrategias y sus descripciones"""
        return {
            key: strategy.get_descripcion() 
            for key, strategy in self._estrategias_disponibles.items()
        }
    
    def get_estrategia_actual(self) -> str:
        """Retorna descripción de la estrategia actual"""
        return self._validador.get_descripcion_estrategia()