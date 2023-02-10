int HALL_SEN_ANALOG_PIN = A0;
int HALL_SEN_ANALOG_PIN2 = A1;
int TOUCHindex = A3;
int TOUCHmiddle = A4;
int TOUCHring = A5;
int value = 0;
int value2 = 0;
int val = 0;
int val2 = 0;
int valtouchindex = 0;
int valtouchmiddle = 0;
int valtouchring = 0;
int thing;
int inverse_valtouchindex;
int inverse_valtouchmiddle;
int inverse_valtouchring;
void setup() {
  Serial.begin(9600);
  pinMode(22, INPUT_PULLUP );
  pinMode(24, INPUT_PULLUP );
  pinMode(26, INPUT_PULLUP );
}

int inverse_num(int thing)
{
    if (thing == 0){
      thing = 2;
    }
    else{
      thing = 1;
    }
    return thing;
}

void loop()
{
  int valtouchindex;
  int valtouchmiddle;
  int valtouchring;
  valtouchindex = (digitalRead(22));
  valtouchmiddle = (digitalRead(24));
  valtouchring = (digitalRead(26));
  inverse_valtouchindex = inverse_num(valtouchindex);
  inverse_valtouchmiddle = inverse_num(valtouchmiddle);
  inverse_valtouchring = inverse_num(valtouchring);
  value = analogRead(HALL_SEN_ANALOG_PIN);
  if (value > 360)
  {
    val = 2;
  }
  else
  {
    val = 1;
  }
  
  value2 = analogRead(HALL_SEN_ANALOG_PIN2);
  if (value2 > 350)
  {
    val2 = 2;
  }
  else
  {
    val2 = 1;
  }
  

  Serial.print(val);
  Serial.print(val2);
  Serial.print(inverse_valtouchindex);
  Serial.print(inverse_valtouchmiddle);
  Serial.println(inverse_valtouchring);
  delay(40);
}
