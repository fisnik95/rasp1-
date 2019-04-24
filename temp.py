from sense_hat import SenseHat
sense = SenseHat()
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
white = (255,255,255)
while True:

  # Take readings from all three sensors
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()

  # Round the values to one decimal place
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)
  
  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)
  
  if t >18.3 and t <26.7:
    bg = white 
  else:
    bg = red
    
  if p > 1000 and p < 1200:
    tg = blue
  else:
    tg = red
  if h > 30 and h < 50:
     hg = sense.set_rotation(90)
  else: 
    hg = sense.set_rotation(0) 
  
  # Display the scrolling message
  sense.show_message(message, scroll_speed=0.05, back_colour=bg, text_colour=tg)
