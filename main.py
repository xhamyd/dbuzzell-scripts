from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

# Generate a random colour
def pick_random_colour():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)

sense.show_letter("V", pick_random_colour())
sleep(1)
sense.show_letter("e", pick_random_colour())
sleep(1)
sense.show_letter("l", pick_random_colour())
sleep(1)
sense.show_letter("i", pick_random_colour())
sleep(1)
sense.show_letter("s", pick_random_colour())
sleep(1)
sense.show_letter("a", pick_random_colour())
sleep(1)

sense.clear()

