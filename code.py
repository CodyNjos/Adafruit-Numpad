# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

from adafruit_macropad import MacroPad
    
macropad = MacroPad()
text_lines = macropad.display_text(title= 'nUMpAd')
num_lock = False
mode = True

text_lines[1].text = "NUMLOCK OFF" 
last_position = 0
macropad.keyboard.send(macropad.Keycode.KEYPAD_NUMLOCK)
while True:
    key_event = macropad.keys.events.get()
    
    if key_event:
        if key_event.pressed:
            if key_event.key_number == 0:
                macropad.keyboard.send(macropad.Keycode.KEYPAD_NUMLOCK)
                num_lock = not num_lock
                if num_lock == True:
                    text_lines[1].text = "NUMLOCK ON"  
                if num_lock == False:
                    text_lines[1].text = "NUMLOCK OFF" 

            if key_event.key_number == 1:
                macropad.keyboard.send(macropad.Keycode.B)
                text_lines[0].text = "-"  
            if key_event.key_number == 2:
                macropad.keyboard.send(macropad.Keycode.C)       
            if key_event.key_number == 3:
                macropad.keyboard.send(macropad.Keycode.KEYPAD_SEVEN)
                text_lines[0].text = "7"          
            if key_event.key_number == 4:
                macropad.keyboard.send(macropad.Keycode.KEYPAD_EIGHT)
                text_lines[0].text = "8"   
            if key_event.key_number == 5:
                macropad.keyboard.send(macropad.Keycode.KEYPAD_NINE)
                text_lines[0].text = "9"   
            if key_event.key_number == 6:
                macropad.keyboard.send(macropad.Keycode.KEYPAD_FOUR)
                text_lines[0].text = "4"   
            if key_event.key_number == 7:
                macropad.keyboard.send(macropad.Keycode.KEYPAD_FIVE)   
                text_lines[0].text = "5"        
            if key_event.key_number == 8:
                macropad.keyboard.send(macropad.Keycode.KEYPAD_SIX)
                text_lines[0].text = "6" 
            if key_event.key_number == 9:   
                macropad.keyboard.send(macropad.Keycode.KEYPAD_ONE)
                text_lines[0].text = "1"
            if key_event.key_number == 10:
                macropad.keyboard.send(macropad.Keycode.KEYPAD_TWO)
                text_lines[0].text = "2"   
            if key_event.key_number == 11:
                macropad.keyboard.send(macropad.Keycode.KEYPAD_THREE)
                text_lines[0].text = "3"   
            

    macropad.encoder_switch_debounced.update()
    
    text_lines.show()
    if macropad.encoder_switch_debounced.pressed:
                mode = not mode
                if mode == True:
                    text_lines[3].text = "MODE 1"  
                if mode == False:
                    text_lines[3].text = "MODE 2" 

    current_position = macropad.encoder
    if macropad.encoder < last_position:
        macropad.consumer_control.send(macropad.ConsumerControlCode.VOLUME_DECREMENT)
        last_position = current_position
        
    if macropad.encoder > last_position:
        macropad.consumer_control.send(macropad.ConsumerControlCode.VOLUME_INCREMENT)
        last_position = current_position
    