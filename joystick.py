from sense_hat import SenseHat
from time import time, sleep


sense = SenseHat()

start = time()

while True:

    for event in sense.stick.get_events():
        print(event.direction, event.action)

    end = time()
    if (end - start) > 10:
        break


e = (0, 0, 0)
w = (255, 255, 255)

sense.clear()

start = time()

while True:

    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                sense.show_letter("U")
            elif event.direction == "down":
                sense.show_letter("D")
            elif event.direction == "left":
                sense.show_letter("L")
            elif event.direction == "right":
                sense.show_letter("R")
            elif event.direction == "middle":
                sense.show_letter("M")

            sleep(0.5)
            sense.clear()

    end = time()
    if (end - start) > 10:
        break
