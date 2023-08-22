# Untitled - By: ASELA - Tue Aug 22 2023

import lcd
import time

# Initialize LCD screen
lcd.init(freq=15000000)
lcd.rotation(0)  # Set screen rotation if needed

# Clear the screen
lcd.clear(lcd.WHITE)

# Set text color and background color
text_color = lcd.BLACK
background_color = lcd.WHITE

# Set font size and position
font_size = 3
x_pos = 50
y_pos = 100

# Display text
lcd.draw_string(x_pos, y_pos, "Hello, Guna Busa", text_color, background_color)

# Refresh the display
lcd.display()

# Wait for a few seconds
time.sleep(5)

# Clear the screen before exiting
lcd.clear(background_color)
lcd.display()
