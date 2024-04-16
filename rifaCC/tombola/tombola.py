import random
import json
import time
import sys
import os
from collections import Counter


class Tombola:
    participants: list = []
    winner: str = None
    header: str = f"[{"Participantes".center(30)}]" + " [Boletos]\n"
    messaje = "\033[92mAgradecimiento especial a todos los que nos apoyan: \033[0m"

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
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
        self.clear_screen()
        with open("js/json/winner.json") as file:
            winner_data = json.load(file)
            self.winner = winner_data.get("winner")
            self.thanks_to_support_us()

    def thanks_to_support_us(self) -> None:
        wait_time = 0.5
        self.smooth_print(self.messaje + '\n')
        self.smooth_print(self.header+ '\n')
        participants_names = [participant['name'] for  participant in self.participants]
        count_data_participants = Counter(participants_names)
        text = [ f"[\033[92m{participant.center(30, " ")}\033[0m]" + f" [{tickets:>2} \033[91m\u2764\033[0m ]" for participant, tickets in  count_data_participants.items()]
        self.smooth_fade_out(text="\n".join(text))
        print('\n' * 2)
        text = "¡Y el ganador es...: "
        self.smooth_print(text, delay=0.1)
        print()
        time.sleep(
            wait_time * 3
        )
        self.smooth_fade_out((self.winner['name'].center(35)))

    def smooth_print(self,text, delay=0.02):
        for char in text:
            if char:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)

    def smooth_fade_out(self,text, delay=0.05):
        self.clear_screen()
        lines_text: list[str] = text.split("\n")
        size_page: int = 20
        page = ["" for _ in range(size_page)]
        lines_text += page + [""]
        for  line in lines_text:
            self.clear_screen()
            print(self.messaje)
            print(self.header,'\n')
            print(f"\n".join(page))
            self.smooth_print(line.center(30), delay=0.01)
            page.append(line.center(30))
            del page[0] 
            time.sleep(delay)


if __name__ == "__main__":
    # Ejemplo de uso
    tombola = Tombola()
    tombola.load_participants()
    tombola.select_winner()
    tombola.reveal_winner()
