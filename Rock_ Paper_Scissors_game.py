#Rock, Paper, & Scissors Game
import random

def rock_paper_scissors_game():

    game_list = ['rock', 'paper', 'scissors']


    comp_pick = random.choice(game_list)
    
    while True:
        
        print('Please choose one: rock, paper or scissors?')
        player = input()
     
     
        if player == comp_pick:
            print(f'Tie! Computer picked {comp_pick} too!')


        elif player == 'rock' and comp_pick == 'paper':
            print(f'Computer picked {comp_pick}! You lose!')
      
        elif player == 'paper' and comp_pick == 'rock':
            print(f'You win! Computer picked {comp_pick}!')

        elif player == 'rock' and comp_pick == 'scissors':
            print(f'You win! Computer picked {comp_pick}!')

        elif player == 'scissors' and comp_pick == 'rock':
            print(f'You lose! Computer picked {comp_pick}!')

        elif player == 'paper' and comp_pick == 'scissors':
            print(f'You lose! Computer picked {comp_pick}!')

        elif player == 'scissors' and comp_pick == 'paper':
            print(f'You win! Computer picked {comp_pick}!')


        else:

            print('Error!')
            False
        

      

rock_paper_scissors_game()
