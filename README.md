# 0.91-inch OLED Screen

 by Corentin-k

---

This is a screen compatible with Arduino/Raspberry Pi that can display the IP address and SSID of the Raspberry Pi's connection.

For my project, I'm using the OLED_0in91 library.

To install the dependencies, you can follow the steps outlined on this website : [RPi_OLED_0.91_i2c](https://levelkro.xyz/wiki/RPi_OLED_0.91_i2c).

I've modified the original Python program :  [display.py](/display.py).

To connect the screen, you can refer to the GPIO pins on this site : [pinout.xyz](https://pinout.xyz/pinout/pin7_gpio4/). The screen uses one pin for power, one for ground, and two others for communication: SDA (GPIO 2) and SCL (GPIO 3).

> :bulb: The SDA pin is used to send data to the screen, and the SCL pin is used to synchronize the data with a clock.

After this, I use the crontab ('Chronos' + 'table') to schedule tasks. I've programmed a task to run when the Raspberry Pi boots or reboots. Essentially, the screen lights up and displays the SSID and IP address of the current connection of the Raspberry Pi.

This setup allows me to use VNC and other software to interact with my Raspberry Pi using my laptop.

You can download or create the shell script document. Then, to access the [crontab]((https://www.raspberrypi-france.fr/lancer-un-script-python-au-demarrage-du-raspberry-pi/)), follow these steps:

    crontab -e

Choose the text editor (I prefer to use the nano editor). At the end of the document, enter:

    @reboot sh /home/pi/lancement.sh > /home/pi/logs/log.txt 2>&1
This line schedules the execution of the lancement.sh script upon reboot, and it redirects any output to a log file located at /home/pi/logs/log.txt.
