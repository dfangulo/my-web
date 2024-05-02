import os
from .menu import mostrar_menu
from .controller import ManagementParticipants
from .tombola import Tombola


class RifaCC:
    managment = ManagementParticipants()
    tombola = Tombola()

    def main(self):
        os.system('cls')
        while True:
            mostrar_menu()
            opcion = input("Ingrese el número de la opción que desea realizar: ")

            if opcion == "1":
                self.managment.show_participants()
            elif opcion == "2":
                while True:
                    nombre = input("Ingrese el nombre: ")
                    if not nombre:
                        break

                    celular = input("Ingrese el número de celular: ")
                    referencia = input("Ingrese la referencia: ")
                    tickets = input("Cuantos boletos (deje en blanco para un boleto): ")

                    # Si el usuario deja en blanco la cantidad de boletos, se asume que solo compra uno
                    if not tickets:
                        tickets = 1
                    else:
                        # Validar que la cantidad de boletos sea un número entero positivo
                        try:
                            tickets = int(tickets)
                            if tickets <= 0:
                                raise ValueError
                        except ValueError:
                            print(
                                "La cantidad de boletos debe ser un número entero positivo."
                            )
                            continue

                    # Agregar el participante con la cantidad de boletos ingresada
                    for _ in range(tickets):
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
            elif opcion.lower() == "l":
                self.managment.list_participants()
            elif opcion == "w":
                self.tombola.load_participants()
                self.tombola.select_winner()
                self.tombola.reveal_winner()
                break
            else:
                print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
