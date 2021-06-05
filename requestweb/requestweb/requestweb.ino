#include <WiFi.h>
#include <WiFiClient.h>
#include <HTTPClient.h>
#include <LiquidCrystal_I2C.h>

#define WIFISSID "Ahlan Wa Sahlan"
#define PASSWORD "jazakumullahu_Kha1ran"

#define LEDid 4
#define LEDod 2
#define LEDtest 12
#define lamPu1 17
#define lamPu2 5
#define lamPu3 18
#define lamPu4 19

LiquidCrystal_I2C lcd(0x27, 16, 2);
WiFiClient client;

const char* host = "192.168.1.64";
const int httpPort = 80;
String url;
String request_string;

void setup(){
  Serial.begin(9600); // Starts the serial communication
  lcd.begin();
  pinMode (LEDid, OUTPUT);
  pinMode (LEDod, OUTPUT);
  pinMode (LEDtest, OUTPUT);
  pinMode (lamPu1, OUTPUT);
  pinMode (lamPu2, OUTPUT);
  pinMode (lamPu3, OUTPUT);
  pinMode (lamPu4, OUTPUT);
  WiFi.begin(WIFISSID, PASSWORD);
  lcd.setCursor(0,0);
  lcd.println("WiFi Connecting.");
  lcd.setCursor(0,1);
  lcd.println(String(WIFISSID) + "    ");
    //cek
    while(WiFi.status() != WL_CONNECTED){
      Serial.println(".");
      digitalWrite(LEDid, LOW);
      delay(500);
      digitalWrite(LEDid, HIGH);
      delay(500);
    }
    lcd.setCursor(0,0);
    lcd.println("Connected...!   ");
    Serial.println("Connected");
    delay(1800);
    digitalWrite(LEDid, HIGH);

}

void loop (){
    lcd.setCursor(0,0);
    lcd.print("request from....");
    Serial.print("request from...");
    Serial.println(host);
    lcd.setCursor(0,1);
    lcd.println("==" + String(host) + "==");
    delay(500);
   
    WiFiClient client;
    if (!client.connect(host, httpPort)) {
      lcd.setCursor(0,0);
      lcd.println("Info = !        ");
      lcd.setCursor(0,1);
      Serial.println("connection fail ");
      lcd.println("connection fail ");
      delay(2000);
      return;
    }

    const char* Link[4];
    Link[0]="/Behavior/readData/readData1.php";
    Link[1]="/Behavior/readData/readData2.php";
    Link[2]="/Behavior/readData/readData3.php";
    Link[3]="/Behavior/readData/readData4.php";
    
    HTTPClient http;
    for(int i=0; i<4; i++){
      http.begin("http://"+ String(host) + String(Link[i]));
      http.GET();
      String respon = http.getString();
      lcd.setCursor(0,0);
      lcd.println(respon + "#       ");
      Serial.println(respon + "]");
      delay(500);
    
    char responAngka[65];
    respon.toCharArray(responAngka,65);
    digitalWrite(LEDod, LOW);
    delay(100);
    digitalWrite(LEDod, HIGH);
    delay(100);   
    digitalWrite(LEDod, LOW);
    delay(100);
    digitalWrite(LEDod, HIGH);
    delay(100);
    digitalWrite(LEDod, LOW);
    delay(100); 
    digitalWrite(LEDod, HIGH);
    Serial.println("=================Last Data...=================");
    if (responAngka[7]=='1' && responAngka[14]=='0'){
      digitalWrite(lamPu1,HIGH);
      lcd.setCursor(0,1);
      lcd.println(" =Relay 1 Mati=  ");
      Serial.println("Relay 1 Mati");
    }
    else if (responAngka[7]=='1' && responAngka[14]=='1'){
      digitalWrite(lamPu1,LOW);
      lcd.setCursor(0,1);
      lcd.println("=Relay 1  Hidup=  ");
      Serial.println("Relay 1 Hidup");
    }
    else if (responAngka[7]=='2' && responAngka[14]=='0'){
      digitalWrite(lamPu2,HIGH);
      lcd.setCursor(0,1);
      lcd.println(" =Relay 2 Mati=  ");
      Serial.println("Relay 2 Mati");
    }
    else if (responAngka[7]=='2' && responAngka[14]=='1'){
      digitalWrite(lamPu2,LOW);
      lcd.setCursor(0,1);
      lcd.println("=Relay 2  Hidup=  ");
      Serial.println("Relay 2 Hidup");
    }
    else if (responAngka[7]=='3' && responAngka[14]=='0'){
      digitalWrite(lamPu3,HIGH);
      lcd.setCursor(0,1);
      lcd.println(" =Relay 3 Mati=  ");
      Serial.println("Relay 3 Mati");
    }
    else if (responAngka[7]=='3' && responAngka[14]=='1'){
      digitalWrite(lamPu3,LOW);
      lcd.setCursor(0,1);
      lcd.println("=Relay 3  Hidup=  ");
      Serial.println("Relay 3 Hidup");
    }
    else if (responAngka[7]=='4' && responAngka[14]=='0'){
      digitalWrite(lamPu4,HIGH);
      lcd.setCursor(0,1);
      lcd.println(" =Relay 4 Mati=  ");
      Serial.println("Relay 4 Mati");
    }
    else if (responAngka[7]=='4' && responAngka[14]=='1'){
      digitalWrite(lamPu4,LOW);
      lcd.setCursor(0,1);
      lcd.println("=Relay 4  Hidup=  ");
      Serial.println("Relay 4 Hidup");
    }
    lcd.setCursor(0,0);
    lcd.println(">----<LOGs>----<");
    Serial.println("=====================LOGs=====================");
    delay(500);
    }
}
