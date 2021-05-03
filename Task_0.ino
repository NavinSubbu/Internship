void setup() {
  pinMode(A0, INPUT); //Pin declaration for 5.5v to 3.3v 
  pinMode(A1, INPUT); //Pin declaration for 3.3v to 1v 
  pinMode(8,INPUT_PULLUP); //Pin declared as Input pullup for button
  Serial.begin(9600);
}

void loop() {
  int but = digitalRead(8); // read button status
  if( but == LOW) // if pressed run below code
  {
  int x = analogRead(A0);
  Serial.print(x);
  Serial.print(","); // value seperation comma
  int y = analogRead(A1);
  Serial.println(y);
  }
  delay(500);  
}
