import random
import json

class Tombola:
    participants = []

    def load_participants(self):
        try:
            with open("js/json/data.json", "r") as file:
                data = json.load(file)
            self.participants = data.get("data")
        except FileNotFoundError:
            print("El archivo data.json no existe.")
            return None
        except json.JSONDecodeError:
            print("El archivo data.json está mal formateado.")
            return None

    def select_winner(self):
        if not self.participants:
            print("No hay participantes cargados.")
            return

        winner = random.choice(self.participants)
        print(f"¡El ganador es: {winner}!")

        # Escribir el nombre del ganador en un archivo JSON
        winner_data = {"winner": winner}
        with open("js/json/winner.json", "w") as file:
            json.dump(winner_data, file)
            print("Nombre del ganador escrito en js/json/winner.json.")

if __name__== "__main__":
    # Ejemplo de uso
    tombola = Tombola()
    tombola.load_participants()
    tombola.select_winner()
