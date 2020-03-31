from sense_hat import SenseHat
# import firebase_admin
# from firebase_admin import credentials, firestore

#sense_hat
sense = SenseHat()

#color
blue=(0,0,255) 
# sense.show_letter('M')

#while True acceleration
while True:
    acceleration=sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = round(x,0)
    y = round(y,0)
    z = round(z,0)


    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1 or y > 1 or z > 1:
        sense.show_letter('Y', blue)
    else:
        sense.clear()
    
    #fanatsy of rotation
    #if x == -1:
        #sense.set_rotation(180)
    #elif y == 1:
        #sense.set_rotation(90)
    #elif y == -1:
        #sense.set_rotation(270)
    #else:
        #sense.set_rotation(0)