# montyhall
An implementation of the Monty Hall problem. See https://en.wikipedia.org/wiki/Monty_Hall_problem for more info about the problem.
The function `montyhall` can be called with no parameters, so you can play the game, or with params to simulate a game. Below the function I wrote code to simulate a given amount of games according to the settings variables. By default it calls the function 10,000 times starting with a random door, and always switching, then 10,000 times starting with a random door, and staying with the original choice all the time. Then it calculates the percentage, and prints them out.