# ============================================================================
# CAPA DE NEGOCIO - IMPLEMENTACIONES DE STRATEGIES
# Archivo: capa_negocio/strategies/implementaciones_strategy.py
# ============================================================================

from datetime import datetime, timedelta
from capa_negocio.strategies.validacion_strategy import ValidacionStrategy


class ValidacionHorarioEstandar(ValidacionStrategy):
    """
    Estrategia de validación estándar.
    Acepta cualquier hora dentro del rango del doctor.
    """
    
    def validar(self, hora_cita: str, doctor) -> bool:
        """Valida que la hora esté dentro del horario del doctor"""
        formato = "%H:%M"
        try:
            cita = datetime.strptime(hora_cita, formato)
            inicio = datetime.strptime(doctor.horario_inicio, formato)
            fin = datetime.strptime(doctor.horario_fin, formato)
            return inicio <= cita <= fin
        except ValueError:
            return False
    
    def get_descripcion(self) -> str:
        return "Estándar: Cualquier horario dentro del rango del doctor"


class ValidacionHorarioEstricto(ValidacionStrategy):
    """
    Estrategia de validación estricta.
    Solo acepta horas en punto (sin minutos).
    """
    
    def validar(self, hora_cita: str, doctor) -> bool:
        """Valida que sea hora en punto y esté en el rango del doctor"""
        formato = "%H:%M"
        try:
            cita = datetime.strptime(hora_cita, formato)
            
            # Solo permite horas en punto
            if cita.minute != 0:
                return False
            
            inicio = datetime.strptime(doctor.horario_inicio, formato)
            fin = datetime.strptime(doctor.horario_fin, formato)
            return inicio <= cita <= fin
        except ValueError:
            return False
    
    def get_descripcion(self) -> str:
        return "Estricto: Solo horas en punto (ej: 08:00, 14:00)"


class ValidacionHorarioFlexible(ValidacionStrategy):
    """
    Estrategia de validación flexible.
    Permite 30 minutos antes y después del horario establecido.
    """
    
    def validar(self, hora_cita: str, doctor) -> bool:
        """Valida con margen de 30 minutos antes/después"""
        formato = "%H:%M"
        try:
            cita = datetime.strptime(hora_cita, formato)
            inicio = datetime.strptime(doctor.horario_inicio, formato)
            fin = datetime.strptime(doctor.horario_fin, formato)
            
            # Permite 30 minutos de flexibilidad
            inicio_flex = inicio - timedelta(minutes=30)
            fin_flex = fin + timedelta(minutes=30)
            
            return inicio_flex <= cita <= fin_flex
        except ValueError:
            return False
    
    def get_descripcion(self) -> str:
        return "Flexible: Permite 30 minutos antes/después del horario"