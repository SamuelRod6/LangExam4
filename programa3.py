# Programa de la pregunta 3


class ManejadorClases:
    def __init__(self):
        self.clases = {}

    def agregar_clase(self, definicion_clase):
        partes = definicion_clase.split()
        if len(partes) < 2:
            print("Error: Definición de clase inválida.")
            return

        clase = partes[1]
        if clase in self.clases:
            print("Error: La clase ya existe.")
            return

        if ':' in definicion_clase:
            clase, super_clase = partes[1], partes[3]
            if super_clase not in self.clases:
                print("Error: La super clase no existe.")
                return
            metodos = partes[4:]
        else:
            metodos = partes[2:]

        if len(set(metodos)) != len(metodos):
            print("Error: Métodos repetidos en la definición.")
            return

        self.clases[clase] = {
            'super': super_clase if ':' in definicion_clase else None,
            'metodos': {metodo: clase for metodo in metodos}
        }

    def describir_clase(self, clase):
        if clase not in self.clases:
            print("Error: La clase no existe.")
            return

        vtable = self.construir_vtable(clase)
        for metodo, propietario in vtable.items():
            print(f"{metodo} -> {propietario} :: {metodo}")

    def construir_vtable(self, clase):
        vtable = {}
        clase_actual = clase
        while clase_actual:
            for metodo, propietario in self.clases[clase_actual]['metodos'].items():
                if metodo not in vtable:
                    vtable[metodo] = propietario
            clase_actual = self.clases[clase_actual]['super']
        return vtable

                
# MAIN
def main():
    manejador = ManejadorClases()
    while True:
        accion = input("Ingrese una acción: ")
        if accion.startswith("CLASS"):
            manejador.agregar_clase(accion)
        elif accion.startswith("DESCRIBIR"):
            _, clase = accion.split()
            manejador.describir_clase(clase)
        elif accion == "AYUDA":
            print("Comandos disponibles:")
            print("  - CLASS <tipo> [<nombre>]: Crea un nuevo tipo con métodos establecidos dentro de la lista.")
            print("  - DESCRIBIR <nombre>: Muestra la tabla de métodos virtuales del tipo.")
            print("  - SALIR: Termina el programa.")
        elif accion == "SALIR":
            break
        else:
            print("Acción no reconocida. (Escriba AYUDA para ver los comandos disponibles)")

if __name__ == "__main__":
    main()
    
# Las pruebas se encuentran en el archivo test_programa3.py