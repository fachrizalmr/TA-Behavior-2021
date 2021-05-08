#include <RTClib.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266HTTPClient.h>

#define LEDid 16
#define LEDod 10
#define LEDmode 0
#define PUSH1 14
#define PUSH2 12
#define PUSH3 13
#define PUSH4 15
#define PUSH5 2

int buttonState1 = 0;
int buttonState2 = 0;
int buttonState3 = 0;
int buttonState4 = 0;
int buttonState5 = 0;

#define WIFISSID "Ahlan Wa Sahlan"
#define PASSWORD "jazakumullahu_Kha1ran"
#define HOST "192.168.1.64"

RTC_DS3231 rtc;

int action;
int idlampu;
String profile;
String waktu;
int lampS;
char dataHari[7][12] = {"7", "1", "2", "3", "4", "5", "6"};
String hari;
int tanggal, bulan, tahun, jam, menit, detik;

void setup()
{
  Serial.begin(9600); // Starts the serial communication
  pinMode(LEDid, OUTPUT);
  pinMode(LEDod, OUTPUT);
  pinMode(LEDmode, OUTPUT);
  pinMode(PUSH1, INPUT);
  pinMode(PUSH2, INPUT);
  pinMode(PUSH3, INPUT);
  pinMode(PUSH4, INPUT);
  pinMode(PUSH5, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  WiFi.begin(WIFISSID, PASSWORD);
  //cek
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.println(".");
    digitalWrite(LEDid, LOW);
    delay(500);
    digitalWrite(LEDid, HIGH);
    delay(500);
  }
  Serial.println("Connected");
  digitalWrite(LEDid, HIGH);

  if (!rtc.begin())
  {
    Serial.println("RTC Tidak Ditemukan");
    Serial.flush();
    abort();
  }

  //Atur Waktu
  rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
  rtc.adjust(DateTime(2021, 5, 8, 10, 23, 0));
}

void loadData()
{
  DateTime now = rtc.now();
  hari = dataHari[now.dayOfTheWeek()];
  tanggal = now.day(), DEC;
  bulan = now.month(), DEC;
  tahun = now.year(), DEC;
  jam = now.hour(), DEC;
  menit = now.minute(), DEC;
  detik = now.second(), DEC;

  waktu = String() + jam + ":" + menit + ":" + detik;

  WiFiClient client;
  int httpPort = 80;
  if (!client.connect(HOST, httpPort))
  {
    Serial.println("Connection Failed");
    digitalWrite(LED_BUILTIN, HIGH);
    delay(500);
    digitalWrite(LED_BUILTIN, LOW);
    delay(500);
  }
  digitalWrite(LED_BUILTIN, HIGH);

  Serial.println("Waktu : " + String(waktu));
  Serial.println("Hari : " + String(hari));
  Serial.println("ID Lampu : " + String(idlampu));
  Serial.println("Status : " + String(lampS));

  String Link;
  HTTPClient http;

  Link = "http://" + String(HOST) + "/Behavior/loadData.php?&waktu=" + String(waktu) + "&hari=" + String(hari) + "&idlampu=" + String(idlampu) + "&status=" + String(lampS);
  http.begin(Link);
  http.GET();

  String respon = http.getString();
  Serial.println("====================" + respon + "====================");
  digitalWrite(LED_BUILTIN, HIGH);
  delay(250);
  digitalWrite(LED_BUILTIN, LOW);
  delay(250);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(250);
  digitalWrite(LED_BUILTIN, LOW);
  delay(250);
  http.end();
  delay(1000);
  digitalWrite(LEDod, HIGH);
  delay(100);
  digitalWrite(LEDod, LOW);
  delay(100);
  digitalWrite(LEDod, HIGH);
  delay(100);
  digitalWrite(LEDod, LOW);
  delay(100);
  return;
}

void loop()
{
  if (digitalRead(PUSH5) == 1 && buttonState5 == 0)
  {
    buttonState5 = 1;
    action = 1;
    Serial.println("Mode Behavior Aktif");
    String Link;
    HTTPClient http;
    Link = "http://" + String(HOST) + "/Behavior/loadMode.php?&action=" + String(action);
    http.begin(Link);
    http.GET();
    digitalWrite(LEDmode, HIGH);
    String respon = http.getString();
    Serial.println("====================" + respon + "====================");
    http.end();
    delay(1000);
    digitalWrite(LEDod, HIGH);
    delay(100);
    digitalWrite(LEDod, LOW);
    delay(100);
    digitalWrite(LEDod, HIGH);
    delay(100);
    digitalWrite(LEDod, LOW);
    delay(100);
  }

  else if (digitalRead(PUSH5) == 1 && buttonState5 == 1)
  {
    buttonState5 = 0;
    action = 0;
    Serial.println("Manual Mode Aktif");
    String Link;
    HTTPClient http;
    Link = "http://" + String(HOST) + "/Behavior/loadMode.php?&action=" + String(action);
    http.begin(Link);
    http.GET();
    digitalWrite(LEDmode, LOW);
    String respon = http.getString();
    Serial.println("====================" + respon + "====================");
    http.end();
    delay(1000);
    digitalWrite(LEDod, HIGH);
    delay(100);
    digitalWrite(LEDod, LOW);
    delay(100);
    digitalWrite(LEDod, HIGH);
    delay(100);
    digitalWrite(LEDod, LOW);
    delay(100);
  }

  else if (digitalRead(PUSH1) == 1 && buttonState1 == 0)
  {
    buttonState1 = 1;
    Serial.println("==================Lampu 1 Aktif==================");
    idlampu = 1;
    lampS = 1;
    loadData();
  }
  else if (digitalRead(PUSH1) == 1 && buttonState1 == 1)
  {
    buttonState1 = 0;
    Serial.println("==================Lampu 1 Mati===================");
    idlampu = 1;
    lampS = 0;
    loadData();
  }
  //2
  else if (digitalRead(PUSH2) == 1 && buttonState2 == 0)
  {
    buttonState2 = 1;
    Serial.println("==================Lampu 2 Aktif==================");
    idlampu = 2;
    lampS = 1;
    loadData();
  }
  else if (digitalRead(PUSH2) == 1 && buttonState2 == 1)
  {
    buttonState2 = 0;
    Serial.println("==================Lampu 2 Mati===================");
    idlampu = 2;
    lampS = 0;
    loadData();
  }
  //3
  else if (digitalRead(PUSH3) == 1 && buttonState3 == 0)
  {
    buttonState3 = 1;
    Serial.println("==================Lampu 3 Aktif==================");
    idlampu = 3;
    lampS = 1;
    loadData();
  }
  else if (digitalRead(PUSH3) == 1 && buttonState3 == 1)
  {
    buttonState3 = 0;
    Serial.println("==================Lampu 3 Mati===================");
    idlampu = 3;
    lampS = 0;
    loadData();
  }
  //4
  else if (digitalRead(PUSH4) == 1 && buttonState4 == 0)
  {
    buttonState4 = 1;
    Serial.println("==================Lampu 4 Aktif==================");
    idlampu = 4;
    lampS = 1;
    loadData();
  }
  else if (digitalRead(PUSH4) == 1 && buttonState4 == 1)
  {
    buttonState4 = 0;
    Serial.println("==================Lampu 4 Mati===================");
    idlampu = 4;
    lampS = 0;
    loadData();
  }
}
