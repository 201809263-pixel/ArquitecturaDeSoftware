from datetime import datetime, timedelta
from abc import ABC, abstractmethod

# ============================================================================
# PATRÓN CREACIONAL: FACTORY METHOD
# ============================================================================
class Doctor:
    """Clase base para todos los doctores"""
    def __init__(self, nombre, horario_inicio, horario_fin, especialidad):
        self.nombre = nombre
        self.horario_inicio = horario_inicio
        self.horario_fin = horario_fin
        self.especialidad = especialidad
    
    def __str__(self):
        return f"{self.nombre} - {self.especialidad} ({self.horario_inicio} - {self.horario_fin})"


class DoctorFactory(ABC):
    """Factory abstracto para crear doctores"""
    @abstractmethod
    def crear_doctores(self):
        pass
    
    @abstractmethod
    def get_especialidad(self):
        pass


class DermatologiaFactory(DoctorFactory):
    def crear_doctores(self):
        return [
            Doctor("Dr. Carlos Mendoza", "08:00", "14:00", "Dermatología"),
            Doctor("Dra. Ana López", "14:00", "20:00", "Dermatología"),
            Doctor("Dr. Roberto Vargas", "09:00", "15:00", "Dermatología")
        ]
    
    def get_especialidad(self):
        return "Dermatología"


class GinecologiaFactory(DoctorFactory):
    def crear_doctores(self):
        return [
            Doctor("Dra. María Fernández", "07:00", "13:00", "Ginecología y obstetricia"),
            Doctor("Dr. José Ramírez", "13:00", "19:00", "Ginecología y obstetricia"),
            Doctor("Dra. Patricia González", "08:00", "16:00", "Ginecología y obstetricia")
        ]
    
    def get_especialidad(self):
        return "Ginecología y obstetricia"


class EmergenciaFactory(DoctorFactory):
    def crear_doctores(self):
        return [
            Doctor("Dr. Miguel Torres", "00:00", "08:00", "Medicina de emergencia"),
            Doctor("Dra. Laura Sánchez", "08:00", "16:00", "Medicina de emergencia"),
            Doctor("Dr. Fernando Cruz", "16:00", "23:59", "Medicina de emergencia")
        ]
    
    def get_especialidad(self):
        return "Medicina de emergencia"


class OdontologiaFactory(DoctorFactory):
    def crear_doctores(self):
        return [
            Doctor("Dr. Pedro Martínez", "08:00", "14:00", "Odontología"),
            Doctor("Dra. Sofía Herrera", "14:00", "20:00", "Odontología"),
            Doctor("Dr. Luis Castillo", "09:00", "17:00", "Odontología")
        ]
    
    def get_especialidad(self):
        return "Odontología"


class OftalmologiaFactory(DoctorFactory):
    def crear_doctores(self):
        return [
            Doctor("Dr. Ricardo Flores", "07:00", "13:00", "Oftalmología"),
            Doctor("Dra. Carmen Rojas", "13:00", "19:00", "Oftalmología"),
            Doctor("Dr. Alberto Díaz", "08:00", "14:00", "Oftalmología")
        ]
    
    def get_especialidad(self):
        return "Oftalmología"


class OtorrinolaringologiaFactory(DoctorFactory):
    def crear_doctores(self):
        return [
            Doctor("Dr. Javier Morales", "08:00", "15:00", "Otorrinolaringología"),
            Doctor("Dra. Elena Vega", "15:00", "22:00", "Otorrinolaringología"),
            Doctor("Dr. Andrés Ortiz", "09:00", "16:00", "Otorrinolaringología")
        ]
    
    def get_especialidad(self):
        return "Otorrinolaringología"


class TraumatologiaFactory(DoctorFactory):
    def crear_doctores(self):
        return [
            Doctor("Dr. Gabriel Ruiz", "07:00", "14:00", "Traumatología y Ortopedia"),
            Doctor("Dra. Mónica Silva", "14:00", "21:00", "Traumatología y Ortopedia"),
            Doctor("Dr. Diego Campos", "08:00", "15:00", "Traumatología y Ortopedia")
        ]
    
    def get_especialidad(self):
        return "Traumatología y Ortopedia"


class UrologiaFactory(DoctorFactory):
    def crear_doctores(self):
        return [
            Doctor("Dr. Raúl Navarro", "08:00", "14:00", "Urología"),
            Doctor("Dra. Isabel Medina", "14:00", "20:00", "Urología"),
            Doctor("Dr. Francisco Paredes", "09:00", "17:00", "Urología")
        ]
    
    def get_especialidad(self):
        return "Urología"


# ============================================================================
# PATRÓN DE COMPORTAMIENTO: STRATEGY
# ============================================================================
class ValidacionStrategy(ABC):
    """Estrategia abstracta para validar disponibilidad"""
    @abstractmethod
    def validar(self, hora_cita, doctor):
        pass


class ValidacionHorarioEstandar(ValidacionStrategy):
    """Validación estándar de horario"""
    def validar(self, hora_cita, doctor):
        formato = "%H:%M"
        try:
            cita = datetime.strptime(hora_cita, formato)
            inicio = datetime.strptime(doctor.horario_inicio, formato)
            fin = datetime.strptime(doctor.horario_fin, formato)
            return inicio <= cita <= fin
        except ValueError:
            return False


class ValidacionHorarioEstricto(ValidacionStrategy):
    """Validación estricta - solo horas en punto"""
    def validar(self, hora_cita, doctor):
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


class ValidacionHorarioFlexible(ValidacionStrategy):
    """Validación flexible - permite 30 min antes/después"""
    def validar(self, hora_cita, doctor):
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


class ValidadorCitas:
    """Contexto que usa la estrategia de validación"""
    def __init__(self, strategy: ValidacionStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: ValidacionStrategy):
        self._strategy = strategy
    
    def es_horario_valido(self, hora_cita, doctor):
        return self._strategy.validar(hora_cita, doctor)


# ============================================================================
# Clase Cita
# ============================================================================
class Cita:
    """Representa una cita médica"""
    def __init__(self, paciente, doctor, fecha, hora):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.hora = hora
    
    def mostrar_confirmacion(self):
        print("\n" + "="*50)
        print("       ✓ CITA RESERVADA EXITOSAMENTE")
        print("="*50)
        print(f"\n📋 DATOS DE LA CITA:")
        print("-" * 50)
        print(f"Paciente:       {self.paciente}")
        print(f"Doctor:         {self.doctor.nombre}")
        print(f"Especialidad:   {self.doctor.especialidad}")
        print(f"Fecha:          {self.fecha}")
        print(f"Hora:           {self.hora}")
        print("-" * 50)
        print("\n¡Recuerde llegar 15 minutos antes de su cita!")
        print("="*50 + "\n")


# ============================================================================
# PATRÓN ESTRUCTURAL: FACADE
# ============================================================================
class SistemaCitasFacade:
    """
    Facade que simplifica la interacción con el sistema de citas.
    Oculta la complejidad de los factories y validadores.
    """
    def __init__(self):
        # Registro de factories de especialidades
        self.factories = {
            "1": DermatologiaFactory(),
            "2": GinecologiaFactory(),
            "3": EmergenciaFactory(),
            "4": OdontologiaFactory(),
            "5": OftalmologiaFactory(),
            "6": OtorrinolaringologiaFactory(),
            "7": TraumatologiaFactory(),
            "8": UrologiaFactory()
        }
        
        # Validador con estrategia estándar por defecto
        self.validador = ValidadorCitas(ValidacionHorarioEstandar())
    
    def cambiar_estrategia_validacion(self, tipo):
        """Cambia la estrategia de validación"""
        estrategias = {
            "1": ValidacionHorarioEstandar(),
            "2": ValidacionHorarioEstricto(),
            "3": ValidacionHorarioFlexible()
        }
        if tipo in estrategias:
            self.validador.set_strategy(estrategias[tipo])
    
    def obtener_especialidades(self):
        """Retorna lista de especialidades disponibles"""
        return [(key, factory.get_especialidad()) 
                for key, factory in self.factories.items()]
    
    def obtener_doctores(self, especialidad_key):
        """Obtiene doctores de una especialidad usando el Factory"""
        if especialidad_key in self.factories:
            return self.factories[especialidad_key].crear_doctores()
        return None
    
    def validar_formato_hora(self, hora_str):
        """Valida el formato de hora"""
        try:
            datetime.strptime(hora_str, "%H:%M")
            return True
        except ValueError:
            return False
    
    def obtener_fecha_proxima(self):
        """Obtiene la fecha del día siguiente"""
        manana = datetime.now() + timedelta(days=1)
        return manana.strftime("%d/%m/%Y")
    
    def crear_cita(self, paciente, doctor, hora):
        """Crea y valida una cita"""
        # Validar formato de hora
        if not self.validar_formato_hora(hora):
            return None, "Formato de hora incorrecto. Use HH:MM"
        
        # Validar disponibilidad usando Strategy
        if not self.validador.es_horario_valido(hora, doctor):
            return None, "Horario no disponible o lleno"
        
        # Crear cita
        fecha = self.obtener_fecha_proxima()
        cita = Cita(paciente, doctor, fecha, hora)
        return cita, "Cita creada exitosamente"
    
    def mostrar_menu_especialidades(self):
        """Muestra el menú de especialidades"""
        print("\n" + "="*50)
        print("    SISTEMA DE RESERVA DE CITAS MÉDICAS")
        print("="*50)
        print("\nESPECIALIDADES DISPONIBLES:")
        print("-" * 50)
        for key, especialidad in self.obtener_especialidades():
            print(f"{key}. {especialidad}")
        print("-" * 50)
    
    def mostrar_doctores(self, doctores, especialidad):
        """Muestra los doctores disponibles"""
        print(f"\nDOCTORES DISPONIBLES EN {especialidad.upper()}:")
        print("-" * 50)
        for i, doctor in enumerate(doctores, 1):
            print(f"{i}. {doctor}")
        print("-" * 50)


# ============================================================================
# INTERFAZ DE USUARIO
# ============================================================================
def reservar_cita():
    """Función principal para reservar una cita usando el Facade"""
    # Crear el Facade
    sistema = SistemaCitasFacade()
    
    try:
        # Mostrar especialidades
        sistema.mostrar_menu_especialidades()
        
        # Seleccionar tipo de validación (opcional)
        print("\nTIPO DE VALIDACIÓN DE HORARIO:")
        print("1. Estándar (cualquier horario en el rango)")
        print("2. Estricto (solo horas en punto)")
        print("3. Flexible (30 min antes/después)")
        tipo_validacion = input("Seleccione tipo de validación (Enter para estándar): ").strip()
        
        if tipo_validacion in ["1", "2", "3"]:
            sistema.cambiar_estrategia_validacion(tipo_validacion)
        
        # Seleccionar especialidad
        especialidad_key = input("\nSeleccione el número de la especialidad: ").strip()
        
        doctores = sistema.obtener_doctores(especialidad_key)
        if doctores is None:
            print("\n❌ Especialidad no válida.")
            return
        
        especialidad = sistema.factories[especialidad_key].get_especialidad()
        
        # Mostrar doctores
        sistema.mostrar_doctores(doctores, especialidad)
        
        # Seleccionar doctor
        doctor_num = input("\nSeleccione el número del doctor: ").strip()
        
        try:
            doctor_index = int(doctor_num) - 1
            if doctor_index < 0 or doctor_index >= len(doctores):
                print("\n❌ Número de doctor no válido.")
                return
        except ValueError:
            print("\n❌ Debe ingresar un número válido.")
            return
        
        doctor_seleccionado = doctores[doctor_index]
        
        # Ingresar datos del paciente
        print("\n" + "-" * 50)
        nombre_paciente = input("Ingrese el nombre del paciente: ").strip()
        
        if not nombre_paciente:
            print("\n❌ El nombre del paciente no puede estar vacío.")
            return
        
        # Ingresar hora de la cita
        hora_cita = input("Ingrese la hora de la cita (formato HH:MM, ej: 10:30): ").strip()
        
        # Crear cita usando el Facade
        cita, mensaje = sistema.crear_cita(nombre_paciente, doctor_seleccionado, hora_cita)
        
        if cita:
            cita.mostrar_confirmacion()
        else:
            print(f"\n❌ {mensaje}")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Reserva cancelada por el usuario.")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")


def main():
    """Función principal del programa"""
    print("\n╔════════════════════════════════════════════════╗")
    print("║  SISTEMA CON PATRONES DE DISEÑO IMPLEMENTADOS ║")
    print("╠════════════════════════════════════════════════╣")
    print("║  • Factory Method (Creacional)                 ║")
    print("║  • Facade (Estructural)                        ║")
    print("║  • Strategy (Comportamiento)                   ║")
    print("╚════════════════════════════════════════════════╝")
    
    while True:
        reservar_cita()
        
        continuar = input("\n¿Desea reservar otra cita? (s/n): ").strip().lower()
        if continuar != 's':
            print("\n¡Gracias por usar nuestro sistema de citas médicas!")
            print("¡Que tenga un excelente día! 👋\n")
            break


if __name__ == "__main__":
    main()