import random

game_data = {
    1: {
        "Pile 1": ("A red rose", 
                   "Passion is blooming in your love life—embrace it, but remember to protect your heart and nurture healthy boundaries."),
        "Pile 2": ("A white feather", 
                   "Clarity and new beginnings are on the horizon. Let go of past heartaches and open your heart to a fresh, honest connection."),
        "Pile 3": ("A golden key", 
                   "You are unlocking new levels of love and potential in your relationships. Trust in the process, and allow vulnerability to open doors to deeper intimacy.")
    },
    2: {
        "Pile 1": ("Moonstone", 
                   "Trust your intuition in love. Emotional healing is key right now—listen to your inner voice, and let it guide you to the love that nurtures your soul."),
        "Pile 2": ("Butterfly", 
                   "Love is transforming. Whether it’s a relationship evolving or a personal shift, embrace the changes—this transformation will lead you to a more beautiful, fulfilling love."),
        "Pile 3": ("Flame", 
                   "Passion and energy are igniting in your love life. It’s a time for action—don’t hold back. Let your desire and confidence lead you toward an exciting romantic adventure.")
    },
    3: {
        "Pile 1": ("💎 (Diamond)", 
                   "Your love is precious and rare. Cherish the value of what you have or seek in a relationship. It’s time to appreciate the true, lasting connections that shine brightest."),
        "Pile 2": ("🌊 (Ocean Wave)", 
                   "Emotions run deep. Let your feelings flow naturally, allowing love to grow and evolve like the tides. Don't resist—embrace the depth and rhythm of your heart."),
        "Pile 3": ("☀️ (Sun)", 
                   "Joy and warmth surround your love life. Happiness and positivity will light up your romantic journey, bringing clarity and a sense of fulfillment. Bask in this energy!")
    }
}

def display_welcome():
    print("Welcome to the Pick a Pile Game!")
    print("In this game, you will choose a pile in three rounds.")
    print("Each pile has a unique item and an interpretation related to love and relationships.")
    print("Let's see what the universe has in store for you!\n")

def display_piles(round_number):
    print(f"Round {round_number}:\n")
    for pile, (item, _) in game_data[round_number].items():
        print(f"{pile}: {item}")
    
def get_user_choice():
    while True:
        chosen_pile = input("Choose a pile (Pile 1, Pile 2, Pile 3): ").strip()
        if chosen_pile in ["Pile 1", "Pile 2", "Pile 3"]:
            return chosen_pile
        else:
            print("Invalid choice. Please choose a valid pile.")

def display_interpretation(round_number, chosen_pile):
    item, interpretation = game_data[round_number][chosen_pile]
    print(f"\nYou chose {item}.")
    print(f"Interpretation: {interpretation}\n")

def play_round(round_number):
    display_piles(round_number)
    chosen_pile = get_user_choice()
    display_interpretation(round_number, chosen_pile)

def pick_a_pile_game():
    display_welcome()
    score = 0 
    
    for round_number in range(1, 4):
        play_round(round_number)
        score += 1

        print("-" * 30) 

    print(f"Your total score: {score}/3")
    print("Thank you for playing the Pick a Pile Game!")

def ask_replay():
    while True:
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay in ["yes", "no"]:
            return replay == "yes"
        else:
            print("Please answer with 'yes' or 'no'.")

if __name__ == "__main__":
    while True:
        pick_a_pile_game()
        if not ask_replay():
            break
