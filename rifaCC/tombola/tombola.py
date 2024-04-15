import random
import json
import time
import sys
import os
from collections import Counter


class Tombola:
    participants: list = []
    winner: str = None

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
        # print(f"¡El ganador es: {winner}!")

        # Escribir el nombre del ganador en un archivo JSON
        winner_data = {"winner": winner}
        with open("js/json/winner.json", "w") as file:
            json.dump(winner_data, file)
            print("Nombre del ganador escrito en js/json/winner.json.")

    def reveal_winner(self) -> None:
        os.system('cls')
        with open("js/json/winner.json") as file:
            winner_data = json.load(file)
            self.winner = winner_data.get("winner")
            self.animate_winner_reveal(self.participants, self.winner)

    def animate_winner_reveal(self, participants, winner):
        # Tiempo de espera entre cada nombre (en segundos)
        wait_time = 0.5
        self.type_text_slowly("Agradecimiento especial a todos los que nos apayoran: ")
        print()
        participants_names = [participant['name'] for  participant in participants]
        count_data_participants = Counter(participants_names)
        line: int = 0
        pages = round(len(count_data_participants)/4)
        header: str = f"[{"Participantes".center(30)}]" + " [Boletos]\n"
        print(header)
        for participant, tickets  in count_data_participants.items():
            if line > pages:
                os.system('cls')
                print(header)
                line = 0
            str_names = f"[\033[92m{participant.center(30, " ")}\033[0m]" + f" [{tickets:>2} \033[91m\u2764\033[0m ]"
            self.type_text_slowly(str_names, 0.01)
            line += 1
            print()
        
        print('\n' * 2)
        text = "¡Y el ganador es..."
        self.type_text_slowly(text)
        print()
        time.sleep(
            wait_time * 3
        )  # Tiempo de espera adicional antes de revelar al ganador

        self.type_text_slowly(("¡" + winner["name"]+ "!"))
        time.sleep(
            wait_time * 5
        )  # Tiempo de espera adicional después de revelar al ganador

    def type_text_slowly(self, text, delay=0.1):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)


if __name__ == "__main__":
    # Ejemplo de uso
    tombola = Tombola()
    tombola.load_participants()
    tombola.select_winner()
    tombola.reveal_winner()
