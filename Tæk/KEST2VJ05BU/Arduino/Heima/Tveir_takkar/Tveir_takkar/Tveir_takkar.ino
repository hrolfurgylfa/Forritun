#define buttonPin1 2
#define buttonPin2 3

int OnOff = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  pinMode(buttonPin1,INPUT);
  pinMode(buttonPin2,INPUT);
}
void buttonRead(int pin){
  OnOff = digitalRead(pin);
  if (OnOff == HIGH)
  {
    Serial.print("High");
    Serial.print("\t");
  }
  else
  {
    Serial.print("Low");
    Serial.print("\t");
  }
}

void loop() {
  buttonRead(buttonPin1);//Button 1
  buttonRead(buttonPin2);//Button 2
  
  Serial.print("\n");
}
