#include <Servo.h> // Sambærilegt og import í python
#include <IRremote.h>//Það þarf library sem heitir IRRemote og er búið til af shirriff

//IR
#define IR_PIN 10
IRrecv irrecv(IR_PIN);
decode_results ircode;

//ultrasonic sensor
const int TrigPin = 4;//Trig attach to pin2
const int EchoPin = 5;//Echo attach to pin3
float cm; // fjöldi cm sem mældir eru

//Servo motor
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
    irrecv.enableIRIn();//Fyrir IR
}

void fall_motor_vinstri(){
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

    if (att_upp == 1){
        if (cm < 20 and cm != 0){
            while (cm < 20 and cm != 0){
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
                Serial.println(cm);
                Serial.println("delay");
                delay(100);
            }
        }
        motor_gradur = motor_gradur + 5;

        motor.write(motor_gradur);

        Serial.println(motor_gradur);

        if (motor_gradur > 180){
            att_upp == 0;
            Serial.println("Snúa við");
        }

    }
}
void fall_motor_haegri(){
    if (cm < 20 and cm != 0){
        while (cm < 20 and cm != 0){
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
            Serial.println(cm);
            Serial.println("delay");
            delay(100);
        }
    }
    motor_gradur = motor_gradur - 5;
    motor.write(motor_gradur);

    Serial.println(motor_gradur);
}

void IR_1(){
    if (irrecv.decode(&ircode)){
        Serial.println(ircode.value,HEX);
        if (ircode.value == 0xFF629D){
            Serial.println("virkar");
        }
        irrecv.resume();
    }
}

void loop(){
    for (int x = 0; x > 51;x++){
        IR_1();
        delay(5);
    }
    fall_motor_vinstri();
}