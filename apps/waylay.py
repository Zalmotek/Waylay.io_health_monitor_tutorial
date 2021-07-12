from m5stack import *
from m5stack_ui import *
from uiflow import *
import time
import wifiCfg
import urequests
import json

import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
ncir2 = unit.get(unit.NCIR, unit.PORTA)
heart4 = unit.get(unit.HEART, unit.PORTA)


hr = None
temperature = None
status = None
spo2 = None
json_data = None
DataMap = None

wifiCfg.autoConnect(lcdShow=True)
HeartRate = M5Label('Heart', x=21, y=129, color=0x509ed3, font=FONT_MONT_30, parent=None)
sp = M5Label('SPO2', x=129, y=129, color=0x509ed3, font=FONT_MONT_30, parent=None)
temperature_label = M5Label('TEM', x=239, y=129, color=0x509ed3, font=FONT_MONT_30, parent=None)
label3 = M5Label('Data Sent', x=21, y=207, color=0x509ed3, font=FONT_MONT_14, parent=None)
HttpStat = M5Label('200', x=255, y=207, color=0x509ed3, font=FONT_MONT_14, parent=None)
touch_button0 = M5Btn(text='Button', x=35, y=61, w=35, h=35, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button1 = M5Btn(text='Button', x=142, y=61, w=32, h=32, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button2 = M5Btn(text='Button', x=263, y=46, w=15, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
image0 = M5Img("res/oximeter.png", x=128, y=46, parent=None)
image1 = M5Img("res/pulse.png", x=20, y=46, parent=None)
image2 = M5Img("res/thermometer.png", x=238, y=46, parent=None)
image3 = M5Img("res/waylay.png", x=110, y=207, parent=None)
label0 = M5Label('bpm', x=34, y=158, color=0x509ed3, font=FONT_MONT_14, parent=None)
label1 = M5Label('%', x=154, y=158, color=0x509ed3, font=FONT_MONT_14, parent=None)
label2 = M5Label('Celsius', x=239, y=158, color=0x509ed3, font=FONT_MONT_14, parent=None)


# Describe this function...
def SendPOST():
  global hr, temperature, status, spo2, json_data, DataMap
  status = 'NoStatusCode'
  try:
    req = urequests.request(method='POST', url='replace_with_your_webscript_address',data=json_data, headers={'Content-Type':'application/json'})
    status = req.status_code
    wait(3)
    ps.set_text('Data sent')
  except:
    ps.set_text('Not Sent')
  wait(3)
  HttpStat.set_text(str(status))


def touch_button0_pressed():
  global hr, temperature, status, spo2, json_data, DataMap
  hr = heart4.getHeartRate()
  spo2 = heart4.getSpO2()
  wait_ms(200)
  HeartRate.set_text(str(hr))
  sp.set_text(str(spo2))
  wait(2)
  DataMap = {'HeartRate':hr,'SPO2':spo2}
  json_data = json.dumps(DataMap)
  wait_ms(200)
  SendPOST()
  pass
touch_button0.pressed(touch_button0_pressed)

def touch_button1_pressed():
  global hr, temperature, status, spo2, json_data, DataMap
  hr = heart4.getHeartRate()
  spo2 = heart4.getSpO2()
  wait_ms(200)
  HeartRate.set_text(str(hr))
  sp.set_text(str(spo2))
  wait(2)
  DataMap = {'HeartRate':hr,'SPO2':spo2}
  json_data = json.dumps(DataMap)
  wait_ms(200)
  SendPOST()
  pass
touch_button1.pressed(touch_button1_pressed)

def touch_button2_pressed():
  global hr, temperature, status, spo2, json_data, DataMap
  temperature = ncir2.temperature
  wait(0.2)
  temperature_label.set_text(str(temperature))
  wait(2)
  DataMap = {'Temperature':temperature}
  json_data = json.dumps(DataMap)
  wait_ms(200)
  SendPOST()
  pass
touch_button2.pressed(touch_button2_pressed)

def buttonA_wasPressed():
  global hr, temperature, status, spo2, json_data, DataMap
  hr = heart4.getHeartRate()
  spo2 = heart4.getSpO2()
  wait_ms(200)
  HeartRate.set_text(str(hr))
  sp.set_text(str(spo2))
  wait(2)
  DataMap = {'HeartRate':hr,'SPO2':spo2}
  json_data = json.dumps(DataMap)
  wait_ms(200)
  SendPOST()
  pass
btnA.wasPressed(buttonA_wasPressed)


import custom.urequests as urequests
heart4.setLedCurrent(0x04, 0x01)
heart4.setMode(0x03)

