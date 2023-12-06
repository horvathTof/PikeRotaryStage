
import serial
import time  #only to use sleep command for the test

# Define the serial port and baud rate
serial_port = 'COM3'
baud_rate = 9600

try:
    ser = serial.Serial(serial_port, baud_rate, timeout=1)
    print(f"Serial port {serial_port} opened successfully.")

    if not ser.is_open:
        ser.open()

except serial.SerialException as e:
    print(f"Failed to open serial port: {e}")
    exit()

if ser:

    #Check data reading. Expect "Stepper motor control start-up.
    serial_data = ser.readline().decode().strip()   # Read the line and decode from bytes to string
    while serial_data:                              # Loop until all buffered messages have been red
        print("From Arduino:", serial_data)             # Print the message
        serial_data = ser.readline().decode().strip()
            
    #SPD: Motor speed command 
    stringCommand="SPD30"+ '\n'          # command that set the speed to 20
    ser.write(stringCommand.encode())  # Send command via serial port

    serial_data = ser.readline().decode().strip()   # Read the line and decode from bytes to string
    while serial_data:                              # Loop until all buffered messages have been red
        print("From Arduino:", serial_data)             # Print the message
        serial_data = ser.readline().decode().strip()

    #ACT: Activate motor control command 
    stringCommand="ACT1" + '\n'        # command that activate the motor driver
    ser.write(stringCommand.encode())  # Send command via serial port

    serial_data = ser.readline().decode().strip()   # Read the line and decode from bytes to string
    while serial_data:                              # Loop until all buffered messages have been red
        print("From Arduino:", serial_data)             # Print the message
        serial_data = ser.readline().decode().strip()

    #MOV: Move stepper motor command. 1 step = 1 degree because of gear reduction.
    for i in range(5):
        stringCommand="MOV10"+ '\n'          # command that makes a rotation CW
        ser.write(stringCommand.encode())  # Send command via serial port

        serial_data = ser.readline().decode().strip()   # Read the line and decode from bytes to string
        while serial_data:                              # Loop until all buffered messages have been red
            print("From Arduino:", serial_data)             # Print the message
            serial_data = ser.readline().decode().strip()
        time.sleep(1)


    #MOV: Move stepper motor command. minus value rotate in the other direction
    stringCommand="MOV-10"+ '\n'          # command that makes a rotation CCW
    ser.write(stringCommand.encode())  # Send command via serial port

    serial_data = ser.readline().decode().strip()   # Read the line and decode from bytes to string
    while serial_data:                              # Loop until all buffered messages have been red
        print("From Arduino:", serial_data)             # Print the message
        serial_data = ser.readline().decode().strip()
    

    #ACT: Desactivate motor control command. Recommanded during long idle period to prevent heating
    stringCommand="ACT0"+ '\n'          # command that desactivate the motor driver during idle phases
    ser.write(stringCommand.encode())  # Send command via serial port

    serial_data = ser.readline().decode().strip()   # Read the line and decode from bytes to string
    while serial_data:                              # Loop until all buffered messages have been red
        print("From Arduino:", serial_data)             # Print the message
        serial_data = ser.readline().decode().strip()


    ser.close()  # Close the serial port
    print("Serial port closed.")