# ============================================================================
# CAPA DE DATOS - REPOSITORIO
# Archivo: capa_datos/repositorios/repositorio_doctores.py
# ============================================================================

from typing import Dict, List, Optional
from capa_datos.factories.doctor_factory import DoctorFactory
from capa_datos.factories.implementaciones_factory import (
    DermatologiaFactory, GinecologiaFactory, EmergenciaFactory,
    OdontologiaFactory, OftalmologiaFactory, OtorrinolaringologiaFactory,
    TraumatologiaFactory, UrologiaFactory
)


class RepositorioDoctores:
    """
    Repositorio para gestionar el acceso a doctores.
    
    PRINCIPIO SOLID: Single Responsibility Principle (SRP)
    - Responsabilidad única: Gestionar el acceso a datos de doctores
    
    PRINCIPIO SOLID: Dependency Inversion Principle (DIP)
    - Depende de la abstracción DoctorFactory, no de implementaciones concretas
    """
    
    def __init__(self):
        """Inicializa el repositorio con todos los factories disponibles"""
        self._factories: Dict[str, DoctorFactory] = {
            "1": DermatologiaFactory(),
            "2": GinecologiaFactory(),
            "3": EmergenciaFactory(),
            "4": OdontologiaFactory(),
            "5": OftalmologiaFactory(),
            "6": OtorrinolaringologiaFactory(),
            "7": TraumatologiaFactory(),
            "8": UrologiaFactory()
        }
    
    def obtener_todas_especialidades(self) -> List[tuple]:
        """
        Retorna lista de todas las especialidades disponibles.
        
        Returns:
            List[tuple]: Lista de tuplas (key, nombre_especialidad)
        """
        return [(key, factory.get_especialidad()) 
                for key, factory in self._factories.items()]
    
    def obtener_doctores_por_especialidad(self, especialidad_key: str) -> Optional[List]:
        """
        Obtiene lista de doctores de una especialidad específica.
        
        Args:
            especialidad_key: Clave de la especialidad
            
        Returns:
            List[Doctor] si la especialidad existe, None en caso contrario
        """
        factory = self._factories.get(especialidad_key)
        if factory:
            return factory.crear_doctores()
        return None
    
    def obtener_factory_por_key(self, especialidad_key: str) -> Optional[DoctorFactory]:
        """
        Obtiene el factory de una especialidad específica.
        
        Args:
            especialidad_key: Clave de la especialidad
            
        Returns:
            DoctorFactory si existe, None en caso contrario
        """
        return self._factories.get(especialidad_key)
    
    def especialidad_existe(self, especialidad_key: str) -> bool:
        """
        Verifica si una especialidad existe.
        
        Args:
            especialidad_key: Clave de la especialidad
            
        Returns:
            bool: True si existe, False en caso contrario
        """
        return especialidad_key in self._factories
    
    def agregar_factory(self, key: str, factory: DoctorFactory) -> None:
        """
        Agrega un nuevo factory de especialidad.
        
        PRINCIPIO SOLID: Open/Closed Principle
        - Permite extender el sistema sin modificar código existente
        
        Args:
            key: Clave única para la especialidad
            factory: Factory de doctores a agregar
        """
        self._factories[key] = factory
    
    def get_numero_especialidades(self) -> int:
        """Retorna el número total de especialidades disponibles"""
        return len(self._factories)