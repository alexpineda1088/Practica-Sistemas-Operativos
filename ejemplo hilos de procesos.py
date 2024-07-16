import threading
import time

# Definición de la clase MiHilo que hereda de threading.Thread
class MiHilo(threading.Thread):
    def __init__(self, nombre, tarea):
        # Llamada al constructor de la clase base threading.Thread
        threading.Thread.__init__(self)
        self.nombre = nombre  # Nombre del hilo
        self.tarea = tarea    # Tarea que realizará el hilo
        print(f"Hilo {self.nombre} creado")

    # Método que se ejecuta cuando se llama a start()
    def run(self):
        print(f"Hilo {self.nombre} en ejecución, realizando: {self.tarea}")
        time.sleep(2)  # Simulando una tarea que toma tiempo con una pausa de 2 segundos
        print(f"Hilo {self.nombre} ha terminado de realizar: {self.tarea}")

    # Destructor que se llama cuando el objeto es destruido
    def __del__(self):
        print(f"Hilo {self.nombre} destruido")

# Crear instancias de MiHilo con nombres y tareas diferentes
hilo1 = MiHilo("Hilo-1", "Tarea-1")
hilo2 = MiHilo("Hilo-2", "Tarea-2")
hilo3 = MiHilo("Hilo-3", "Tarea-3")

# Iniciar los hilos para que comiencen su ejecución
hilo1.start()
hilo2.start()
hilo3.start()

# Esperar a que todos los hilos terminen antes de continuar
hilo1.join()
hilo2.join()
hilo3.join()
