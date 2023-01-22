#define blu 9
#define gre 8
String cod;

void setup() 
{
  Serial.begin(9600);
  pinMode(blu,OUTPUT);
  pinMode(gre,OUTPUT);
}

void loop() 
{

  while(Serial.available())
  {
    delay(10);
    char aux = Serial.read();
    cod += aux; 
  }

  switch(cod) 
  {
    
    case "azulLIG":
      digitalWrite(blu,1);
      cod = "";    
      break;
    
    case "azulDES":
      digitalWrite(blu,0);
      cod = "";    
      break;
    
    case "verdeLIG":
      digitalWrite(gre,1);
      cod = "";    
      break;

    case "verdeDES":
      digitalWrite(gre,0);
      cod = "";    
      break;
    
    default:
      cod = "";
  }

  delay(15);
}
