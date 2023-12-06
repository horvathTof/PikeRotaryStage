# PikeRotaryStage
Driving stepper motor to rotate the sample holder of the Pike in the DNA project. 

#Hardware
Stepper motor Nema8
Motor driver Adafruit TB6612
Arduino nano Every

#Python control
stepperControl.py python script shows how to establish the serial communication with the Arduino in order to control the motor.

It is not necessary to open and close the serial communication each time. But it is recommanded to desactivate the driver for long period of idle step to prevent heating. Then the driver should be reactivate before initiating the next move.

#Arduino control
The step cycles are done by an Arduino nano using the standard Stepper library.
The Arduino nano is loaded with the file TB6612MotorControl.ino.
The Arduino catches command formated XXXY... in the serial communication to drive the motor. XXX is a 3 character command and Y is a digital parameter that can be of any length.
Commands are:
MOV : move the motor. Use negative values to turn counter clockwise.
SPD : set the speed of the motor
ACT : 0 to disable and 1 to activate the driver.

#Motor driver
The driver TB6612FNG embedded in the Adafruit TB6612 includes two H-bridges for motor control. Find Adafruit tutorial for wiring.

#Motor / mechanical
Motor is a NEMA8 4 wires stepper motor of 200 steps. A 27/15 gear reduction induces a final control of 1 degree per motor step.

