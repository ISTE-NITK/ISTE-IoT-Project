void setup() {
pinMode(3,INPUT_PULLUP);
pinMode(7,OUTPUT);
Serial.begin(9600);

}
int c,d;

void loop() {

  if (Serial.read()=='s')
  {
   while(1)
   {
     c=digitalRead(3);
     d=!c;
     Serial.println(c,DEC); //prints c in ASCII encoded decimal form 
     Serial.println('\n');  //does serial.print automatically send it to python code? 
     digitalWrite(7,d);
   }
  }

}
