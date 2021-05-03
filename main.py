import serial
rx = serial.Serial('COM4', 9600,timeout = 1) #intitalising Serial Connection between Arduino and PC

while True:

    line = rx.readline() #read receieved byte
    #print (line)
    if line:
        decoded = line.decode() #converting byte to string
        stripped = decoded.strip() #deleting next line code from the string
        val_list = stripped.split(',') #splitting string into 2 substring
        #print(val_list)
        
        val_1 = int(val_list[0]) #value of 5v to 3.3v
        #print(val_1)
        val_2 = int(val_list[1]) #value of 3.3v to 1v
        #print(val_2)

        #min step size (multiplication factor)
        m = 5.0/1024 

        #Output from analog reading to Volts
        out1= val_1 * m 
        out2= val_2 * m
        print('5v -',round(out1,1),'\t3.3v -',round(out2,1))

    else:
        print('No Value received')
        print('Press the Button to send values')
            
