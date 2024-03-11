import os
from random import randint, choice
from questions import *
import random
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# Rest of the existing code remains unchanged
def check_guess(guess, answer_list, buzzer, game_board):
  """Checks if player guess is in the answer list and returns how many points gained if any"""
  
  
  if guess in game_board:
    print("you already guessed this")

  if guess in answer_list:
    index = list(answer_list.keys()).index(guess)
    index_num = index + 1
    game_board[str(index + 1)] = guess
    clear()
    print(f"{player1} guessed the number {index_num} answer ")
    return buzzer
  elif guess not in answer_list:

    buzzer += 1
    clear()
    print(f"Survey says: [X] {guess} is not on the board")
  return buzzer


def score_card():
  print(f"{player1}: points: {score} [X]'s: {buzzer}")
  print(game_board)


def add_points(guess):
  points = answer_list[guess]
  print(f"Survey says {guess} is worth {points}")
  return points
def guess(answer_list):
  pass


def get_question():
  question = game_questions[randint(0,2)]
  for key in question:
    question1 = key
    print(question1)
  answer_list1 = (question[key])
  return  question1

def get_answer_list():
  pass
  game_questions 
  return  answer_list1

question =question3
answer_list = answer_list3
answer_list_length = len(answer_list)



end_of_game = False
score = 0
buzzer = 0
game_board = {str(i + 1): '_' for i in range(len(answer_list))}

player1 = "Damian"
def game():
  global end_of_game
  global score 
  global buzzer 
  print(logo)
  print(
    f"Round one with {answer_list_length} answers on the board \n{game_board} the question is: "
  )

  while not end_of_game:

    guess = input(question)
    buzzer = check_guess(guess, answer_list, buzzer, game_board)
    if guess in answer_list:
      score += add_points(guess)
    score_card()
    if buzzer == 3 or score == 100:
      end_of_game = True
      clear()
  
  print(f"GAME OVER you ended with {score} points ")
  print(answer_list)



game()