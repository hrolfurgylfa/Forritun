/*
Led_klukka_0-255
Hrólfur Gylfason
21/03/2018
*/
const int led_1 = 4;
const int led_2 = 5;
const int led_3 = 6;
const int led_4 = 7;

const int led_5 = 8;
const int led_6 = 9;
const int led_7 = 10;
const int led_8 = 11;

int teljari = 0;

void setup() {
  pinMode(led_1,OUTPUT);
  pinMode(led_2,OUTPUT);
  pinMode(led_3,OUTPUT);
  pinMode(led_4,OUTPUT);

  pinMode(led_5,OUTPUT);
  pinMode(led_6,OUTPUT);
  pinMode(led_7,OUTPUT);
  pinMode(led_8,OUTPUT);

  Serial.begin(9600);
}

void loop() {
  digitalWrite(led_1,(teljari) % 2);
  digitalWrite(led_2,(teljari/2) % 2);
  digitalWrite(led_3,(teljari/4) % 2);
  digitalWrite(led_4,(teljari/8) % 2);

  digitalWrite(led_5,(teljari/16) % 2);
  digitalWrite(led_6,(teljari/32) % 2);
  digitalWrite(led_7,(teljari/64) % 2);
  digitalWrite(led_8,(teljari/128) % 2);

  Serial.println(teljari);

  teljari++;
  delay(500);
}
