const int TrigPin = 4;//Trig attach to pin2
const int EchoPin = 5;//Echo attach to pin3
float cm; // fjöldi cm sem mældir eru

void setup(){
   Serial.begin(9600); //Sets the data rate in bits per second (baud) for serial data transmission
   //set the below pins as OUTPUT
   pinMode(TrigPin,OUTPUT);
   pinMode(EchoPin,INPUT);
}

void loop(){
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
  Serial.println(cm);
}