#define dpin 7
#define wait 1000

void setup() {
    pinMode(dpin, OUTPUT);
}
void loop() {
    digitalWrite(dpin, HIGH);

    delay(wait);

    digitalWrite(dpin, LOW);

    delay(wait);
}
