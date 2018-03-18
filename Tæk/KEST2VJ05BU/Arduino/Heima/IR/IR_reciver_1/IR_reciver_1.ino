#include <IRremote.h>

#define IR_PIN 4
#define LEDpin 8

IRrecv irrecv(IR_PIN);
decode_results ircode;

void setup(){
  Serial.begin(9600);
  irrecv.enableIRIn();
}
void loop(){
  if (irrecv.decode(&ircode)){
    Serial.println(ircode.value,HEX);
    irrecv.resume();
  }
}
