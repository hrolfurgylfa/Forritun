const int gr1_LED = 0;
const int gu1_LED = 1;
const int r1_LED = 2;
const int gr2_LED = 3;
const int gu2_LED = 4;
const int r2_LED = 5;

void setup(){
    pinMode(0,OUTPUT);
    pinMode(1,OUTPUT);
    pinMode(2,OUTPUT);
    pinMode(3,OUTPUT);
    pinMode(4,OUTPUT);
    pinMode(5,OUTPUT);

    digitalWrite(gu1_LED,LOW);
    digitalWrite(r1_LED,HIGH);//Ljós 1 Rauð #1
    delay(1000);
    digitalWrite(gu2_LED,LOW);
    digitalWrite(r2_LED,LOW);
    digitalWrite(gr2_LED,HIGH);//Ljós 2 Græn #2
}
void loop(){
    //Ljós 1 eru gul og ljós 2 eru rauð og gul
    delay(10000);
    
    digitalWrite(gr2_LED,LOW);
    digitalWrite(gu2_LED,HIGH);//Ljós 2 Gul #3
    delay(1000);
    
    digitalWrite(gu2_LED,LOW);
    digitalWrite(r2_LED,HIGH);//Ljós 2 Rauð #4
    delay(1000);
    digitalWrite(gu1_LED,HIGH);//Ljós 1 Rauð og Gul #5
    delay(1000);
    
    digitalWrite(r1_LED,LOW);
    digitalWrite(gu1_LED,LOW);
    digitalWrite(gr1_LED,HIGH);//Ljós 1 Græn #6
    delay(10000);
    
    digitalWrite(gr1_LED,LOW);
    digitalWrite(gu1_LED,HIGH);//Ljós 1 Gul #7
    delay(1000);
    
    digitalWrite(gu1_LED,LOW);
    digitalWrite(r1_LED,HIGH);//Ljós 1 Rauð #8
    delay(1000);
    
    digitalWrite(gu2_LED,HIGH);//Ljós 2 Rauð og Gul #9
    delay(1000);
    
    digitalWrite(gu2_LED,LOW);
    digitalWrite(r2_LED,LOW);
    digitalWrite(gr2_LED,HIGH);//Ljós 2 Græn #10
}
