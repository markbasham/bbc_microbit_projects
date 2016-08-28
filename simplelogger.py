from microbit import *

POLL_TIME = 10
MAX_FRAMES = 100

# main loop
while True: 
    display.show(Image.ARROW_W)

    # wait for button a to be pressed
    while True:
        if button_a.is_pressed():
            break

    display.show(Image.SMILE)
    start_time = running_time()

    # open the file
    with open('output.csv', 'w') as my_file:
        # write the file headder
        my_file.write("time, x, y, z\n")
        
        count = 0
        while count < MAX_FRAMES:
            count+=1
            # log data
            x_val = accelerometer.get_x()
            y_val = accelerometer.get_y()
            z_val = accelerometer.get_z()
            my_file.write("%i, %i, %i, %i\n" % ((running_time()-start_time), x_val, y_val, z_val))
