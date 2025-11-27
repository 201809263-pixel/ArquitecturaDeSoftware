# ============================================================================
# CAPA DE DATOS - MODELOS
# Archivo: capa_datos/modelos/cita.py
# ============================================================================

class Cita:
    """
    Modelo de dominio que representa una Cita médica.
    
    PRINCIPIO SOLID: Single Responsibility Principle (SRP)
    - Responsabilidad única: Representar datos de una cita
    - Incluye método de presentación de sus propios datos
    """
    
    def __init__(self, paciente: str, doctor, fecha: str, hora: str):
        self._paciente = paciente
        self._doctor = doctor
        self._fecha = fecha
        self._hora = hora
    
    @property
    def paciente(self) -> str:
        return self._paciente
    
    @property
    def doctor(self):
        return self._doctor
    
    @property
    def fecha(self) -> str:
        return self._fecha
    
    @property
    def hora(self) -> str:
        return self._hora
    
    def mostrar_confirmacion(self) -> None:
        """Muestra la confirmación de la cita en formato legible"""
        print("\n" + "="*50)
        print("       ✓ CITA RESERVADA EXITOSAMENTE")
        print("="*50)
        print(f"\n📋 DATOS DE LA CITA:")
        print("-" * 50)
        print(f"Paciente:       {self._paciente}")
        print(f"Doctor:         {self._doctor.nombre}")
        print(f"Especialidad:   {self._doctor.especialidad}")
        print(f"Fecha:          {self._fecha}")
        print(f"Hora:           {self._hora}")
        print("-" * 50)
        print("\n¡Recuerde llegar 15 minutos antes de su cita!")
        print("="*50 + "\n")
    
    def __str__(self) -> str:
        return f"Cita de {self._paciente} con {self._doctor.nombre} el {self._fecha} a las {self._hora}"
    
    def __repr__(self) -> str:
        return f"Cita(paciente='{self._paciente}', doctor='{self._doctor.nombre}', fecha='{self._fecha}', hora='{self._hora}')"