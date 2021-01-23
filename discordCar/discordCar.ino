// Multiple tests are required to retrieve the mathematical equations for the rotation.

#define enA 8
#define enB 9
#define en1 2
#define en2 3
#define en3 4
#define en4 5

int defaultSpeed = 100;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(15);
  pinMode(en1, OUTPUT);
  pinMode(en2, OUTPUT);
  pinMode(en3, OUTPUT);
  pinMode(en4, OUTPUT);
  digitalWrite(en1, HIGH);
  digitalWrite(en2, LOW);
  digitalWrite(en3, HIGH);
  digitalWrite(en4, LOW);
  analogWrite(enA, 0);
  analogWrite(enB, 0);
}

void loop() {
  if (Serial.available() > 0) {
    String text = Serial.readString();
    if (text.startsWith("t")) {
      text.remove(0, 1);
      int deg = text.substring(0, text.indexOf("|")).toInt();
      char d = text.substring(text.indexOf("|") + 1);
      if (d == 'l') {
        digitalWrite(en1, HIGH);
        digitalWrite(en2, LOW);
        digitalWrite(en3, LOW);
        digitalWrite(en4, HIGH);
      } else {
        digitalWrite(en1, LOW);
        digitalWrite(en2, HIGH);
        digitalWrite(en3, HIGH);
        digitalWrite(en4, LOW);
      }
      analogWrite(enA, defaultSpeed);
      analogWrite(enB, defaultSpeed);
      delay(deg);
      analogWrite(enA, 0);
      analogWrite(enB, 0);
    } 
    if (text.startsWith("m")) {
      text.remove(0, 1);
      int ms = text.substring(0, text.indexOf("|")).toInt();
      char d = text.substring(text.indexOf("|") + 1);
      if (d == 'f') {
        digitalWrite(en1, LOW);
        digitalWrite(en2, HIGH);
        digitalWrite(en3, LOW);
        digitalWrite(en4, HIGH);
      } else {
        digitalWrite(en1, HIGH);
        digitalWrite(en2, LOW);
        digitalWrite(en3, HIGH);
        digitalWrite(en4, LOW);
      }
      analogWrite(enA, defaultSpeed);
      analogWrite(enB, defaultSpeed);
      delay(ms);
      analogWrite(enA, 0);
      analogWrite(enB, 0);
    }
    //Commands for other discord to arduino functions
    // if (text.startsWith("r")) {
    //   lcd.clear();
    //   text.remove(0, 1);
    //   if (text.length() > 16) {
    //     String initText = text.substring(0, 16);
    //     String subText = text.substring(16);
    //     lcd.setCursor(0, 0);
    //     lcd.print(initText);
    //     lcd.setCursor(0, 1);
    //     lcd.print(subText);
    //   } else {
    //     lcd.print(text);
    //   }
    // } 
    // if (text.startsWith("w")) {
    //   text.remove(0, 1);
    //   String axis = text.substring(0, 1);
    //   int deg = text.substring(1).toInt();
    //   if (axis == "y") {
    //     y_servo.write(deg);
    //   }
    // }
    delay(1000);
  }

}