# Untitled - By: ASELA - Tue Aug 22 2023

import lcd
import time
import image

# Initialize LCD screen
lcd.init(freq=15000000)
lcd.rotation(0)  # Set screen rotation if needed

# Clear the screen
lcd.clear(lcd.WHITE)

# Set text color and background color
text_color = lcd.BLACK
background_color = lcd.WHITE

# Display text
loading = image.Image(size=(lcd.width(), lcd.height()))
loading.draw_rectangle((0, 0, lcd.width(), lcd.height()), fill=True, color=background_color)

info = "Hello, Guna Busa"
loading.draw_string(int(lcd.width()//2 - len(info) * 5), (lcd.height())//4, info, color=text_color, scale=2, mono_space=0)

# Refresh the display
lcd.display(loading)

# Wait for a few seconds
time.sleep(5)

# Clear the screen before exiting
loading.clear()
lcd.clear(background_color)

lcd.display(loading)
