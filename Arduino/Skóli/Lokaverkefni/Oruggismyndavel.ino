#include <Servo.h> // Sambærilegt og import í python

//Takkar
int Btn1 = 13;
int Btn2 = 12;
int Btn3 = 11;

//ultrasonic sensor
const int TrigPin = 4;//Trig attach to pin2
const int EchoPin = 5;//Echo attach to pin3
float cm; // fjöldi cm sem mældir eru

//Servo motor
Servo motor; // bý til tilvik af Servo klasanum
int motor_pinni = 9; // pinninn sem ég nota til að stjórna mótornum
int att_upp = 1;
int motor_gradur = 0;
int x = 0;
int skila_strengur = 0;

//LED
int LED_1 = 7;

void setup(){
    Serial.begin(9600); //Sets the data rate in bits per second (baud) for serial data transmission
    //set the below pins as OUTPUT
    pinMode(TrigPin,OUTPUT);
    pinMode(EchoPin,INPUT);
    motor.attach(motor_pinni); // segi servo tilvikinu hvaða pinna á að nota
    //Fyrir takka
    pinMode(Btn1,INPUT);
    pinMode(Btn2,INPUT);
    pinMode(Btn3,INPUT);
    pinMode(LED_1,OUTPUT);
}

void lengdarskynjari(){
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

void bida(){
    lengdarskynjari();
    while (cm < 20 and cm != 0){
        lengdarskynjari();
        Serial.println(cm);
        Serial.println("delay");
        digitalWrite(LED_1,HIGH);
        delay(100);
    }
    digitalWrite(LED_1,LOW);
}

void hreifa_motor(){
    for (x = 0; x < 180; x = x + 15 ){
        bida();
        motor.write(x);
        Serial.println(x);
        if (digitalRead(Btn2) == HIGH){
            delay(100);
            Serial.println("\tHætta");
            skila_strengur = 1;
            break;
        }
        delay(50);
    }
}

void manual(){
    while (analogRead(A0) != 9999999999999){
        Serial.println(digitalRead(Btn1));
        Serial.print("\t");
        Serial.print(digitalRead(Btn2));
        Serial.print("\t");
        Serial.print(digitalRead(Btn3));
        Serial.print("\n");
        bida();
        if (digitalRead(Btn1) == HIGH){
            x = x + 15;
            if (x > 0){
                motor.write(x);
            }
            Serial.println(x);
        }
        else if (digitalRead(Btn3) == HIGH){
            x = x - 15;
            if (x < 180){
                motor.write(x);
            }
            Serial.println(x);
        }
        if (digitalRead(Btn2) == HIGH){
            break;
        }
        delay(100);
    }
}

void loop(){
    hreifa_motor();
    Serial.println(skila_strengur);
    if (skila_strengur == 1){
        skila_strengur = 0;
        manual();
    }
    delay(50);
    Serial.println("loop fall búið");
}
