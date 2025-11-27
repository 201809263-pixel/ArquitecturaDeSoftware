# ============================================================================
# CAPA DE NEGOCIO - SERVICIO DE CITAS
# Archivo: capa_negocio/servicios/servicio_citas.py
# ============================================================================

from typing import Optional, Tuple
from datetime import datetime, timedelta
from capa_datos.modelos.cita import Cita


class ServicioCitas:
    """
    Servicio para gestionar la lógica de negocio de citas.
    
    PRINCIPIO SOLID: Single Responsibility Principle (SRP)
    - Responsabilidad única: Gestionar creación y validación de citas
    
    PRINCIPIO SOLID: Dependency Inversion Principle (DIP)
    - Depende del servicio de validación (abstracción)
    """
    
    def __init__(self, servicio_validacion):
        """
        Inicializa el servicio de citas.
        
        Args:
            servicio_validacion: Servicio para validar horarios
        """
        self._servicio_validacion = servicio_validacion
    
    def crear_cita(self, paciente: str, doctor, hora: str) -> Tuple[Optional[Cita], str]:
        """
        Crea una nueva cita médica con validaciones.
        
        Args:
            paciente: Nombre del paciente
            doctor: Doctor asignado
            hora: Hora de la cita
            
        Returns:
            Tuple[Optional[Cita], str]: (Cita creada, mensaje)
        """
        # Validar nombre del paciente
        if not paciente or not paciente.strip():
            return None, "El nombre del paciente no puede estar vacío"
        
        # Validar formato de hora
        if not self._servicio_validacion.validar_formato_hora(hora):
            return None, "Formato de hora incorrecto. Use HH:MM (ejemplo: 14:30)"
        
        # Validar disponibilidad de horario
        if not self._servicio_validacion.validar_horario_disponible(hora, doctor):
            return None, "Horario no disponible o lleno"
        
        # Calcular fecha de la cita (día siguiente)
        fecha = self._calcular_fecha_proxima()
        
        # Crear la cita
        cita = Cita(paciente, doctor, fecha, hora)
        return cita, "Cita creada exitosamente"
    
    def _calcular_fecha_proxima(self) -> str:
        """
        Calcula la fecha del día siguiente.
        
        Returns:
            str: Fecha formateada (DD/MM/YYYY)
        """
        manana = datetime.now() + timedelta(days=1)
        return manana.strftime("%d/%m/%Y")
    
    def validar_paciente(self, nombre: str) -> bool:
        """
        Valida que el nombre del paciente sea válido.
        
        Args:
            nombre: Nombre del paciente
            
        Returns:
            bool: True si es válido
        """
        return bool(nombre and nombre.strip())