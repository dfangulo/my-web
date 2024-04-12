from .menu import mostrar_menu
from .controller import ManagementParticipants
from .tombola import Tombola


class RifaCC:
    managment = ManagementParticipants()
    tombola = Tombola()

    def main(self):
        while True:
            mostrar_menu()
            opcion = input("Ingrese el número de la opción que desea realizar: ")

            if opcion == "1":
                self.managment.show_participants()
            elif opcion == "2":
                nombre = input("Ingrese el nombre: ")
                celular = input("Ingrese el número de celular: ")
                referencia = input("Ingrese la referencia: ")
                self.managment.add_participant(nombre, celular, referencia)
            elif opcion == "3":
                index = int(
                    input("Ingrese el índice del participante que desea editar: ")
                )
                if index != 0:  # Verificar que el índice no sea cero
                    try:
                        self.managment.show_participant_by_index(index=index - 1)
                        confirmacion = input("¿Desea editar este participante? (s/n): ")
                        if confirmacion.lower() == "s":
                            nombre = input("Ingrese el nuevo nombre del participante: ")
                            celular = input(
                                "Ingrese el nuevo número de celular del participante: "
                            )
                            referencia = input(
                                "Ingrese la nueva referencia del participante: "
                            )
                            self.managment.edit_participant(
                                index - 1, nombre, celular, referencia
                            )
                            print("Participante editado correctamente.")
                        else:
                            print("Edición cancelada.")
                    except IndexError:
                        print("No existe el participante con ese índice.")
                else:
                    print("El índice del participante no puede ser cero.")
            elif opcion == "4":
                print("¡Hasta luego!")
                break
            elif opcion == "w":
                self.tombola.load_participants()
                self.tombola.select_winner()
            else:
                print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
