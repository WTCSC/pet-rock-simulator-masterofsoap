import random
import sys
import time

def rock_art(happiness):
    """Return ASCII art for the rock based on happiness."""
    if happiness >= 7:
        return "(^_^)  A happy rock!"
    elif 4 <= happiness < 7:
        return "(-_-)  A bored rock."
    else:
        return "(T_T)  A very sad rock..."

def main():
    # Setup
    name = input("What will you name your pet rock? ")
    rock = {
        "happiness": 5,
        "hunger": 5,
        "energy": 5
    }

    print(f"\nCongratulations! You've adopted {name}, your new pet rock.\n")

    # Game Loop
    while True:
        # Display stats
        print("\n")
        print(f"--- Your Pet Rock, {name} ---")
        print(rock_art(rock["happiness"]))
        print(f"Happiness: {rock['happiness']}/10")
        print(f"Hunger:    {rock['hunger']}/10")
        print(f"Energy:    {rock['energy']}/10")

        # Check game over
        if rock["happiness"] <= 0:
            print(f"\n{name} became too depressed and rolled away into the wilderness.")
            print("GAME OVER")
            break
        if rock["hunger"] >= 10:
            print(f"\n{name} starved from neglect and now refuses to be your pet.")
            print("GAME OVER")
            break
        if rock["energy"] <= 0:
            print(f"\n{name} ran out of energy and is now in eternal rock sleep.")
            print("GAME OVER")
            break

        # Menu
        print("\nWhat do you want to do?")
        print(f"1. Feed {name}")
        print(f"2. Play with {name}")
        print(f"3. Let {name} rest")
        print("4. Do nothing")
        print("5. Quit")

        choice = input("Your choice: ").strip()

        # Handle actions
        if choice == "1":  # Feed
            rock["hunger"] -= 3
            rock["happiness"] -= 1
            rock["energy"] -= 1
            print(f"\nYou fed {name}. Rocks don’t need food, but somehow it worked.")
        elif choice == "2":  # Play
            rock["happiness"] += 3
            rock["hunger"] += 2
            rock["energy"] -= 2
            print(f"\nYou played with {name}. It rolled in joy!")
        elif choice == "3":  # Rest
            rock["energy"] += 3
            rock["hunger"] += 1
            print(f"\n{name} rests peacefully. Its energy is restored.")
        elif choice == "4":  # Do nothing
            rock["happiness"] -= 2
            rock["hunger"] += 1
            print(f"\nYou ignored {name}. It stares into the void...")
        elif choice == "5":  # Quit
            print(f"\nYou abandoned {name}. Cold-hearted move.")
            print("GAME OVER")
            break
        elif choice.lower() == "secret":  # Hidden action
            rock["happiness"] = 10
            rock["hunger"] = 0
            rock["energy"] = 10
            print(f"\nSECRET POWER! {name} is now a legendary shiny rock!")
        else:
            print(f"\n{name} tilts slightly... it doesn’t understand.")

        # Random events
        if random.random() < 0.2:  # 20% chance per turn
            event = random.choice(["bird", "rain", "sun"])
            if event == "bird":
                rock["happiness"] += 2
                print(f"\n🐦 A bird landed on {name}! It feels special.")
            elif event == "rain":
                rock["hunger"] -= 1
                print(f"\nRain falls, washing {name}. It feels refreshed.")
            elif event == "sun":
                rock["energy"] += 1
                print(f"\nSunshine warms {name}. It gains energy.")

        # Passive changes (time passes)
        rock["happiness"] -= 1
        rock["hunger"] += 1

        # Clamp stats to 0–10
        for key in rock:
            rock[key] = max(0, min(10, rock[key]))

        time.sleep(1)  # Slow it down a little for readability

if __name__ == "__main__":
    main()
