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
    IRControl();
    irrecv.resume();
  }
}
void IRControl(){
  switch(ircode.value){
    case 0x80C://Hérna bæti ég við 0x í byrjun tölunnar til þess að library-ið skilji þetta sem IR tölu
    Blink();
    Blink();
    Blink();
    break;
  }
}
void Blink(){
  digitalWrite(LEDpin,HIGH);
  delay(100);
  digitalWrite(LEDpin,LOW);
  delay(100);
}

