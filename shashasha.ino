#include <ESP8266WebServer.h>
ESP8266WebServer server;
const char username[] = "govind";
const char passwd[] = "jaggugullu";



void setup() {
  Serial.begin(115200);
  WiFi.softAP(username, passwd);
  
  
  IPAddress myIP = WiFi.softAPIP();
  Serial.print(myIP);
  server.begin();
  server.on("/pwm_value", print_val);
  // put your setup code here, to run once:

}

void loop() {
  server.handleClient();
  // put your main code here, to run repeatedly:

}
void print_val(){
  String html = "";
  server.send(200, "text/html", html);
  Serial.println(server.arg("state"));
}

