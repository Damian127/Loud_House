question = "name something associated with vampires ".title()
anwser = {
    "twilight": 33,
    "blood": 29,
    "bloodsucker": 29,
    "garlic": 9,
    "bat": 7,
    "cape": 7,
    "Dracula": 5,
    "Fangs": 4,
    "Halloween": 4
}

player1 = input("Who will be player one? ")
player2 = input("Who will be player two? ")
guess = input(question)
if guess in anwser:
  points = anwser[guess]
  print(f"Correct, {guess} is on the board for {points} ponts!.")

print(guess)
