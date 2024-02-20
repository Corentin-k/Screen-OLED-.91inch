#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging    
import time
import traceback
import getopt
from waveshare_OLED import OLED_0in91
from PIL import Image, ImageDraw, ImageFont
import netifaces as ni
import subprocess

def get_ip():
    try:
        interface = 'wlan0'
        ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
        return ip
    except Exception as e:
        return False

def get_ssid():
    try:
       ssid=os.popen("sudo iwgetid -r").read()
       return ssid
    except Exception as e:
       return ""

disp = OLED_0in91.OLED_0in91()
disp.Init()

font1 = ImageFont.truetype("DejaVuSansMono.ttf", 12)
font2 = ImageFont.truetype("DejaVuSansMono.ttf", 11)
font3 = ImageFont.truetype("DejaVuSansMono.ttf", 9)



while True:
    IP = get_ip()
    if not IP:
        IP = "pas de connexion"
        ssid = ''
    else:
        ssid = get_ssid()
    disp.clear()
    image = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image)
    draw.text((2, 0),ssid, font=font1, fill=0)
    draw.text((2, 12), "Adresse IP : ", font=font2, fill=0)
    draw.text((2, 23), IP, font=font3, fill=0)
    disp.ShowImage(disp.getbuffer(image))
    time.sleep(15)