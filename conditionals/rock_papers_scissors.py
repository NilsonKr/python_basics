import random

## Rock papers scissors game

relations = {
  'Rock': 'Scissors',
  'Paper': 'Rock',
  'Scissors': 'Paper',
}

def game(): 
  options = {
    1: 'Rock',
    2: 'Paper',
    3: 'Scissors'
  }
  user_input = input('Cual seleccionas? : ')
  
  user_choice = options[int(user_input)] 
  cpu_choice = cpu()

  if user_choice == cpu_choice:
    print('Empate!, vamos de nuevo: ')
    return game()
  elif relations[user_choice] == cpu_choice:
    print(f'Ganaste! {user_choice} gana a {cpu_choice},  vamos de nuevo: ')
    return game()
  else :
    print(f'Perdiste :( {cpu_choice} gana a {user_choice},  vamos de nuevo: ')
    return game()
    


def cpu():
  random_choice = random.choice(list(relations.keys()))

  return random_choice


print('''ROCK, PAPER, SCISSORS!
        
        Seleciona para empezar a jugar
        
        1. Rock
        2. Paper
        3. Scissors
        ''')
game()

