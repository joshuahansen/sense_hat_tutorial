from sense_hat import SenseHat
from time import sleep
from random import randint


sense = SenseHat()

sense.show_letter("Z")

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

sense.show_letter("L", red)
sleep(1)
sense.show_letter("a", blue)
sleep(1)
sense.show_letter("u", green)
sleep(1)
sense.show_letter("r", white)
sleep(1)
sense.show_letter("a", yellow)


def pick_random_colour():
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)
    return (random_red, random_green, random_blue)


sense.show_letter("L", pick_random_colour())
sleep(1)
sense.show_letter("a", pick_random_colour())
sleep(1)
sense.show_letter("u", pick_random_colour())
sleep(1)
sense.show_letter("r", pick_random_colour())
sleep(1)
sense.show_letter("a", pick_random_colour())
