"""This is a number guess program.
One way to play with the computer if you have no one to talk to."""
from random import randint
from time import sleep

def get_user_guess():
  guess = int(input("Guess a number: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides*2
  print ("The maximum possible value is: {}".format(max_val))
  return max_val, first_roll, second_roll
max_val, first_roll, second_roll = roll_dice(6)
guess = get_user_guess()

if guess > max_val:
  print ("Guess number to high.")
else:
  print ("Rolling...")
  sleep(2)
  print ("The 1st roll is: {}".format(first_roll))
  sleep(1)
  print ("The 2nd roll is: {}" .format(second_roll))
  sleep(1);
  total_roll = first_roll + second_roll;
  print ("The total roll is: {}".format(total_roll))
  print ("Result...")
  sleep(1)
  if guess == total_roll:
    print ("You won.")
  else:
    print ("You lose.")
  
  
