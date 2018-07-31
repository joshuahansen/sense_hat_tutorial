from sense_hat import SenseHat


sense = SenseHat()

sense.clear()

pressure = sense.get_pressure()
print("Pressure: ", pressure)

temp = sense.get_temperature()
print("Temperature: ", temp)

humidity = sense.get_humidity()
print("Humidity: ", humidity)

for x in range(2):

    # Take reading from all 3 sensors
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    # Round values to one decimal place
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    # Create message to display on sense hat
    message = (
        "Temperature: " + str(t) +
        " Pressure: " + str(p) +
        " Humidity: " + str(h)
    )

    # Display message
    sense.show_message(message, scroll_speed=0.05)

red = (255, 0, 0)
green = (0, 255, 0)

for x in range(2):

    # Take reading from all 3 sensors
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    # Round values to one decimal place
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    # Create message to display on sense hat
    message = (
        "Temperature: " + str(t) +
        " Pressure: " + str(p) +
        " Humidity: " + str(h)
    )

    if t > 18.3 and t < 26.7:
        bg = green
    else:
        bg = red

    # Display message
    sense.show_message(message, back_colour=bg, scroll_speed=0.05)

sense.clear()
