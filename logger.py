from microbit import *
import os

# Set up some default parameters
POLL_TIME = 100
MAX_FRAMES = 300

# main loop
while True:
    # Prompt the user to press the left button(a)
    display.show(Image.ARROW_W)

    # Wait for button a to be pressed
    while True:
        if button_a.is_pressed():
            break

    # Let the user know the recording is ongoing
    display.show(Image.HAPPY)
    
    # record the start time so that all times can be offset
    start_time = running_time()
    
    # if the file already exists then remove it
    try:
        os.remove('output.csv')
    except:
        pass
        
    # open the file for writing     
    with open('output.csv', 'w') as my_file:
        # write the file header
        my_file.write("time, x, y, z\n")

        # Main recording loop
        count = 0
        while count < MAX_FRAMES:
            count+=1        
            # log data
            x_val = accelerometer.get_x()
            y_val = accelerometer.get_y()
            z_val = accelerometer.get_z()
            my_file.write("%i, %i, %i, %i\n" % ((running_time()-start_time), x_val, y_val, z_val))
            sleep(POLL_TIME)
 
            