# ArquitecturaDeSoftware
# ReservaDeCitasMedicas3Capas
Arquitectura de 3 capas



Resumen de caso de uso y funcionalidades.
1.1 Descripción General del Sistema
El Sistema de Reserva de Citas Médicas es una aplicación de consola desarrollada en Python que permite a los pacientes agendar citas médicas con especialistas de manera eficiente y organizada. El sistema implementa una arquitectura de software robusta basada en 3 capas, patrones de diseño clásicos y principios SOLID.
Actor: Paciente que desea reservar cita médica
Flujo:
Sistema muestra tipos de validación (Estándar, Estricto, Flexible)
Usuario selecciona tipo de validación
Sistema muestra 8 especialidades médicas
Usuario selecciona especialidad
Sistema muestra 3 doctores con sus horarios
Usuario selecciona doctor
Usuario ingresa nombre del paciente
Usuario ingresa hora deseada (formato HH:MM)
Sistema valida disponibilidad según estrategia elegida
Sistema confirma cita para mañana o muestra error
Resultado exitoso: Comprobante con datos de la cita (paciente, doctor, especialidad, fecha, hora)
Errores posibles:
Especialidad no válida
Doctor no válido
Nombre vacío
Formato de hora incorrecto
Horario no disponible o lleno

Ejemplo 1: Reserva Exitosa con Validación Estándar

Ejemplo 3: Validación Estricta Rechaza Minutos

Tecnologías usadas.

Sin dependencias externas - Solo bibliotecas estándar de Python

Captura de pantalla de la Arquitectura de 3 capas.

ReservaDeCitasMedicas/
│
├── main.py                                    [ENTRADA]
│
├── capa_presentacion/                         [CAPA 1]
│   ├── __init__.py
│   └── interfaz_consola.py
│
├── capa_negocio/                              [CAPA 2]
│   ├── facades/
│   │   └── sistema_citas_facade.py
│   ├── servicios/
│   │   ├── servicio_validacion.py
│   │   └── servicio_citas.py
│   └── strategies/
│       ├── validacion_strategy.py
│       └── implementaciones_strategy.py
│
└── capa_datos/                                [CAPA 3]
    ├── modelos/
    │   ├── doctor.py
    │   └── cita.py
    ├── factories/
    │   ├── doctor_factory.py
    │   └── implementaciones_factory.py
    └── repositorios/
        └── repositorio_doctores.py
4.2 Descripción de Capas
CAPA 1 - PRESENTACIÓN (Interfaz de Usuario)
Responsabilidad: Interacción con el usuario (I/O)
Clase: InterfazConsola
Función: Muestra menús, solicita datos, presenta resultados
NO contiene: Lógica de negocio ni acceso a datos
CAPA 2 - NEGOCIO (Lógica de Negocio)
Responsabilidad: Reglas de negocio, validaciones, coordinación
Clases: SistemaCitasFacade, ServicioValidacion, ServicioCitas, Strategies
Función: Valida datos, aplica reglas, coordina operaciones
Patrones: Facade (Estructural), Strategy (Comportamiento)
CAPA 3 - DATOS (Acceso a Datos)
Responsabilidad: Gestión de datos y creación de objetos
Clases: Doctor, Cita, Factories, RepositorioDoctores
Función: Crea y almacena datos
Patrón: Factory Method (Creacional)


Código fuente documentado por clases y rutas (path)
CAPA DE PRESENTACIÓN
Ruta: capa_presentacion/interfaz_consola.py
class InterfazConsola:
    """
    Interfaz de usuario por consola.
    Responsabilidad: Interacción con el usuario (I/O únicamente)
    """
    
    def __init__(self, facade):
        self._facade = facade
    
    def ejecutar(self):
        """Método principal que ejecuta el sistema"""
        self.mostrar_banner_bienvenida()
        while True:
            self.reservar_cita()
            if not self.solicitar_continuar():
                break
    
    def reservar_cita(self):
        """Flujo completo de reserva delegando al Facade"""
        # Seleccionar tipo de validación
        tipo_validacion = self.solicitar_tipo_validacion()
        self._facade.cambiar_estrategia_validacion(tipo_validacion)
        
        # Seleccionar especialidad
        especialidad_key = self.solicitar_especialidad()
        
        # Mostrar doctores
        doctores = self._facade.obtener_doctores(especialidad_key)
        self.mostrar_doctores(doctores, especialidad)
        
        # Seleccionar doctor y crear cita
        doctor = self._validar_y_obtener_doctor(doctor_num, doctores)
        nombre_paciente = self.solicitar_nombre_paciente()
        hora_cita = self.solicitar_hora_cita()
        
        # Crear cita usando Facade
        cita, mensaje = self._facade.crear_cita(nombre_paciente, doctor, hora_cita)
        
        if cita:
            cita.mostrar_confirmacion()
        else:
            self.mostrar_error(mensaje)
7.2 CAPA DE NEGOCIO
Ruta: capa_negocio/facades/sistema_citas_facade.py
class SistemaCitasFacade:
    """
    Facade que simplifica interacción con subsistemas.
    Patrón: Facade (Estructural)
    """
    
    def __init__(self):
        self._repositorio_doctores = RepositorioDoctores()
        self._servicio_validacion = ServicioValidacion()
        self._servicio_citas = ServicioCitas(self._servicio_validacion)
    
    def obtener_especialidades(self):
        return self._repositorio_doctores.obtener_todas_especialidades()
    
    def obtener_doctores(self, especialidad_key):
        return self._repositorio_doctores.obtener_doctores_por_especialidad(especialidad_key)
    
    def crear_cita(self, paciente, doctor, hora):
        return self._servicio_citas.crear_cita(paciente, doctor, hora)
    
    def cambiar_estrategia_validacion(self, tipo):
        return self._servicio_validacion.cambiar_estrategia(tipo)
Ruta: capa_negocio/servicios/servicio_validacion.py
class ServicioValidacion:
    """
    Servicio de validación de horarios.
    Responsabilidad: Validar formatos y disponibilidad
    """
    
    def __init__(self):
        self._validador = ValidadorCitas(ValidacionHorarioEstandar())
        self._estrategias_disponibles = {
            "1": ValidacionHorarioEstandar(),
            "2": ValidacionHorarioEstricto(),
            "3": ValidacionHorarioFlexible()
        }
    
    def validar_formato_hora(self, hora_str):
        try:
            datetime.strptime(hora_str, "%H:%M")
            return True
        except ValueError:
            return False
    
    def validar_horario_disponible(self, hora_cita, doctor):
        return self._validador.es_horario_valido(hora_cita, doctor)
    
    def cambiar_estrategia(self, tipo):
        if tipo in self._estrategias_disponibles:
            self._validador.set_strategy(self._estrategias_disponibles[tipo])
            return True
        return False
Ruta: capa_negocio/servicios/servicio_citas.py
class ServicioCitas:
    """
    Servicio de gestión de citas.
    Responsabilidad: Crear y validar citas
    """
    
    def __init__(self, servicio_validacion):
        self._servicio_validacion = servicio_validacion
    
    def crear_cita(self, paciente, doctor, hora):
        # Validar nombre
        if not paciente or not paciente.strip():
            return None, "El nombre del paciente no puede estar vacío"
        
        # Validar formato
        if not self._servicio_validacion.validar_formato_hora(hora):
            return None, "Formato de hora incorrecto. Use HH:MM"
        
        # Validar disponibilidad
        if not self._servicio_validacion.validar_horario_disponible(hora, doctor):
            return None, "Horario no disponible o lleno"
        
        # Crear cita
        fecha = self._calcular_fecha_proxima()
        cita = Cita(paciente, doctor, fecha, hora)
        return cita, "Cita creada exitosamente"
    
    def _calcular_fecha_proxima(self):
        manana = datetime.now() + timedelta(days=1)
        return manana.strftime("%d/%m/%Y")
Ruta: capa_negocio/strategies/validacion_strategy.py
class ValidacionStrategy(ABC):
    """
    Estrategia abstracta de validación.
    Patrón: Strategy (Comportamiento)
    """
    
    @abstractmethod
    def validar(self, hora_cita, doctor):
        pass
    
    @abstractmethod
    def get_descripcion(self):
        pass

class ValidadorCitas:
    """Contexto que usa la estrategia"""
    
    def __init__(self, strategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy):
        self._strategy = strategy
    
    def es_horario_valido(self, hora_cita, doctor):
        return self._strategy.validar(hora_cita, doctor)
Ruta: capa_negocio/strategies/implementaciones_strategy.py
class ValidacionHorarioEstandar(ValidacionStrategy):
    """Acepta cualquier hora en el rango"""
    def validar(self, hora_cita, doctor):
        cita = datetime.strptime(hora_cita, "%H:%M")
        inicio = datetime.strptime(doctor.horario_inicio, "%H:%M")
        fin = datetime.strptime(doctor.horario_fin, "%H:%M")
        return inicio <= cita <= fin

class ValidacionHorarioEstricto(ValidacionStrategy):
    """Solo acepta horas en punto"""
    def validar(self, hora_cita, doctor):
        cita = datetime.strptime(hora_cita, "%H:%M")
        if cita.minute != 0:
            return False
        inicio = datetime.strptime(doctor.horario_inicio, "%H:%M")
        fin = datetime.strptime(doctor.horario_fin, "%H:%M")
        return inicio <= cita <= fin

class ValidacionHorarioFlexible(ValidacionStrategy):
    """Permite ±30 minutos"""
    def validar(self, hora_cita, doctor):
        cita = datetime.strptime(hora_cita, "%H:%M")
        inicio = datetime.strptime(doctor.horario_inicio, "%H:%M")
        fin = datetime.strptime(doctor.horario_fin, "%H:%M")
        inicio_flex = inicio - timedelta(minutes=30)
        fin_flex = fin + timedelta(minutes=30)
        return inicio_flex <= cita <= fin_flex
7.3 CAPA DE DATOS
Ruta: capa_datos/modelos/doctor.py
class Doctor:
    """
    Entidad de dominio Doctor.
    Responsabilidad: Representar datos de un doctor
    """
    
    def __init__(self, nombre, horario_inicio, horario_fin, especialidad):
        self._nombre = nombre
        self._horario_inicio = horario_inicio
        self._horario_fin = horario_fin
        self._especialidad = especialidad
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def horario_inicio(self):
        return self._horario_inicio
    
    @property
    def horario_fin(self):
        return self._horario_fin
    
    @property
    def especialidad(self):
        return self._especialidad
    
    def __str__(self):
        return f"{self._nombre} - {self._especialidad} ({self._horario_inicio} - {self._horario_fin})"

Ruta: capa_datos/modelos/cita.py
class Cita:
    """
    Entidad de dominio Cita.
    Responsabilidad: Representar datos de una cita
    """
    
    def __init__(self, paciente, doctor, fecha, hora):
        self._paciente = paciente
        self._doctor = doctor
        self._fecha = fecha
        self._hora = hora
    
    def mostrar_confirmacion(self):
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
Ruta: capa_datos/factories/doctor_factory.py
class DoctorFactory(ABC):
    """
    Factory abstracto para crear doctores.
    Patrón: Factory Method (Creacional)
    """
    
    @abstractmethod
    def crear_doctores(self):
        pass
    
    @abstractmethod
    def get_especialidad(self):
        pass
Ruta: capa_datos/factories/implementaciones_factory.py
class DermatologiaFactory(DoctorFactory):
    def crear_doctores(self):
        return [
            Doctor("Dr. Carlos Mendoza", "08:00", "14:00", "Dermatología"),
            Doctor("Dra. Ana López", "14:00", "20:00", "Dermatología"),
            Doctor("Dr. Roberto Vargas", "09:00", "15:00", "Dermatología")
        ]
    def get_especialidad(self):
        return "Dermatología"

# Similar para: GinecologiaFactory, EmergenciaFactory, OdontologiaFactory,
# OftalmologiaFactory, OtorrinolaringologiaFactory, TraumatologiaFactory, UrologiaFactory
Ruta: capa_datos/repositorios/repositorio_doctores.py
class RepositorioDoctores:
    """
    Repositorio de doctores.
    Responsabilidad: Gestionar acceso a doctores mediante factories
    """
    
    def __init__(self):
        self._factories = {
            "1": DermatologiaFactory(),
            "2": GinecologiaFactory(),
            "3": EmergenciaFactory(),
            "4": OdontologiaFactory(),
            "5": OftalmologiaFactory(),
            "6": OtorrinolaringologiaFactory(),
            "7": TraumatologiaFactory(),
            "8": UrologiaFactory()
        }
    
    def obtener_todas_especialidades(self):
        return [(key, factory.get_especialidad()) 
                for key, factory in self._factories.items()]
    
    def obtener_doctores_por_especialidad(self, especialidad_key):
        factory = self._factories.get(especialidad_key)
        if factory:
            return factory.crear_doctores()
        return None
    
    def especialidad_existe(self, especialidad_key):
        return especialidad_key in self._factories
7.4 ARCHIVO PRINCIPAL
Ruta: main.py
from capa_negocio.facades.sistema_citas_facade import SistemaCitasFacade
from capa_presentacion.interfaz_consola import InterfazConsola

def main():
    """Función principal del sistema"""
    # Crear Facade (coordina todo el sistema)
    facade = SistemaCitasFacade()
    
    # Crear Interfaz (recibe Facade por inyección)
    interfaz = InterfazConsola(facade)
    
    # Ejecutar sistema
    interfaz.ejecutar()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido por el usuario.")
        print("¡Hasta luego! 👋\n")
    except Exception as e:
        print(f"\n❌ Error crítico: {e}\n")


Resumen de cumplimiento de SOLID, Patrones y Arquitectura.
S - Single Responsibility Principle 
Cada clase tiene una única responsabilidad
InterfazConsola: Solo I/O
ServicioValidacion: Solo validaciones
ServicioCitas: Solo gestión de citas
Doctor: Solo datos de doctor
O - Open/Closed Principle 
Abierto a extensión, cerrado a modificación
Agregar especialidad: Crear nuevo Factory (sin modificar existentes)
Agregar validación: Crear nueva Strategy (sin modificar existentes)
L - Liskov Substitution Principle 
Las subclases pueden sustituir a la clase base
Todos los Factories son intercambiables
Todas las Strategies son intercambiables
I - Interface Segregation Principle 
Interfaces específicas y mínimas
DoctorFactory: Solo 2 métodos necesarios
ValidacionStrategy: Solo 2 métodos necesarios
D - Dependency Inversion Principle 
Depender de abstracciones, no de implementaciones
InterfazConsola depende de SistemaCitasFacade (abstracción)
ServicioCitas depende de ServicioValidacion (abstracción)
ValidadorCitas depende de ValidacionStrategy (abstracción)
PATRONES DE DISEÑO IMPLEMENTADOS
5.1 Factory Method (Creacional)
Ubicación: capa_datos/factories/
Propósito: Delegar la creación de doctores a clases especializadas
Implementación:
1 clase abstracta: DoctorFactory
8 clases concretas: DermatologiaFactory, GinecologiaFactory, etc.
Cada factory crea 3 doctores de su especialidad
Beneficio: Agregar nuevas especialidades sin modificar código existente
Ejemplo:
python
class DermatologiaFactory(DoctorFactory):
    def crear_doctores(self):
        return [
            Doctor("Dr. Carlos Mendoza", "08:00", "14:00", "Dermatología"),
            Doctor("Dra. Ana López", "14:00", "20:00", "Dermatología"),
            Doctor("Dr. Roberto Vargas", "09:00", "15:00", "Dermatología")
        ]
5.2 Facade (Estructural)
Ubicación: capa_negocio/facades/sistema_citas_facade.py
Propósito: Simplificar la interacción con subsistemas complejos
Implementación:
Coordina 3 subsistemas: RepositorioDoctores, ServicioValidacion, ServicioCitas
Proporciona interfaz unificada y simple
Beneficio: La capa de presentación solo conoce el Facade, no los subsistemas internos
Ejemplo:
python
class SistemaCitasFacade:
    def __init__(self):
        self._repositorio_doctores = RepositorioDoctores()
        self._servicio_validacion = ServicioValidacion()
        self._servicio_citas = ServicioCitas(self._servicio_validacion)
    
    def crear_cita(self, paciente, doctor, hora):
        return self._servicio_citas.crear_cita(paciente, doctor, hora)
5.3 Strategy (Comportamiento)
Ubicación: capa_negocio/strategies/
Propósito: Cambiar el algoritmo de validación dinámicamente
Implementación:
1 clase abstracta: ValidacionStrategy
3 estrategias concretas:
Estándar: Acepta cualquier hora en el rango
Estricto: Solo acepta horas en punto (08:00, 14:00)
Flexible: Permite ±30 minutos del rango
1 contexto: ValidadorCitas
Beneficio: Cambiar comportamiento sin modificar código
Ejemplo:
python
# Estrategia Estándar
class ValidacionHorarioEstandar(ValidacionStrategy):
    def validar(self, hora_cita, doctor):
        return inicio <= hora_cita <= fin

# Cambio dinámico
validador.set_strategy(ValidacionHorarioEstricto())



