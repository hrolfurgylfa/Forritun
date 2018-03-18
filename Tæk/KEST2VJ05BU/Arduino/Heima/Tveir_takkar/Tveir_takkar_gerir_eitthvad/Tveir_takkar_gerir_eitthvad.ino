#define buttonPin1 2
#define buttonPin2 3

#define LEDpin1 9
#define LEDpin2 8

int OnOff = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  pinMode(buttonPin1,INPUT);
  pinMode(buttonPin2,INPUT);

  pinMode(LEDpin1,OUTPUT);
  pinMode(LEDpin2,OUTPUT);
}
void buttonRead(int buttonPin, int LEDpin){
  OnOff = digitalRead(buttonPin);
  if (OnOff == HIGH)
  {
    Serial.print("High");
    Serial.print("\t");
    digitalWrite(LEDpin,HIGH);
  }
  else
  {
    Serial.print("Low");
    Serial.print("\t");
    digitalWrite(LEDpin,LOW);
  }
}

void loop() {
  buttonRead(buttonPin1,LEDpin1);//Button 1
  buttonRead(buttonPin2,LEDpin2);//Button 2
  
  Serial.print("\n");
}
