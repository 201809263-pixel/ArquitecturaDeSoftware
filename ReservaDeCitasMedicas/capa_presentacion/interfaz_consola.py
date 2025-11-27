# ============================================================================
# CAPA DE PRESENTACIÓN - INTERFAZ DE CONSOLA
# Archivo: capa_presentacion/interfaz_consola.py
# ============================================================================

from typing import Optional, Any


class InterfazConsola:
    """
    Interfaz de usuario por consola para el sistema de citas.
    
    PRINCIPIO SOLID: Single Responsibility Principle (SRP)
    - Responsabilidad única: Manejar interacción con usuario (I/O)
    - NO contiene lógica de negocio
    - NO accede directamente a datos
    
    PRINCIPIO SOLID: Dependency Inversion Principle (DIP)
    - Depende del Facade (abstracción de alto nivel)
    - No conoce detalles de implementación interna
    """
    
    def __init__(self, facade):
        """
        Inicializa la interfaz con el facade del sistema.
        
        Args:
            facade: Facade que coordina el sistema de citas
        """
        self._facade = facade
    
    # ========================================================================
    # MÉTODOS DE PRESENTACIÓN
    # ========================================================================
    
    def mostrar_banner_bienvenida(self) -> None:
        """Muestra el banner de bienvenida del sistema"""
        print("\n╔════════════════════════════════════════════════╗")
        print("║     SISTEMA DE RESERVA DE CITAS MÉDICAS       ║")
        print("╠════════════════════════════════════════════════╣")
        print("║  ARQUITECTURA: 3 CAPAS                         ║")
        print("║  PATRONES: Factory, Facade, Strategy           ║")
        print("║  PRINCIPIOS: SOLID                             ║")
        print("╚════════════════════════════════════════════════╝")
    
    def mostrar_menu_especialidades(self) -> None:
        """Muestra el menú de especialidades disponibles"""
        print("\n" + "="*50)
        print("    ESPECIALIDADES MÉDICAS DISPONIBLES")
        print("="*50)
        especialidades = self._facade.obtener_especialidades()
        for key, nombre in especialidades:
            print(f"{key}. {nombre}")
        print("="*50)
    
    def mostrar_menu_validacion(self) -> None:
        """Muestra el menú de tipos de validación"""
        print("\n" + "="*50)
        print("    TIPO DE VALIDACIÓN DE HORARIO")
        print("="*50)
        estrategias = self._facade.obtener_estrategias_validacion()
        for key, descripcion in estrategias.items():
            print(f"{key}. {descripcion}")
        print("="*50)
    
    def mostrar_doctores(self, doctores: list, especialidad: str) -> None:
        """
        Muestra la lista de doctores de una especialidad.
        
        Args:
            doctores: Lista de doctores a mostrar
            especialidad: Nombre de la especialidad
        """
        print(f"\n{'='*50}")
        print(f"    DOCTORES EN {especialidad.upper()}")
        print("="*50)
        for i, doctor in enumerate(doctores, 1):
            print(f"{i}. {doctor}")
        print("="*50)
    
    def mostrar_error(self, mensaje: str) -> None:
        """
        Muestra un mensaje de error.
        
        Args:
            mensaje: Mensaje de error a mostrar
        """
        print(f"\n❌ {mensaje}")
    
    def mostrar_exito(self, mensaje: str) -> None:
        """
        Muestra un mensaje de éxito.
        
        Args:
            mensaje: Mensaje de éxito a mostrar
        """
        print(f"\n✓ {mensaje}")
    
    def mostrar_info(self, mensaje: str) -> None:
        """
        Muestra un mensaje informativo.
        
        Args:
            mensaje: Mensaje informativo a mostrar
        """
        print(f"\nℹ️  {mensaje}")
    
    # ========================================================================
    # MÉTODOS DE ENTRADA DE DATOS
    # ========================================================================
    
    def solicitar_tipo_validacion(self) -> str:
        """
        Solicita al usuario el tipo de validación.
        
        Returns:
            str: Tipo de validación seleccionado
        """
        return input("\nSeleccione tipo de validación (Enter para estándar): ").strip()
    
    def solicitar_especialidad(self) -> str:
        """
        Solicita al usuario la especialidad.
        
        Returns:
            str: Key de la especialidad seleccionada
        """
        return input("\nSeleccione el número de la especialidad: ").strip()
    
    def solicitar_numero_doctor(self) -> str:
        """
        Solicita al usuario el número del doctor.
        
        Returns:
            str: Número del doctor seleccionado
        """
        return input("\nSeleccione el número del doctor: ").strip()
    
    def solicitar_nombre_paciente(self) -> str:
        """
        Solicita al usuario el nombre del paciente.
        
        Returns:
            str: Nombre del paciente
        """
        print("\n" + "-" * 50)
        return input("Ingrese el nombre del paciente: ").strip()
    
    def solicitar_hora_cita(self) -> str:
        """
        Solicita al usuario la hora de la cita.
        
        Returns:
            str: Hora de la cita en formato HH:MM
        """
        return input("Ingrese la hora de la cita (formato HH:MM, ej: 10:30): ").strip()
    
    def solicitar_continuar(self) -> bool:
        """
        Pregunta al usuario si desea continuar.
        
        Returns:
            bool: True si desea continuar, False en caso contrario
        """
        respuesta = input("\n¿Desea reservar otra cita? (s/n): ").strip().lower()
        return respuesta == 's'
    
    # ========================================================================
    # MÉTODO PRINCIPAL DE RESERVA
    # ========================================================================
    
    def reservar_cita(self) -> None:
        """
        Ejecuta el flujo completo de reserva de una cita.
        
        Este método coordina toda la interacción con el usuario,
        delegando la lógica de negocio al Facade.
        """
        try:
            # Paso 1: Mostrar y seleccionar tipo de validación
            self.mostrar_menu_validacion()
            tipo_validacion = self.solicitar_tipo_validacion()
            
            if tipo_validacion in ["1", "2", "3"]:
                if self._facade.cambiar_estrategia_validacion(tipo_validacion):
                    self.mostrar_info(f"Estrategia seleccionada: {self._facade.obtener_estrategia_actual()}")
            
            # Paso 2: Mostrar y seleccionar especialidad
            self.mostrar_menu_especialidades()
            especialidad_key = self.solicitar_especialidad()
            
            if not self._facade.especialidad_existe(especialidad_key):
                self.mostrar_error("Especialidad no válida.")
                return
            
            # Paso 3: Obtener y mostrar doctores
            doctores = self._facade.obtener_doctores(especialidad_key)
            especialidad = self._facade.obtener_nombre_especialidad(especialidad_key)
            
            if not doctores:
                self.mostrar_error("No hay doctores disponibles para esta especialidad.")
                return
            
            self.mostrar_doctores(doctores, especialidad)
            
            # Paso 4: Seleccionar doctor
            doctor_num = self.solicitar_numero_doctor()
            doctor_seleccionado = self._validar_y_obtener_doctor(doctor_num, doctores)
            
            if not doctor_seleccionado:
                return
            
            # Paso 5: Ingresar datos del paciente
            nombre_paciente = self.solicitar_nombre_paciente()
            
            if not self._facade.validar_paciente(nombre_paciente):
                self.mostrar_error("El nombre del paciente no puede estar vacío.")
                return
            
            # Paso 6: Ingresar hora de la cita
            hora_cita = self.solicitar_hora_cita()
            
            # Paso 7: Crear la cita usando el Facade
            cita, mensaje = self._facade.crear_cita(nombre_paciente, doctor_seleccionado, hora_cita)
            
            if cita:
                cita.mostrar_confirmacion()
            else:
                self.mostrar_error(mensaje)
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Reserva cancelada por el usuario.")
        except Exception as e:
            self.mostrar_error(f"Error inesperado: {e}")
    
    def _validar_y_obtener_doctor(self, doctor_num: str, doctores: list) -> Optional[Any]:
        """
        Valida la selección del doctor y lo retorna.
        
        Args:
            doctor_num: Número ingresado por el usuario
            doctores: Lista de doctores disponibles
            
        Returns:
            Doctor seleccionado o None si es inválido
        """
        try:
            doctor_index = int(doctor_num) - 1
            if doctor_index < 0 or doctor_index >= len(doctores):
                self.mostrar_error("Número de doctor no válido.")
                return None
            return doctores[doctor_index]
        except ValueError:
            self.mostrar_error("Debe ingresar un número válido.")
            return None
    
    # ========================================================================
    # MÉTODO DE EJECUCIÓN PRINCIPAL
    # ========================================================================
    
    def ejecutar(self) -> None:
        """
        Ejecuta el sistema de citas médicas.
        
        Este es el método principal que mantiene el sistema en ejecución
        hasta que el usuario decida salir.
        """
        self.mostrar_banner_bienvenida()
        
        while True:
            self.reservar_cita()
            
            if not self.solicitar_continuar():
                print("\n╔════════════════════════════════════════════╗")
                print("║  ¡Gracias por usar nuestro sistema!       ║")
                print("║  ¡Que tenga un excelente día! 👋          ║")
                print("╚════════════════════════════════════════════╝\n")
                break