from sense_hat import SenseHat
sense = SenseHat()

sense.clear()

pressure = sense.get_pressure()
print("pressure: ", pressure)

temp = sense.get_temperature()
print("temperature: ", temp)
