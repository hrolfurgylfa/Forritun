#include <Servo.h> // Sambærilegt og import í python

const int TrigPin = 4;//Trig attach to pin2
const int EchoPin = 5;//Echo attach to pin3
float cm; // fjöldi cm sem mældir eru

Servo motor; // bý til tilvik af Servo klasanum
int motor_pinni = 9; // pinninn sem ég nota til að stjórna mótornum
int att_upp = 1;
int motor_gradur = 0;

void setup(){
    Serial.begin(9600); //Sets the data rate in bits per second (baud) for serial data transmission
    //set the below pins as OUTPUT
    pinMode(TrigPin,OUTPUT);
    pinMode(EchoPin,INPUT);
    motor.attach(motor_pinni); // segi servo tilvikinu hvaða pinna á að nota
}

void loop(){
    for (int i = 0; i < 180; i = i + 15){
        //Þetta les ultrasonic skynjaran og setir það í breytuna cm
        digitalWrite(TrigPin,LOW);
        delayMicroseconds(2);
        digitalWrite(TrigPin,HIGH);
        delayMicroseconds(10);
        digitalWrite(TrigPin,LOW);
    
        cm = pulseIn(EchoPin,HIGH)/58.0;  
        cm = (int(cm * 100.0))/100.0;
        if(cm < 0){
            cm = 0;
        }
        //Serial.println(cm);

        if (cm < 20){
            while (cm < 20){
                delay(100);
            }
        }

        motor.write(i);

        Serial.println(i);
        delay(250);
    }
}