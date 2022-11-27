#include <Arduino.h>
#include <DMXSerial.h>

/**
* @brief the serial-communication and the dmx-receiver are initialiced
*/
void setup() {
  Serial.begin(115200);
  DMXSerial.init(DMXReceiver);
}

/**
* @brief it is checked if there are any new messages sent by the serial. If yes a dmx channel is read and then sent back over the serial. 
*/
void loop() {
  if(Serial.available() > 0)
  {
    String input = Serial.readStringUntil('\n');
    int index = input.toInt();
    Serial.println((String)DMXSerial.read(index));
  }
}