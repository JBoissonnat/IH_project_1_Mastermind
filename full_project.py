# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import random

def generate_combination(len_comb):
    
    possible_colors = ["yellow", "blue", "red", "green", "white"]
    
    comb = [possible_colors[random.randint(0,5)] for i in range(len_comb)]
    
    return comb

def verify_length(guess, a):
    length_guess = len(guess)
    
    length_combination_to_guess = a
    
    if length_guess == length_combination_to_guess:
        return True
    else:
        return False
    

def manage_players_entries(list_parameters) :
    
    a = list_parameters[1]
    
    correct_guess = False
    
    while correct_guess == False:
        
        saisie = input('Enter your color combination from [yellow, blue, red, green, white] ; There must be '+str(list_parameters[1])+' colors !')
    
        if "," in saisie:
            guess1 = saisie.split(",")
        else:
            guess1 = saisie.split()

        print(guess1)
        guess=[]
        liste=["yellow", "blue", "red", "green", "white"]
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
        
        print("\nYou found the correct combination !")
        
        correct_guess = True
        
        return correct_guess
    
    else:
        print("\nWrong answer !")
    
    return comb_to_guess_copy

def set_parameters():
    
    tries = int(input("Enter maximum number of tries (must be integer) : "))
        
    length_combination = int(input("Enter the length of the combination (must be integer) : "))
    
    parameters = [tries, length_combination]
    
    return parameters

def main():
    
    list_parameters = set_parameters()
    
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
        print("\nGame Over - Play another time")
        
##########

main()


