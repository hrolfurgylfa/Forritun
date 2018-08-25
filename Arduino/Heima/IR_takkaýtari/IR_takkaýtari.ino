/*Þetta forrit tekur við skipunum frá IR fjarstýringu og snýr svo servo mótor til þess að ýta á takka*/
#include <IRremote.h>//Það þarf library sem heitir IRRemote og er búið til af shirriff
#include <Servo.h> // Þetta sækir libraryið sem stjórnar mótornum og þarf ekkert exterrnal library

#define IR_PIN 10
#define LEDpin 12
#define motor_pinni 6 // pinninn sem ég nota til að stjórna mótornum

IRrecv irrecv(IR_PIN);
decode_results ircode;

Servo motor; // bý til tilvik af Servo klasanum

void setup(){
    Serial.begin(9600);
    irrecv.enableIRIn();
    motor.attach(motor_pinni);
    motor.write(50);
    motor.detach();
}

void IRControl(){
    if (ircode.value == 0x4F5844BB || ircode.value == 0x36 || ircode.value == 0x836){
        Serial.println("2");
        blink();
        takki();
    }
}

void takki(){
    motor.attach(motor_pinni);
    motor.write(20);
    delay(300);
    motor.write(50);
    delay(50);
    motor.detach();
}

void blink(){
    digitalWrite(LEDpin,HIGH);
    delay(100);
    digitalWrite(LEDpin,LOW);
    delay(100);
}

void loop(){
    if (irrecv.decode(&ircode)){
        Serial.println("1");
        IRControl();
        irrecv.resume();
    }
}