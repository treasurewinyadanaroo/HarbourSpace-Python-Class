import random

# Piles and their meanings for each round
piles_round_1 = {
    1: ("Red Rose", "Passion is blooming in your love life—embrace it, but remember to protect your heart and nurture healthy boundaries."),
    2: ("White Feather", "Clarity and new beginnings are on the horizon. Let go of past heartaches and open your heart to a fresh, honest connection."),
    3: ("Golden Key", "You are unlocking new levels of love and potential in your relationships. Trust in the process, and allow vulnerability to open doors to deeper intimacy.")
}

piles_round_2 = {
    1: ("Moonstone", "Trust your intuition in love. Emotional healing is key right now—listen to your inner voice, and let it guide you to the love that nurtures your soul."),
    2: ("Butterfly", "Love is transforming. Whether it’s a relationship evolving or a personal shift, embrace the changes—this transformation will lead you to a more beautiful, fulfilling love."),
    3: ("Flame", "Passion and energy are igniting in your love life. It’s a time for action—don’t hold back. Let your desire and confidence lead you toward an exciting romantic adventure.")
}

piles_round_3 = {
    1: ("💎 Diamond", "Your love is precious and rare. Cherish the value of what you have or seek in a relationship. It’s time to appreciate the true, lasting connections that shine brightest."),
    2: ("🌊 Ocean Wave", "Emotions run deep. Let your feelings flow naturally, allowing love to grow and evolve like the tides. Don't resist—embrace the depth and rhythm of your heart."),
    3: ("☀️ Sun", "Joy and warmth surround your love life. Happiness and positivity will light up your romantic journey, bringing clarity and a sense of fulfillment. Bask in this energy!")
}

# Step 1: Shuffle piles for each round
def shuffle_piles(pile_dict):
    piles = list(pile_dict.items())  # Get list of piles with their descriptions
    random.shuffle(piles)  # Shuffle them randomly
    return piles  # Return shuffled piles

# Step 2: Pick a pile from the 3 shuffled piles
def pick_pile():
    while True:
        try:
            choice = int(input("Pick a pile (1, 2, or 3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid input, choose 1, 2, or 3.")
        except ValueError:
            print("Please enter a number.")

# Step 3: Gather piles, placing the chosen pile in the middle
def gather_piles(piles, chosen_pile):
    if chosen_pile == 1:
        return piles[1], piles[0], piles[2]
    elif chosen_pile == 2:
        return piles[0], piles[1], piles[2]
    elif chosen_pile == 3:
        return piles[0], piles[2], piles[1]

# Step 4: Play one round of the game
def play_round(piles, round_num):
    print(f"\nRound {round_num}:")
    print("Pile 1:", piles[0][1], "\nPile 2:", piles[1][1], "\nPile 3:", piles[2][1])
    chosen_pile = pick_pile()
    
    piles = gather_piles(piles, chosen_pile)  # Gather piles based on player's choice
    return piles, chosen_pile

# Step 5: Reveal the final pile after 3 rounds
def reveal_pile(piles, chosen_pile, round_dict):
    final_pile = piles[1]  # The middle pile is the chosen pile after 3 rounds
    pile_name, interpretation = round_dict[chosen_pile]
    print(f"\nFinal Reveal:\nYou chose the {pile_name} pile.")
    print(f"Interpretation: {interpretation}")

# Step 6: Play the full game with 3 rounds
def pick_a_pile_game():
    # Round 1
    shuffled_piles = shuffle_piles(piles_round_1)
    shuffled_piles, chosen_pile = play_round(shuffled_piles, 1)
    
    # Round 2
    shuffled_piles = shuffle_piles(piles_round_2)
    shuffled_piles, chosen_pile = play_round(shuffled_piles, 2)
    
    # Round 3
    shuffled_piles = shuffle_piles(piles_round_3)
    shuffled_piles, chosen_pile = play_round(shuffled_piles, 3)
    
    # Final Reveal
    reveal_pile(shuffled_piles, chosen_pile, piles_round_3)

# Start the game
pick_a_pile_game()
