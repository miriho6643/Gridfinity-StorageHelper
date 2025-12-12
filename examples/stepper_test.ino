#include <Arduino.h>
const int STEP_PIN = 3;
const int DIR_PIN = 4;
void setup() {
  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIR_PIN, OUTPUT);
} 
void loop() {
  digitalWrite(DIR_PIN, HIGH);
  for(int i=0;i<200;i++){
    digitalWrite(STEP_PIN,HIGH);
    delayMicroseconds(800);
    digitalWrite(STEP_PIN,LOW);
    delayMicroseconds(800);
  }
  delay(1000);
  digitalWrite(DIR_PIN,LOW);
  for(int i=0;i<200;i++){
    digitalWrite(STEP_PIN,HIGH);
    delayMicroseconds(800);
    digitalWrite(STEP_PIN,LOW);
    delayMicroseconds(800);
  }
  delay(1000);
}
