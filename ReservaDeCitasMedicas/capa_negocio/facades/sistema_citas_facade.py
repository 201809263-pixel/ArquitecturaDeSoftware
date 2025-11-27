# ============================================================================
# CAPA DE NEGOCIO - FACADE (PATRÓN ESTRUCTURAL)
# Archivo: capa_negocio/facades/sistema_citas_facade.py
# ============================================================================

from typing import List, Optional, Tuple
from capa_datos.repositorios.repositorio_doctores import RepositorioDoctores
from capa_negocio.servicios.servicio_validacion import ServicioValidacion
from capa_negocio.servicios.servicio_citas import ServicioCitas


class SistemaCitasFacade:
    """
    Facade que proporciona una interfaz simplificada al sistema de citas.
    
    PATRÓN DE DISEÑO: Facade (Estructural)
    - Simplifica la interacción con múltiples subsistemas
    - Oculta la complejidad interna del sistema
    - Proporciona una interfaz unificada
    
    PRINCIPIOS SOLID:
    - Single Responsibility: Coordinar subsistemas
    - Dependency Inversion: Depende de abstracciones (servicios, repositorios)
    - Interface Segregation: Interfaz clara y específica
    
    SUBSISTEMAS COORDINADOS:
    1. RepositorioDoctores (Acceso a datos)
    2. ServicioValidacion (Validación de horarios)
    3. ServicioCitas (Lógica de negocio de citas)
    """
    
    def __init__(self):
        """Inicializa el Facade con todos los subsistemas necesarios"""
        # Capa de Datos
        self._repositorio_doctores = RepositorioDoctores()
        
        # Capa de Negocio - Servicios
        self._servicio_validacion = ServicioValidacion()
        self._servicio_citas = ServicioCitas(self._servicio_validacion)
    
    # ========================================================================
    # MÉTODOS RELACIONADOS CON ESPECIALIDADES
    # ========================================================================
    
    def obtener_especialidades(self) -> List[Tuple[str, str]]:
        """
        Obtiene todas las especialidades disponibles.
        
        Returns:
            List[Tuple[str, str]]: Lista de tuplas (key, nombre_especialidad)
        """
        return self._repositorio_doctores.obtener_todas_especialidades()
    
    def especialidad_existe(self, especialidad_key: str) -> bool:
        """
        Verifica si una especialidad existe.
        
        Args:
            especialidad_key: Clave de la especialidad
            
        Returns:
            bool: True si existe
        """
        return self._repositorio_doctores.especialidad_existe(especialidad_key)
    
    # ========================================================================
    # MÉTODOS RELACIONADOS CON DOCTORES
    # ========================================================================
    
    def obtener_doctores(self, especialidad_key: str) -> Optional[List]:
        """
        Obtiene doctores de una especialidad específica.
        
        Args:
            especialidad_key: Clave de la especialidad
            
        Returns:
            List[Doctor] o None si no existe la especialidad
        """
        return self._repositorio_doctores.obtener_doctores_por_especialidad(especialidad_key)
    
    def obtener_nombre_especialidad(self, especialidad_key: str) -> Optional[str]:
        """
        Obtiene el nombre de una especialidad.
        
        Args:
            especialidad_key: Clave de la especialidad
            
        Returns:
            str con el nombre o None si no existe
        """
        factory = self._repositorio_doctores.obtener_factory_por_key(especialidad_key)
        if factory:
            return factory.get_especialidad()
        return None
    
    # ========================================================================
    # MÉTODOS RELACIONADOS CON VALIDACIÓN
    # ========================================================================
    
    def cambiar_estrategia_validacion(self, tipo: str) -> bool:
        """
        Cambia la estrategia de validación de horarios.
        
        Args:
            tipo: Tipo de estrategia ("1", "2", o "3")
            
        Returns:
            bool: True si se cambió exitosamente
        """
        return self._servicio_validacion.cambiar_estrategia(tipo)
    
    def obtener_estrategias_validacion(self) -> dict:
        """
        Obtiene las estrategias de validación disponibles.
        
        Returns:
            dict: Diccionario con estrategias y descripciones
        """
        return self._servicio_validacion.obtener_estrategias_disponibles()
    
    def obtener_estrategia_actual(self) -> str:
        """
        Obtiene la descripción de la estrategia actual.
        
        Returns:
            str: Descripción de la estrategia
        """
        return self._