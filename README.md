# Ironhack project 1 Mastermind

https://camo.githubusercontent.com/cb6ad07e6d2e77619e835c0569fa73beeb103a50/68747470733a2f2f7777772e6c65676f2e636f6d2f63646e2f63732f7365742f6173736574732f626c74343364373162646237613265653739332f7069636b2d612d627269636b2d62616e6e65722d6261636b67726f756e642d6c617267652e6a70673f77696474683d31333230266865696768743d323030266470723d31

Project Description

The project was to recreate the Mastermind game in Python, using the basic knowledge
acquired during the first week of the bootcamp. This game was selected because of its
research/guessing angles. It was an interesting challenge to make Python understand how
to compare lists properly to replicate the initial game.

Rules

In this version of the game the codifier is simply played by the computer. The player is 
first allowed to choose the number of tries that he has to guess the combination, and 
the length of the combinations.

The possible colors for the combinations are red, green, blue, yellow, white, black.

At each tries, the computer displays the number of elements that have the right position
and color, and the number of elements that have a correct color but not in the right
position.

The game stops whether when the player finds the combination or when has spent all his
tries has been spent.

Workflow

First the main organization was thinked about on Thursday, the functions to compare the
combinations and to format the player's guess. Eventually on Saturday and Sunday, all
the functions were made and fixed. The game was tested several times to check if it
works with different settings and combinations.

Organization

The code was made with Jupyter and Spyder, and using Zoom in the same time to discuss
about the ideas and the way to write it. The repository contains 3 pythons files :
- functions_mm.py ; contains all the functions
- main_mm.py ; contains an import of the python file with the functions and a line to 
call the whole game.
- full_project.py ; contains both the functions and the line to call the main function
and the game. It was the file used to create most of the code.

Otherwise the repository contains a .gitignore file, a LICENSE file and a README (that
you're currently reading).

Links

Repository : https://github.com/JBoissonnat/project_mastermind1
Presentation GS : https://docs.google.com/presentation/d/12KkFZ23lvVWq0GXDXWbt_2pdy8DF39V_GaGb6Ahn1gA/edit?usp=sharing

