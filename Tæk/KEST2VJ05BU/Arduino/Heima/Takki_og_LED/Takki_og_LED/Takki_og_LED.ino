int switchPin = 12;
int ledPin = 13;

void setup() {
  Serial.begin(9600);
  pinMode(switchPin,INPUT);
  pinMode(ledPin,OUTPUT);
}

void loop() {
  Serial.println(digitalRead(switchPin));
  if (digitalRead(switchPin) == HIGH){
    digitalWrite(ledPin, HIGH);
  }
  else{
    digitalWrite(ledPin, LOW);
  }
  delay(5);
}
