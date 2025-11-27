# ============================================================================
# CAPA DE NEGOCIO - STRATEGIES (PATRÓN DE COMPORTAMIENTO)
# Archivo: capa_negocio/strategies/validacion_strategy.py
# ============================================================================

from abc import ABC, abstractmethod


class ValidacionStrategy(ABC):
    """
    Estrategia abstracta para validar disponibilidad de horarios.
    
    PATRÓN DE DISEÑO: Strategy (Comportamiento)
    PRINCIPIOS SOLID:
    - Open/Closed Principle: Abierto a extensión (nuevas estrategias)
    - Liskov Substitution Principle: Todas las estrategias son intercambiables
    - Interface Segregation Principle: Interfaz específica y mínima
    """
    
    @abstractmethod
    def validar(self, hora_cita: str, doctor) -> bool:
        """
        Valida si una hora de cita es válida para un doctor.
        
        Args:
            hora_cita: Hora solicitada en formato HH:MM
            doctor: Doctor para el cual se valida el horario
            
        Returns:
            bool: True si es válido, False en caso contrario
        """
        pass
    
    @abstractmethod
    def get_descripcion(self) -> str:
        """Retorna descripción de la estrategia de validación"""
        pass


class ValidadorCitas:
    """
    Contexto que utiliza una estrategia de validación.
    
    PRINCIPIO SOLID: Dependency Inversion Principle (DIP)
    - Depende de la abstracción ValidacionStrategy, no de implementaciones concretas
    """
    
    def __init__(self, strategy: ValidacionStrategy):
        """
        Inicializa el validador con una estrategia.
        
        Args:
            strategy: Estrategia de validación a utilizar
        """
        self._strategy = strategy
    
    def set_strategy(self, strategy: ValidacionStrategy) -> None:
        """
        Cambia la estrategia de validación en tiempo de ejecución.
        
        Args:
            strategy: Nueva estrategia a utilizar
        """
        self._strategy = strategy
    
    def es_horario_valido(self, hora_cita: str, doctor) -> bool:
        """
        Valida un horario usando la estrategia configurada.
        
        Args:
            hora_cita: Hora a validar
            doctor: Doctor para el cual validar
            
        Returns:
            bool: True si es válido según la estrategia
        """
        return self._strategy.validar(hora_cita, doctor)
    
    def get_descripcion_estrategia(self) -> str:
        """Retorna la descripción de la estrategia actual"""
        return self._strategy.get_descripcion()