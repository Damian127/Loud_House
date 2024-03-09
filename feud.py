def check_guess(guess, answer_list, buzzer):
  """Checks if player guess is in the answer list and returns how many points gained if any"""
  if guess in game_board:
    print("you already guessed this")
    
  if guess in answer_list:
    index = list(answer_list.keys()).index(guess)
    index_num = index + 1
    game_board[str(index + 1)] = guess
    print(f"{player1} guessed the number {index_num} ")
    return buzzer
  elif guess not in answer_list:
   
    
    buzzer += 1
    print(f"Wrong you got {buzzer}")
  return buzzer


def score_card():
  print(f"{player1}: points: {score} X's: {buzzer}")
  print(game_board)


question = "name something associated with vampires ".title()
answer_list = {
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
answer_list_length = len(answer_list)

score = 0
buzzer = 0
end_of_game = False

game_board = {str(i + 1): '_' for i in range(len(answer_list))}

player1 = "Damian"
print(
    f"Round one with {answer_list_length} answers on the board \n{game_board} the question is: "
)

while not end_of_game :
  
  guess = input(question)
  buzzer = check_guess(guess, answer_list, buzzer)
  score_card()
  if buzzer == 4:
    end_of_game = True
