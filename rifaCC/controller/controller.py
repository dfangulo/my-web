import os
import json
from ..model import Participant


class ManagementParticipants:
    # Función para cargar los datos del archivo JSON
    def load_data(self):
        try:
            with open("js/json/data.json", "r") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print("El archivo data.json no existe.")
            return None
        except json.JSONDecodeError:
            print("El archivo data.json está mal formateado.")
            return None

    # Función para agregar un nuevo participante
    def add_participant(self, name, celular, reference):
        data = self.load_data()
        if data is not None:
            new_participant = {"name": name, "celular": celular, "reference": reference}
            data["data"].append(new_participant)
            with open("js/json/data.json", "w") as file:
                json.dump(data, file, indent=4)
            print("Participante agregado correctamente.")
        else:
            print("No se pudo agregar el participante.")

    # Función para editar un participante existente
    def edit_participant(self, index, name, celular, reference):
        data = self.load_data()
        if data is not None:
            if 0 <= index < len(data["data"]):
                # Obtener los datos del participante actual
                participant_data = data["data"][index]

                # Verificar si los campos están en blanco y mantener los valores actuales si es necesario
                if not name:
                    name = participant_data.get("name", "")
                if not celular:
                    celular = participant_data.get("celular", "")
                if not reference:
                    reference = participant_data.get("reference", "")

                # Actualizar los datos del participante con los nuevos valores
                data["data"][index] = {
                    "name": name,
                    "celular": celular,
                    "reference": reference,
                }

                # Escribir los datos actualizados de vuelta al archivo JSON
                with open("js/json/data.json", "w") as file:
                    json.dump(data, file, indent=4)
                print("Participante editado correctamente.")
            else:
                print("Índice de participante fuera de rango.")
        else:
            print("No se pudo editar el participante.")

    # Función para mostrar todos los participantes
    def show_participants(self):
        os.system("cls")
        data = self.load_data()
        if data is not None:
            for i, participant_data in enumerate(data["data"]):
                if all(
                    field in participant_data
                    for field in ["name", "celular", "reference"]
                ):
                    participant = Participant(**participant_data)
                    print(f"Índice: {i + 1}")
                    print(f"Nombre: {participant.name}")
                    print(f"Celular: {participant.celular}")
                    print(f"Referencia: {participant.reference}")
                    print("-------------------------")
                else:
                    print(f"Los datos del participante en el índice {i} son inválidos.")
        else:
            print("No se pudieron cargar los datos.")

    # Función para mostrar los detalles de un participante por su índice
    def show_participant_by_index(self, index):
        data = self.load_data()
        if data is not None:
            if 0 <= index < len(data["data"]):
                participant_data = data["data"][index]
                if all(
                    field in participant_data
                    for field in ["name", "celular", "reference"]
                ):
                    participant = Participant(**participant_data)
                    print(f"Nombre: {participant.name}")
                    print(f"Celular: {participant.celular}")
                    print(f"Referencia: {participant.reference}")
                else:
                    print("Los datos del participante son inválidos.")
            else:
                print("El índice de participante está fuera de rango.")
        else:
            print("No se pudieron cargar los datos.")

    def list_participants(self, file_path: str = 'list.txt') -> None:
        os.system("cls")
        data = self.load_data()
        if data is not None:
            with open(file_path, "w", encoding="utf-8") as file:
                for i, participant_data in enumerate(data["data"]):
                    if all(
                        field in participant_data
                        for field in ["name", "celular", "reference"]
                    ):
                        participant = Participant(**participant_data)
                        file.write(f"{participant.name}\n")
                    else:
                        print(f"Los datos del participante en el índice {i} son inválidos.")
            print(f"Los nombres de los participantes se han guardado en el archivo: {file_path}")
        else:
            print("No se pudieron cargar los datos.")