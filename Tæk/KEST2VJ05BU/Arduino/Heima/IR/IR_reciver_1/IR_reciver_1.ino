#include <IRremote.h>//Það þarf library sem heitir IRRemote og er búið til af shirriff

#define IR_PIN 4

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
