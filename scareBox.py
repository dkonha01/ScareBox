#!/usr/bin/python
# Example using a character LCD plate.
import time

import Adafruit_CharLCD as LCD

import pygame.mixer


# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

pygame.mixer.init(48000,-16,1,1024)

audio1 = pygame.mixer.Sound("crows.wav")      #calling for audio file
audio2 = pygame.mixer.Sound("scream.wav")  #calling for audio file
audio3 = pygame.mixer.Sound("lidcreak.wav")      #calling for audio file
audio4 = pygame.mixer.Sound("wolfhowl.wav")      #calling for audio file
audio5 = pygame.mixer.Sound("arc.wav")

channel1 = pygame.mixer.Channel(1)   #using channel one for first button
channel2 = pygame.mixer.Channel(2)   #using channel two for second button
channel3 = pygame.mixer.Channel(3)    #using channel three for second button
channel4 = pygame.mixer.Channel(4)   #using channel four for second button
channel5 = pygame.mixer.Channel(5)   #using channel five for second button

# create some custom characters
lcd.create_char(1, [2, 3, 2, 2, 14, 30, 12, 0])
lcd.create_char(2, [0, 1, 3, 22, 28, 8, 0, 0])
lcd.create_char(3, [0, 14, 21, 23, 17, 14, 0, 0])
lcd.create_char(4, [31, 17, 10, 4, 10, 17, 31, 0])
lcd.create_char(5, [8, 12, 10, 9, 10, 12, 8, 0])
lcd.create_char(6, [2, 6, 10, 18, 10, 6, 2, 0])
lcd.create_char(7, [31, 17, 21, 21, 21, 21, 17, 31])

# Show some basic colors.
#lcd.set_color(1.0, 0.0, 0.0)
#lcd.clear()
#lcd.message('RED \x01')
#time.sleep(3.0)

# Show button state.
lcd.clear()
lcd.message('Press buttons...')

# Make list of button value, text, and backlight color.
buttons = ( (LCD.SELECT, 'Select', (1,1,1)),
            (LCD.LEFT,   'Left'  , (1,0,0)),
            (LCD.UP,     'Up'    , (0,0,1)),
            (LCD.DOWN,   'Down'  , (0,1,0)),
            (LCD.RIGHT,  'Right' , (1,0,1)) )

print('Press Ctrl-C to quit.')
while True:
    # Loop through each button and check if it is pressed.
    for button in buttons:
        if lcd.is_pressed(LCD.UP):
            # Button is pressed, change the message and backlight.
            lcd.clear()
            channel1.play(audio1) 
            lcd.message('crows')
        if lcd.is_pressed(LCD.DOWN):
            lcd.clear()
            channel2.play(audio2)
            lcd.message('shock')
        if lcd.is_pressed(LCD.LEFT):
            lcd.clear()
            channel3.play(audio3)
            lcd.message('creak')
        if lcd.is_pressed(LCD.RIGHT):
            lcd.clear()
            channel2.play(audio4)
            lcd.message('howl')
        if lcd.is_pressed(LCD.DOWN):
            lcd.clear()
            channel5.play(audio5)
            lcd.message('shock')
         
