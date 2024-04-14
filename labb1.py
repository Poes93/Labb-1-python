import random


def sten_sax_påse_spel():
    choices = ["sten", "sax", "påse"]
    computer_choice = random.choice(choices)
    user_choice = input("Välj 'sten', 'sax', eller 'påse': ").lower()

    while user_choice not in choices:
        user_choice = input("Felaktigt val. Välj 'sten', 'sax', eller 'påse': ").lower()

    print(f"Datorns val: {computer_choice}")
    print(f"Ditt val: {user_choice}")

    if user_choice == computer_choice:
        print("Oavgjort!")
    elif (
        (user_choice == "sten" and computer_choice == "sax")
        or (user_choice == "sax" and computer_choice == "påse")
        or (user_choice == "påse" and computer_choice == "sten")
    ):
        print("Du vann!")
        return True
    else:
        print("Du förlorade!")
        return False


# Startar spelet
def main():
    win = False
    while not win:
        win = sten_sax_påse_spel()


if __name__ == "__main__":
    main()
