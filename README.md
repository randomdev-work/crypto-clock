# crypto-clock
It is a clock with a lot of API stuff for checking crypto from CoinGecko.
The target of this app is Raspberry Pi with a 800x480 display

Tutorial:

Update the system:

1. sudo apt-get update
2. sudo apt-get upgrade

Install git:

1. sudo apt-get install git

Clone and configure:

1. git clone https://github.com/randomdev-work/crypto-clock
2. mkdir /home/pi/.config/autostart
3. nano /home/pi/.config/autostart/crypto-clock.desktop
4. Type:

----------------

[Desktop Entry]

Type=Application
Name=Crypto-clock
Exec=sh /home/pi/crypto-clock/start.sh

----------------


Install libraries:

1. sudo pip3 install matplotlib
2. sudo pip3 install pyautogui
3. sudo pip3 install pygame_gui
4. sudo pip3 install pycoingecko
5. sudo apt-get install libatlas-base-dev
6. sudo apt-get install libsdl2-ttf-2.0-0
7. sudo apt-get install libsdl2-image-2.0-0
