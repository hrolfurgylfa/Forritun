const int B_R_LED = 0;
const int B_Gu_LED = 1;
const int B_Gr_LED = 2;

const int G_R_LED = 6;
const int G_G_LED = 7;

const int Btn_1 = 8;

void setup(){
  
}

void gongu_blikk(){
  digitalWrite(G_G_LED,LOW);
  digitalWrite(G_G_LED,HIGH);
}

void loop(){
  if(digitalRead(Btn_1) == HIGH){

    //Gult hja bilunum
    digitalWrite(B_Gr_LED,LOW);
    digitalWrite(B_Gu_LED,HIGH);
    delay(1000);

    //Rautt hja bilunum
    digitalWrite(B_Gu_LED,LOW);
    digitalWrite(B_R_LED,HIGH);
    delay(1000);

    //Grænt hjá gangandi
    digitalWrite(G_R_LED,LOW);
    digitalWrite(G_G_LED,HIGH);
    delay(9000);

    gongu_blikk();
    delay(200);
    gongu_blikk();
    delay(200);
    gongu_blikk();
    delay(200);
    gongu_blikk();
    delay(200);
    gongu_blikk();
    delay(200);

    //Rautt hjá gangandi
    digitalWrite(G_G_LED,LOW);
    digitalWrite(G_R_LED,HIGH);
    delay(1000);

    //Gult hjá bílum
    digitalWrite(B_Gu_LED,HIGH);
    delay(1000);

    //Grænt hjá bílum
    digitalWrite(B_Gu_LED,LOW);
    digitalWrite(B_R_LED,LOW);
    digitalWrite(B_Gr_LED,HIGH);
    delay(10000);
  }
}
