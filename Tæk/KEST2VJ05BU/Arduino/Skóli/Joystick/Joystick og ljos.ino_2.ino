const int xPin = A0;
const int yPin = A1;
const int buttonPin = 2;

//const int LED_1 = 3;

int xPosition = 0;
int yPosition = 0;
int buttonState = 0;

int bida = 0;
int Stadsetning = 0;
int ljosastada[] = {1,0,0,0,0,0,0,0};

void setup() {
    // initialize serial communications at 9600 bps:
    for (int x = 2; x < 11; x++){
        pinMode(x,OUTPUT);
    }
    Serial.begin(9600); 
  
    pinMode(xPin, INPUT);
    pinMode(yPin, INPUT);

    //activate pull-up resistor on the push-button pin
    pinMode(buttonPin, INPUT_PULLUP); 
  
    // For versions prior to Arduino 1.0.1
    // pinMode(buttonPin, INPUT);
    // digitalWrite(buttonPin, HIGH);
    Serial.println("setup buid");//TEST
}
void hreifa(int att){
    bida = 1;
    Serial.println("hreifa");//TEST
    if (ljosastada[Stadsetning] == 1){
        ljosastada[Stadsetning] = 0;
    }
    if (att == 0){
        Stadsetning++;
        Serial.println("plusad");//TEST
    }
    else {
        Stadsetning--;
        Serial.println("minusad");//TEST
    }
    Serial.println("Stadsetning faerd");//TEST
    if (ljosastada[Stadsetning] == 0){
        ljosastada[Stadsetning] = 1;
    }
}
void loop() {
    Serial.println("loop byrjað");//TEST
    xPosition = analogRead(xPin);
    yPosition = analogRead(yPin);
    Serial.println(xPosition);//TEST
    buttonState = digitalRead(buttonPin);
    if (xPosition < 100 and Stadsetning != 0){
        hreifa(1);
    }
    else if (xPosition > 850 and Stadsetning != 7){
        hreifa(0);
    }
    else if (buttonState == 0){
        bida = 1;
        if (ljosastada[Stadsetning] == 1){
            ljosastada[Stadsetning] = 2;
        }
        else {
            ljosastada[Stadsetning] = 1;
        }
    }

    for (int x = 0; x < 8; x++){
        if (ljosastada[x] == 0){
            digitalWrite(x+3,LOW);
        }
        else if (ljosastada[x] == 1){
            digitalWrite(x+3,HIGH);
        }
        else if (ljosastada[x] == 2){
            digitalWrite(x+3,HIGH);
        }
    }
    if (bida == 1){
        delay(500);
        bida = 0;
    }
}