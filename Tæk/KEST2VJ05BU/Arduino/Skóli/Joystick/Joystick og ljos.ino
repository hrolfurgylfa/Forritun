const int xPin = A0;
const int yPin = A1;
const int buttonPin = 2;

//const int LED_1 = 3;

int xPosition = 0;
int yPosition = 0;
int buttonState = 0;

int LED = 0;
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
}

void loop() {
  xPosition = analogRead(xPin);
  yPosition = analogRead(yPin);
  buttonState = digitalRead(buttonPin);
  
    if (yPosition < 100){
        Serial.println("hægri");
        if (LED != 7){
            Serial.println("hægri0");
            if (ljosastada[LED] == 1){
                Serial.println("hægri1");
                digitalWrite(LED + 3,LOW);
                ljosastada[LED] = 0;
                LED = LED - 1;
                if (ljosastada[LED] != 2){
                    Serial.println("hægri2");
                    ljosastada[LED] = 1; // kveiki ljósið á nýja staðnum
                }
            }
            else if (ljosastada[LED] == 2){
                Serial.println("hægri3");
                LED = LED - 1;
                if (ljosastada[LED] != 2){
                    ljosastada[LED] = 1; // kveiki ljósið á nýja staðnum
                }
            }
        }
    }
    else if (yPosition > 1000){
        Serial.println("vinstri");
        if (LED != 3){
            Serial.println("vinstri0");
            if (ljosastada[LED] == 1){
                Serial.println("vinstri1");
                digitalWrite(LED + 3,LOW);
                LED = LED + 1;
                if (ljosastada[LED] != 2){
                    Serial.println("vinstri2");
                    ljosastada[LED] = 1; // kveiki ljósið á nýja staðnum
                }
            }
            else if (ljosastada[LED] == 2){
                Serial.println("vinstri3");
                LED = LED - 1;
                if (ljosastada[LED] != 2){
                    ljosastada[LED] = 1; // kveiki ljósið á nýja staðnum
                }
            }
        }
    }
    else if (buttonState == 0){
        ljosastada[LED] = 2;
    }
    for( int i = 3; i < 11; i = i + 1 ) {
        if (ljosastada[i] == 0){
            digitalWrite(i,LOW);
        }
        else {
            digitalWrite(i,HIGH);
        }
    }
}
