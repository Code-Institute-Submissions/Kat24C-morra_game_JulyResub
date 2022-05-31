# Morra game
Morra game is a Python terminal game, which user the Code Institute mock terminal on Heroku to run. 

Users must try win by guessing the computers number before the computer can guess the user number. 
https://morra-game.herokuapp.com/

![live-version](https://user-images.githubusercontent.com/98415901/171197867-502a40b6-19a8-4403-8a66-9160d1d15e1c.jpg)

### User stories
 * The user needs to guess the computers number and choose a number between 1 and 3
 * The user needs to see if they scored or the computer scored. 
 * The user will see the total throughout the game. 
 * The user will be able to see if they win or the computer wins. 
 * The user gets to choose if they want to play again. 

## How to play

Morra game is based on the hand game Morra. You can find out more about Morra at the link provided: https://en.wikipedia.org/wiki/Morra_(game). 

In this version, the player enters their name and the rules of the game will be displayed. 

The user will then get to choose their own number between 1 and 3, it will then show the computers guess. 

The user must then guess what they think the computer will choose, afterwards it will show the computers chosen number. 

It will then show the users and computers results for the current round and it will show the total for the entire game.
The user and the computers will then take turns. 

The winner is the first one to reach a total of 12. 

## Features
 *  Asks user for name.
 *  Shows the rules for the game. 

![userdetails](https://user-images.githubusercontent.com/98415901/171198862-7614ee4d-c1fd-4d04-88c5-3cb58cb9f50b.jpg)

 *  Asks the user to choose a number between 1 and 3. 
 *  Computer will generate a number between 1 and 3. 
 *  Asks the user to guess the computers number between 1 and 3.
 *  Computer generates a number between 1 and 3.
 *  Maintains the scores. 

![number](https://user-images.githubusercontent.com/98415901/171200568-8d75bf19-5c17-4534-ad7a-92a74c8d2da4.jpg)

  * Input validation
    * You cannot enter a word or symbol. 
    * You must enter a number between 1 and 3

![error](https://user-images.githubusercontent.com/98415901/171200994-726e4c8f-5e0d-412d-a571-82cf29d9ef91.jpg)

  * Restart game
    * If user enters yes the game will restart. 
    * If the user enters no the game will end. 
    * If the user types anything else it will come up as an invalid option.
 
 ![playagain](https://user-images.githubusercontent.com/98415901/171202248-76e9bfb3-4954-45b5-9d88-660a353b2a0c.jpg)
 
 ## Testing
 ### User story testing
 * The user is able to input a number between 1 and 3
 * The user is able to see if they scored or the computer scored. 
 * The user is able see the total throughout the game. 
 * The user is able to see if they win or the computer wins. 
 * The user is able to choose if they want to play again. 

## Bugs
### Solved bugs

### Remaining Bugs
 * No bugs remain

### Validator Testing
 * PEP8
  * No errors were returned from PEP8online.com 

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku
 * Steps for deployment:
  * Create a new Heroku app. 
  * Set Convig Vars Key: Port Value: 8000. 
  * Set the buildbacks to Python and NodeJS in that order. 
  * Change Deployment method to GitHub. 
  * Connect to GitHub repository morra_game. 
  * Click on Deploy

## Credits
 * Code institute for the deployment terminal
 * https://mindyourdecisions.com/ for the rules of the Morra game.

 
