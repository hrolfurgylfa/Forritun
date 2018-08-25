/*
Random Teningur
Hrólfur Gylfason
12/06/2018
*/
const int led_1 = 2;
const int led_2 = 3;
const int led_3 = 4;
const int led_4 = 5;
const int led_5 = 6;
const int led_6 = 7;

const int Btn = 12;

int random_hlid = 0;

void setup() {
    Serial.begin(9600);

    pinMode(led_1,OUTPUT);
    pinMode(led_2,OUTPUT);
    pinMode(led_3,OUTPUT);
    pinMode(led_4,OUTPUT);
    pinMode(led_5,OUTPUT);
    pinMode(led_6,OUTPUT);
    pinMode(Btn,INPUT);
    randomSeed(analogRead(A0));
}

void loop() {
    if (digitalRead(Btn) == HIGH){
        for (int x = 2; x < 8; x++){
            digitalWrite(x,LOW);
        }
        random_hlid = random(2,8);
        digitalWrite(random_hlid,HIGH);
        delay(500);
    }

}
