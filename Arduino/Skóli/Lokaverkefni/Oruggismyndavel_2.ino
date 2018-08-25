#include <Servo.h> // Sambærilegt og import í python
#include <IRremote.h>//Það þarf library sem heitir IRRemote og er búið til af shirriff

//IR
#define IR_PIN 10
IRrecv irrecv(IR_PIN);
decode_results ircode;
int IRKodi = 0;

//ultrasonic sensor
const int TrigPin = 4;//Trig attach to pin2
const int EchoPin = 5;//Echo attach to pin3
float cm; // fjöldi cm sem mældir eru

//Servo motor
Servo motor; // bý til tilvik af Servo klasanum
int motor_pinni = 9; // pinninn sem ég nota til að stjórna mótornum
int motor_gradur = 0;

void setup(){
    Serial.begin(9600); //Sets the data rate in bits per second (baud) for serial data transmission
    //set the below pins as OUTPUT
    pinMode(TrigPin,OUTPUT);
    pinMode(EchoPin,INPUT);
    motor.attach(motor_pinni); // segi servo tilvikinu hvaða pinna á að nota
    irrecv.enableIRIn();//Fyrir IR
}

void IRControl(){
    if (irrecv.decode(&ircode)){
        Serial.println(ircode.value,HEX);
        irrecv.resume();
    }
    if (ircode.value == 0xFF30CF){
        motorHreifa();
    }
}

void motorHreifa(){
    Serial.println("motor");
    while (IRKodi != 1){
        for(int i = 0; i < 180; i + 5){
            ultrasonicCheck();
            while (cm < 20 and cm != 0){
                Serial.println(cm);
                Serial.println("delay");
                delay(100);
            }
            motor_gradur = motor_gradur + 5;
            motor.write(motor_gradur);
            Serial.println(motor_gradur);
            if (ircode.value == 0xFF629D){
                IRKodi = 1;
                IRControl();
            }
        }
    }
}

void ultrasonicCheck(){
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
}

void loop(){
    IRControl();
}