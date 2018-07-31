from sense_hat import SenseHat
from time import sleep


sense = SenseHat()

sense.clear()

o = sense.get_orientation()
pitch = o['pitch']
roll = o['roll']
yaw = o['yaw']

print(
    "Pitch: {0} Roll: {1} Yaw: {2}"
    .format(pitch, roll, yaw)
)

for x in range(10):

    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = round(x, 0)
    y = round(y, 0)
    z = round(z, 0)

    print(
        "x={0}, y={1}, z={2}"
        .format(x, y, z)
    )
    sleep(0.05)

for x in range(10):

    sense.show_letter("J")

    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = round(x, 0)
    y = round(y, 0)
    z = round(z, 0)

    print(
        "x={0}, y={1}, z={2}"
        .format(x, y, z)
    )

    # update the rotation of the display
    if x == -1:
        sense.set_rotation(180)
    elif y == 1:
        sense.set_rotation(90)
    elif y == -1:
        sense.set_rotation(270)
    else:
        sense.set_rotation(0)

    if x > 1 or y > 1 or z > 1:
        sense.show_letter("!", (255, 0, 0))
    else:
        sense.clear()
    
    sleep(0.05)
