from microbit import *
count = 0

# main loop
while True: 
    display.show(Image.ARROW_W)
    
    # wait for button a to be pressed
    while True:
        if button_a.is_pressed():
            break
    
    display.show(Image.ARROW_E)
    start_time = running_time()
    
    # open the next file
    count+=1
    with open('out%03i.csv' % (count), 'w') as my_file:
        # write the file headder
        my_file.write("time, x, y, z\n")

        while True:
            # check to see if b is pressed, if so exit
            if button_b.is_pressed():
                break
        
            # otherwise, log data
            x_val = accelerometer.get_x()
            y_val = accelerometer.get_y()
            z_val = accelerometer.get_z()
            my_file.write("%f, %f, %f, %f\n" % ((running_time()-start_time), x_val, y_val, z_val))
            sleep(100)