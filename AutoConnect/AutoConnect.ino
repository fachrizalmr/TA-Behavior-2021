#include <LiquidCrystal.h>
#include <Wire.h>
#include <ESP8266WiFi.h>
#include <DNSServer.h>
#include <ESP8266WebServer.h>
#include <WiFiManager.h>
#include <LiquidCrystal_I2C.h>
#include <FirebaseArduino.h>

#define FIREBASE_HOST "cloudta2021-fa4af-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "6fOAEv0SJgisAV9tjJZNR1IaAo9G1HxCRRdcY3Hs"

#define ledConnection 0
#define ledData 2
#define relay1 14
#define relay2 12
#define relay3 13
#define relay4 3

String modes;
String relayStatus1;
String relayStatus2;
String relayStatus3;
String relayStatus4;
float akurasi = 0;
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(115200);
  lcd.begin();
  pinMode (ledConnection, OUTPUT);
  pinMode (ledData, OUTPUT);
  pinMode (relay1, OUTPUT);
  pinMode (relay2, OUTPUT);
  pinMode (relay3, OUTPUT);
  pinMode (relay4, OUTPUT);
  lcd.setCursor(0, 0);
  lcd.print("Try to Connect: ");
  lcd.setCursor(0, 1);
  lcd.print("SSID:Relay4Channel");
  delay(100);
  WiFiManager wifiManager;
  wifiManager.autoConnect("Relay4Channel");
  Serial.println("connected...yeey :)");
  digitalWrite(ledConnection, HIGH);
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Serial.println("connect with Firebase");
  lcd.setCursor(0, 0);
  lcd.println("Firebase Cloud...");
  lcd.setCursor(0, 1);
  lcd.println("Relay 4 Channel   ");
  delay(1000);
  digitalWrite(ledData, HIGH);
}

String getStringPartByNr(String data, char separator, int index)
{
  int stringData = 0;
  String dataPart = "";
  for (int i = 0; i < data.length() - 1; i++) {
    if (data[i] == separator) {
      stringData++;
    } else if (stringData == index) {
      //get the text when separator is the rignt one
      dataPart.concat(data[i]);
    } else if (stringData > index) {
      return dataPart;
      break;
    }
  }
  return dataPart;
}

String p = " | ";
void loop() {
  modes = Firebase.getString("/Relay4Channel/mode/set");
  String newModes = getStringPartByNr(modes, '"', 1);
  Serial.println(newModes);
  if (newModes == "behavior") {
    akurasi = Firebase.getFloat("/Relay4Channel/behavior/akurasi");
    relayStatus1 = Firebase.getString("/Relay4Channel/behavior/relay1/status");
    relayStatus2 = Firebase.getString("/Relay4Channel/behavior/relay2/status");
    relayStatus3 = Firebase.getString("/Relay4Channel/behavior/relay3/status");
    relayStatus4 = Firebase.getString("/Relay4Channel/behavior/relay4/status");

    if (relayStatus1 == "ON") {
      digitalWrite(relay1, LOW);
    }
    if (relayStatus1 == "OFF") {
      digitalWrite(relay1, HIGH);
    }
    if (relayStatus2 == "ON") {
      digitalWrite(relay2, LOW);
    }
    if (relayStatus2 == "OFF") {
      digitalWrite(relay2, HIGH);
    }
    if (relayStatus3 == "ON") {
      digitalWrite(relay3, LOW);
    }
    if (relayStatus3 == "OFF") {
      digitalWrite(relay3, HIGH);
    }
    if (relayStatus4 == "ON") {
      digitalWrite(relay4, LOW);
    }
    if (relayStatus4 == "OFF") {
      digitalWrite(relay4, HIGH);
    }
    lcd.setCursor(0, 0);
    lcd.print("Mode : " + newModes + "   ");
    lcd.setCursor(0, 1);
    lcd.print("Akurasi : ");
    lcd.setCursor(11, 1);
    lcd.print(akurasi);
    delay(1000);
    lcd.setCursor(0, 0);
    lcd.print("R1: " + relayStatus1 + " R2: " + relayStatus2 + "  ");
    lcd.setCursor(0, 1);
    lcd.print("R3: " + relayStatus3 + " R4: " + relayStatus4 + "  ");
    delay(500);
    digitalWrite(ledData, HIGH);
    delay(150);
    digitalWrite(ledData, LOW);
    delay(150);
    digitalWrite(ledData, HIGH);
    delay(150);
    digitalWrite(ledData, LOW);
    delay(150);
    Serial.println(akurasi + p + relayStatus1 + p + relayStatus2 + p + relayStatus3 + p + relayStatus4);
  } else {
    modes = Firebase.getString("/Relay4Channel/mode/set");
    String newModes = getStringPartByNr(modes, '"', 1);
    relayStatus1 = Firebase.getString("/Relay4Channel/manual/relay1/status");
    relayStatus2 = Firebase.getString("/Relay4Channel/manual/relay2/status");
    relayStatus3 = Firebase.getString("/Relay4Channel/manual/relay3/status");
    relayStatus4 = Firebase.getString("/Relay4Channel/manual/relay4/status");
    String rStatus1 = getStringPartByNr(relayStatus1, '"', 1);
    String rStatus2 = getStringPartByNr(relayStatus2, '"', 1);
    String rStatus3 = getStringPartByNr(relayStatus3, '"', 1);
    String rStatus4 = getStringPartByNr(relayStatus4, '"', 1);

    if (rStatus1 == "ON") {
      digitalWrite(relay1, LOW);
    }
    if (rStatus1 == "OFF") {
      digitalWrite(relay1, HIGH);
    }
    if (rStatus2 == "ON") {
      digitalWrite(relay2, LOW);
    }
    if (rStatus2 == "OFF") {
      digitalWrite(relay2, HIGH);
    }
    if (rStatus3 == "ON") {
      digitalWrite(relay3, LOW);
    }
    if (rStatus3 == "OFF") {
      digitalWrite(relay3, HIGH);
    }
    if (rStatus4 == "ON") {
      digitalWrite(relay4, LOW);
    }
    if (rStatus4 == "OFF") {
      digitalWrite(relay4, HIGH);
    }
    lcd.setCursor(0, 0);
    lcd.print("Mode : " + newModes + "     ");
    lcd.setCursor(0, 1);
    lcd.print("Manual Control    ");
    delay(1000);
    lcd.setCursor(0, 0);
    lcd.print("R1: " + rStatus1 + " R2: " + rStatus2 + "  ");
    lcd.setCursor(0, 1);
    lcd.print("R3: " + rStatus3 + " R4: " + rStatus4 + "  ");
    delay(500);
    digitalWrite(ledData, HIGH);
    delay(150);
    digitalWrite(ledData, LOW);
    delay(150);
    digitalWrite(ledData, HIGH);
    delay(150);
    digitalWrite(ledData, LOW);
    delay(150);
    Serial.println(rStatus1 + p + rStatus2 + p + rStatus3 + p + rStatus4);
  }
}
