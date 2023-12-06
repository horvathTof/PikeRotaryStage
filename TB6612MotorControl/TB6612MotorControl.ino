#include <Arduino.h>
#include <Stepper.h>

#define SPEED 10
#define STEPS 200

Stepper stepper(STEPS, 4, 5, 6, 7);
const int standbyPin = 8;

void setup() {
  Serial.begin(9600);
  Serial.println("Stepper motor control start-up.");

  stepper.setSpeed(SPEED);

  pinMode(standbyPin, OUTPUT);
  digitalWrite(standbyPin, LOW);
  

}

void loop() {
  if (Serial.available() > 0) {
    String serialInput = Serial.readStringUntil('\n');
    if (serialInput.length() >= 4) {
      Serial.println("serial received: " + serialInput);
      String command = serialInput.substring(0, 3); // Extract the first 3 characters
      String parameterStr = serialInput.substring(3);   // Extract the remaining part of the string
      int parameter = parameterStr.toInt(); // Convert the remaining part to an integer
    
      if (command == "MOV") {
        stepper.step(parameter);
        //Serial.println("MOV command executed");
      } else if (command == "SPD") {
        stepper.setSpeed(parameter);
        //Serial.println("SPD command executed");
      } else if (command == "ACT") {
        if (parameter == 0) {
          digitalWrite(standbyPin, LOW);
        } else {
          digitalWrite(standbyPin, HIGH);
        }
      }
      Serial.println("done");
    }
  }
}
