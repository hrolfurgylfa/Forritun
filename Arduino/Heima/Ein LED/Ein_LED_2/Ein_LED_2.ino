#define dpin 7

void setup() {
    pinMode(dpin, OUTPUT);
}

void blink(int on, int off) {
  digitalWrite(dpin, HIGH);
  delay(on);

  digitalWrite(dpin, LOW);
  delay(off);
}

void loop() {
    blink(2000, 500);
}
