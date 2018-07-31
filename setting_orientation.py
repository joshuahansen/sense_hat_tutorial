from sense_hat import SenseHat
from time import sleep


sense = SenseHat()

sense.set_pixel(2, 2, (0, 0, 255))
sense.set_pixel(4, 2, (0, 0, 255))
sense.set_pixel(3, 4, (100, 0, 0))
sense.set_pixel(1, 5, (255, 0, 0))
sense.set_pixel(2, 6, (255, 0, 0))
sense.set_pixel(3, 6, (255, 0, 0))
sense.set_pixel(4, 6, (255, 0, 0))
sense.set_pixel(5, 5, (255, 0, 0))

sleep(2)

w = (150, 150, 150)
b = (0, 0, 255)
e = (0, 0, 0)

image = [
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    w, w, w, e, e, w, w, w,
    w, w, b, e, e, w, w, b,
    w, w, w, e, e, w, w, w,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
]

sense.set_pixels(image)

for x in range(30):
    sleep(0.5)
    sense.flip_h()

sleep(2)

sense.clear()
