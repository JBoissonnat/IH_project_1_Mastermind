# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import random

def generate_combination(len_comb):
    
    '''
    This function generate a combination of colors. Each colors can appear several times.
    
    Input : length of the combination to generate (as an integer).
    Output : a list of random colors of the length given in input.
    
    It's possible to modify the colors that are used by updating the possible colors list
    inside the function.
    '''
    
    possible_colors = ["yellow", "blue", "red", "green", "white", "black"]
    
    comb = [possible_colors[random.randint(0,5)] for i in range(len_comb)]
    
    return comb

def verify_length(guess, a):
    
    '''
    This function verifies the length of the guess combination that the player can enter
    in the manage_players_entries function.
    
    Input : the list for which the length must be verified, and the length wanted.
    Output : True if the list has the right length, False if not.
    
    '''
    
    length_guess = len(guess)
    
    length_combination_to_guess = a
    
    if length_guess == length_combination_to_guess:
        return True
    else:
        return False
    

def manage_players_entries(list_parameters):
    
    '''
    This function asks the player to input its guess, and transforms it into a proper list
    to compare it with the list of the combination to guess. It also uses the function
    verify_length to check if the list provided is adequate.
    
    Input : list containing as second element a parameter of length.
    Output : the guess of the player as a list.
    
    It's possible to modify the colors that can be used by updating the possible colors list
    (liste) inside the function.
    '''
    
    a = list_parameters[1]
    
    correct_guess = False
    
    while correct_guess == False:
        
        saisie = input('Enter your color combination from [yellow, blue, red, green, white, black] ; There must be '+str(list_parameters[1])+' colors ! ')
    
        if "," in saisie:
            guess1 = saisie.split(",")
        else:
            guess1 = saisie.split()

        #print(guess1)
        guess=[]
        liste=["yellow", "blue", "red", "green", "white", "black"]
        for i in guess1 :
            if i in liste:
                guess.append(i)
    
        correct_length = verify_length(guess, a)
    
        if correct_length == True:
            
            correct_guess = True
        else:
            print("\nYou must enter a combination of "+str(list_parameters[1])+" colors !")
            
    return guess


def compare_combination(comb_to_guess, player_comb):
    
    '''
    This function compares the combination to guess with the player's guess. It counts
    the number of elements that have a right color and position, and the number of elements
    that have a correct color but not a correct position, in the player's guess combination.
    It checks if the player found the right combination.
    
    Input : the combination to guess and the player's guess combination as lists.
    Output : a True if the player has found the combination to guess, and a copy of
    the original combination to guess as a list.
    
    The function modifies the list as it count the different indicators. Therefore a copy of the
    original combination to guess has to be made because it stays the same. If the player is 
    able to find the combination, it prints a winner message.
    '''
    
    print("\n###### Lists entries")
        
    print("\nCombination to guess")
    print(comb_to_guess)
    print("\nPlayer's combination")
    print(player_comb)    
    
    correct_pos = 0
    correct_col = 0
    
    correct_guess = False
    
    comb_to_guess_copy = comb_to_guess.copy()
    
    # count correct positions
    
    for i in range(len(player_comb)):
        if player_comb[i] == comb_to_guess[i]:
            correct_pos+=1
            player_comb[i]="*"
            comb_to_guess[i]="*"
            
    player_comb = list(filter(("*").__ne__, player_comb))
    comb_to_guess = list(filter(("*").__ne__, comb_to_guess))
    
    print("\n###### Same position removed")
    print("\nCombination to guess")        
    print(comb_to_guess)
    print("\nPlayer's combination")
    print(player_comb)        

    # count correct colors
    
    for i in range(len(player_comb)):
        for j in range(len(comb_to_guess)):
            if player_comb[i] == comb_to_guess[j]:
                player_comb[i] = "*"
                comb_to_guess[j] = "*"
                
    print("\n###### Common colors removed")
    print("\nCombination to guess")
    print(comb_to_guess)
    print("\nPlayer's combination")
    print(player_comb) 
    
    correct_col = player_comb.count("*")
    
    print("\nCorrect position(s) and color(s) : "+str(correct_pos)+" Correct color(s) : "+str(correct_col))
    
    a = len(comb_to_guess_copy)
    
    if correct_pos == a:
        
        print("\n###### Congrats !!! You found the correct combination ! ######")
        
        correct_guess = True
        
        return correct_guess
    
    else:
        print("\nWrong answer ! Keep searching...")
    
    return comb_to_guess_copy

def set_parameters():
    
    '''
    This function asks the player the number of tries that he will have to guess the combination,
    and the length of the combinations in the game.
    
    Input : None.
    Output : the two parameters inputs provided by the player as a list.
    
    Both parameters must be integers.
    '''
    
    tries = int(input("Enter maximum number of tries (must be integer) : "))
        
    length_combination = int(input("Enter the length of the combination (must be integer) : "))
    
    parameters = [tries, length_combination]
    
    return parameters

def main():
    
    '''
    This function is the main function of the Python Mastermind Game. It uses all the functions
    created for the game, directly or indirectly.
    
    Input : None.
    Output : None.
    
    It uses a while loop that keeps going if the maximum number of tries is not reached, and
    it breaks if the combination to guess is found. The loop asks the player's guess combination
    and compare the combination repeatedly. If the player is not able to find the combination,
    it prints a game over message.
    '''
    
    print("\n###### Welcome to the Python Mastermind Game ######")
    
    list_parameters = set_parameters()
    
    #print("\nParameters choosed :")
    #print("\nMaximum tries : "+str(list_parameters[0]))
    #print("Combinations length : "+str(list_parameters[1]))
    
    combination_to_guess = generate_combination(list_parameters[1])
    
    guess_tried = 0
    
    while (guess_tried < list_parameters[0]):
        
        guess_tried += 1
        print("\nTry "+str(guess_tried))
        
        player_combination = manage_players_entries(list_parameters)

        combination_to_guess = compare_combination(combination_to_guess, player_combination)

        if combination_to_guess == True:
            break
    
    if guess_tried == list_parameters[0]:
        print("\n###### Game is over ######")
    
    return None