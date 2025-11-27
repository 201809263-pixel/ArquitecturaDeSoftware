#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SISTEMA DE RESERVA DE CITAS MÉDICAS
====================================

Arquitectura: 3 Capas
- Capa de Presentación: Interfaz de usuario
- Capa de Negocio: Lógica de negocio y patrones
- Capa de Datos: Modelos y acceso a datos

Patrones de Diseño:
- Factory Method (Creacional): Creación de doctores
- Facade (Estructural): Interfaz simplificada del sistema
- Strategy (Comportamiento): Validación de horarios

Principios SOLID:
✓ S - Single Responsibility Principle
✓ O - Open/Closed Principle
✓ L - Liskov Substitution Principle
✓ I - Interface Segregation Principle
✓ D - Dependency Inversion Principle

Autor: [Tu Nombre]
Fecha: Noviembre 2025
"""

# ============================================================================
# IMPORTS
# ============================================================================

# Capa de Negocio
from capa_negocio.facades.sistema_citas_facade import SistemaCitasFacade

# Capa de Presentación
from capa_presentacion.interfaz_consola import InterfazConsola


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Función principal del sistema.
    
    Crea las instancias necesarias y ejecuta la aplicación.
    
    ARQUITECTURA DE 3 CAPAS EN ACCIÓN:
    1. Se crea el Facade (Capa de Negocio)
    2. Se crea la Interfaz (Capa de Presentación)
    3. La Interfaz usa el Facade
    4. El Facade coordina Servicios y Repositorios
    5. Los Servicios usan Strategies y Factories
    6. Los Repositorios acceden a los Datos
    
    INVERSIÓN DE DEPENDENCIAS (DIP):
    - La Presentación depende de la Negocio (Facade)
    - La Negocio depende de abstracciones (Strategies, Factories)
    - Las capas superiores no conocen detalles de implementación
    """
    
    # Crear instancia del Facade (Capa de Negocio)
    # El Facade internamente crea todos los subsistemas necesarios:
    # - RepositorioDoctores
    # - ServicioValidacion
    # - ServicioCitas
    facade = SistemaCitasFacade()
    
    # Crear instancia de la Interfaz (Capa de Presentación)
    # La interfaz solo conoce el Facade, no los subsistemas internos
    interfaz = InterfazConsola(facade)
    
    # Ejecutar el sistema
    interfaz.ejecutar()


# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    """
    Punto de entrada del programa.
    
    Este bloque se ejecuta solo cuando el script se ejecuta directamente,
    no cuando se importa como módulo.
    """
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido por el usuario.")
        print("¡Hasta luego! 👋\n")
    except Exception as e:
        print(f"\n❌ Error crítico: {e}")
        print("Por favor, reporte este error al administrador del sistema.\n")