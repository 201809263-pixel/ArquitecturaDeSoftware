# ============================================================================
# CAPA DE DATOS - MODELOS
# Archivo: capa_datos/modelos/doctor.py
# ============================================================================

class Doctor:
    """
    Modelo de dominio que representa a un Doctor.
    
    PRINCIPIO SOLID: Single Responsibility Principle (SRP)
    - Responsabilidad única: Representar datos de un doctor
    - No contiene lógica de negocio ni acceso a datos
    """
    
    def __init__(self, nombre: str, horario_inicio: str, horario_fin: str, especialidad: str):
        self._nombre = nombre
        self._horario_inicio = horario_inicio
        self._horario_fin = horario_fin
        self._especialidad = especialidad
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def horario_inicio(self) -> str:
        return self._horario_inicio
    
    @property
    def horario_fin(self) -> str:
        return self._horario_fin
    
    @property
    def especialidad(self) -> str:
        return self._especialidad
    
    def __str__(self) -> str:
        return f"{self._nombre} - {self._especialidad} ({self._horario_inicio} - {self._horario_fin})"
    
    def __repr__(self) -> str:
        return f"Doctor(nombre='{self._nombre}', especialidad='{self._especialidad}')"