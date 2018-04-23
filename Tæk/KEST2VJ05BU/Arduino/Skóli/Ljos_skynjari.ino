const int r_LED = 11;
const int g_LED = 10;
const int b_LED = 9;
const int btn = 12;
const int ljos_skynjari = A5;

int skynjariValue;
int rgb = 0;

void setup(){
    pinMode(r_LED,OUTPUT);
    pinMode(g_LED,OUTPUT);
    pinMode(b_LED,OUTPUT);
    pinMode(btn,INPUT);
}



void loop(){
    skynjariValue = analogRead(ljos_skynjari);
    skynjariValue = map(skynjariValue, 0, 1023, 0, 255);
    if (digitalRead(btn) == HIGH){
        if (rgb == 2){
            rgb = 0;
        }
        else{
            rgb = rgb + 1;
        }
    }
    if (rgb == 0){
        digitalWrite(r_LED, skynjariValue);
        digitalWrite(g_LED, LOW);
        digitalWrite(b_LED, LOW);
    }
    if (rgb == 1){
        digitalWrite(r_LED, LOW);
        digitalWrite(g_LED, skynjariValue);
        digitalWrite(b_LED, LOW);
    }
    if (rgb == 2){
        digitalWrite(r_LED, LOW);
        digitalWrite(g_LED, LOW);
        digitalWrite(b_LED, skynjariValue);
    }
}
