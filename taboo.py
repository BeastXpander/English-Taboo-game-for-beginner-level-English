import tkinter as tk
import random
from tkinter import messagebox

# ----------- GAME DATA -----------
cards = {
    "CHARITY": ["Money", "Help", "Free", "Poor", "Save"],
    "APPEAR": ["Notice", "See", "Suddenly"],
    "MEMBER": ["Team", "Person", "People", "Together"],
    "PROMISE": ["Tell", "Say", "True", "Keep"],
    "SHARE": ["Give", "People", "Nice", "Help"],
    "COMEDY": ["Laugh", "Joke", "Film", "Television"],
    "POVERTY": ["Poor", "Hungry", "Homeless", "Help"],
    "TALENTED": ["Special", "Popular", "Famous", "Sing", "Good"],
    "INTELLIGENT": ["Clever", "IQ", "Study", "Easy"],
    "HUMOUR": ["Funny", "Joke", "Laugh"],
    "CONFIDENT": ["Brave", "Courageous", "Proud"],
    "RUDE": ["Impolite", "Bad", "Respect"],
    "SHY": ["Talk", "Quiet", "Afraid"],
    "EXPERIENCE": ["Adventure", "See", "Knowledge"],
    "INTERESTING": ["Exciting", "Hobby", "Attention", "Unusual"],
    "BLOOD": ["Red", "Die", "Knife", "Body"],
    "SHOUT": ["Talk", "Loud", "Noise"],
    "SQUEEZE": ["Grip", "Fruit", "Pack"],
    "SOUR": ["Taste", "Cherry", "Lemon"],
    "SPICY": ["Hot", "Pepper", "Taste", "Food"],
    "BURGLAR": ["House", "Crime", "Money", "Steal"],
    "FOLLOW": ["Go", "Come", "Behind"],
    "HIDE": ["Cover", "Invisible", "Safe"],
    "HONEY": ["Bee", "Sweet", "Yellow", "Flower"],
    "UPSET": ["Angry", "Nervous", "Aggressive"],
    "DANGER": ["Safe", "Accident", "Fire"],
    "MYSTERIOUS": ["Secret", "Exciting", "Hidden", "Interesting"],
    "SEVERE": ["Serious", "Important", "Problem"],
    "CAMEL": ["Desert", "Water", "Cigarette"],
    "FOREIGN": ["Stranger", "Country", "People"],
    "DELAY": ["Late", "Time", "Schedule"],
    "DESTINATION": ["Location", "Country", "Abroad", "Holiday"],
    "BATTERY": ["Charge", "Camera", "Radio", "Work"],
    "DISCOVER": ["Save", "Find", "Travel", "Expedition"],
    "RESCUE": ["Safe", "Danger", "Life", "Help"],
    "SMOKE": ["Sky", "Fire", "Forest", "Cigarette"],
    "RENT": ["Lend", "Borrow", "Car", "Money"],
    "CAPITAL": ["Country", "City", "People"],
    "DEVELOP": ["Maintain", "Grow", "Strong"],
    "VOLCANO": ["Italy", "Fire", "Explosion", "Erupt"],
    "TOURIST": ["Map", "Foreigner", "Visit", "Museum", "Travel"],
    "ANCIENT": ["Old", "Building", "Museum", "Historical"],


}




# ----------- GAME CLASS -----------
class TabooGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Taboo Game")
        self.root.geometry("600x600")
        self.root.config(bg="#f2f2f2")

        self.team_scores = [0, 0]
        self.current_team = 0
        self.time_left = 90
        self.timer_running = False

        self.used_words = set()
        self.current_word = ""
        self.current_taboos = []

        self.create_start_ui()

    # ---------- Start Screen ----------
    def create_start_ui(self):
        self.start_frame = tk.Frame(self.root, bg="#f2f2f2")
        self.start_frame.pack(expand=True)

        title = tk.Label(
            self.start_frame,
            text="TABOO",
            font=("Arial", 40, "bold"),
            fg="#222",
            bg="#f2f2f2",
        )
        title.pack(pady=30)

        start_button = tk.Button(
            self.start_frame,
            text="▶ START GAME",
            font=("Arial", 20, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=40,
            pady=15,
            relief="raised",
            command=self.start_game,
        )
        start_button.pack(pady=40)

    def start_game(self):
        self.start_frame.destroy()
        self.setup_ui()
        self.next_card()
        self.start_timer()

    # ---------- Main Game UI ----------
    def setup_ui(self):
        self.team_label = tk.Label(
            self.root, text="Team 1's Turn", font=("Arial", 18, "bold"), bg="#f2f2f2"
        )
        self.team_label.pack(pady=10)

        self.timer_label = tk.Label(
            self.root, text="Time: 90", font=("Arial", 16), bg="#f2f2f2"
        )
        self.timer_label.pack()

        # Card Frame (White Rounded Style)
        self.card_frame = tk.Frame(
            self.root,
            bg="white",
            bd=5,
            relief="raised",
            padx=20,
            pady=20,
            highlightbackground="#333",
            highlightthickness=1,
        )
        self.card_frame.pack(pady=25, ipadx=10, ipady=10)

        self.word_label = tk.Label(
            self.card_frame, text="", font=("Arial", 30, "bold"), fg="#007BFF", bg="white"
        )
        self.word_label.pack(pady=10)

        tk.Label(
            self.card_frame,
            text="❌ Taboo Words ❌",
            font=("Arial", 16, "bold"),
            fg="red",
            bg="white",
        ).pack(pady=5)

        self.taboo_text = tk.Label(
            self.card_frame, text="", font=("Arial", 14), bg="white", fg="#555"
        )
        self.taboo_text.pack()

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#f2f2f2")
        btn_frame.pack(pady=20)

        self.next_button = tk.Button(
            btn_frame, text="Next ✅", font=("Arial", 14), width=10, bg="#C8E6C9", command=self.next_word
        )
        self.next_button.grid(row=0, column=0, padx=10)

        self.pass_button = tk.Button(
            btn_frame, text="Pass ⏩", font=("Arial", 14), width=10, bg="#E0E0E0", command=self.pass_word
        )
        self.pass_button.grid(row=0, column=1, padx=10)

        self.taboo_button = tk.Button(
            btn_frame,
            text="TABU! ❌",
            font=("Arial", 14),
            width=10,
            bg="#FFCDD2",
            fg="red",
            command=self.taboo_pressed,
        )
        self.taboo_button.grid(row=0, column=2, padx=10)

        # Scoreboard
        self.score_label = tk.Label(
            self.root,
            text="Team 1: 0  |  Team 2: 0",
            font=("Arial", 16, "bold"),
            bg="#f2f2f2",
        )
        self.score_label.pack(pady=10)

    # ---------- Timer ----------
    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time: {self.time_left}")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.timer_running = False
            self.switch_team()

    # ---------- Game Logic ----------
    def next_card(self):
        available_cards = [word for word in cards.keys() if word not in self.used_words]
        if not available_cards:
            messagebox.showinfo("Game Over", "No more words left!")
            self.root.quit()
            return

        self.current_word = random.choice(available_cards)
        self.current_taboos = cards[self.current_word]
        self.used_words.add(self.current_word)

        self.word_label.config(text=self.current_word.upper())
        self.taboo_text.config(text="\n".join(self.current_taboos))

    def next_word(self):
        self.team_scores[self.current_team] += 1
        self.update_scoreboard()
        self.next_card()

    def pass_word(self):
        self.next_card()

    def taboo_pressed(self):
        self.team_scores[self.current_team] -= 1
        self.update_scoreboard()
        self.next_card()

    def switch_team(self):
        self.time_left = 90
        self.current_team = 1 - self.current_team
        self.team_label.config(text=f"Team {self.current_team + 1}'s Turn")
        self.update_scoreboard()

        ready = messagebox.askyesno(
            "Next Team", f"Is Team {self.current_team + 1} ready?"
        )
        if ready:
            self.next_card()
            self.start_timer()
        else:
            self.root.quit()

    def update_scoreboard(self):
        self.score_label.config(
            text=f"Team 1: {self.team_scores[0]}  |  Team 2: {self.team_scores[1]}"
        )


# ----------- RUN GAME -----------
root = tk.Tk()
game = TabooGame(root)
root.mainloop()
