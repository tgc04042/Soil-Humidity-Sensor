/**
*file : deveopment sensor test source code
*author : YoungJu Jeong
*e-mail : vertex50@cu.ac.kr
*/
const int SEN0114 = A0;
const int Chopsticks = A1;
const int VacuumChopsticks = A2;
const int Copper = A3;
const int Stainless = A4;
const int FC_28 = A5;
int num;

void setup(){
  num = 0;
  pinMode(SEN0114, INPUT);
  pinMode(Chopsticks, INPUT);
  pinMode(VacuumChopsticks, INPUT);
  pinMode(Copper, INPUT);
  pinMode(Stainless, INPUT);
  pinMode(FC_28, INPUT);
  Serial.begin(9600);
}

void loop(){
  int value0 = analogRead(SEN0114);
  Serial.print("SEN0114 : ");
  Serial.println(value0);
  int value1 = analogRead(Chopsticks);
  Serial.print("Chopsticks : ");
  Serial.println(value1);
  int value2 = analogRead(VacuumChopsticks);
  Serial.print("VacuumChopsticks : ");
  Serial.println(value2);
 // int value3 = analogRead(Copper);
 // Serial.print("Copper : ");
 // Serial.println(Copper);
  int value4 = analogRead(Stainless);
  Serial.print("Stainless : ");
  Serial.println(value4);
  int value5 = analogRead(FC_28);
  Serial.print("FC_28 : ");
  value5 = 1023-value5;
  Serial.println(value5);
  delay(1000);
  num++;
  Serial.print("------num is : ");
  Serial.println(num);
}
