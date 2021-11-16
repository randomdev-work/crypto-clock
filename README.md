# crypto-clock
It is a clock with a lot of API stuff for checking crypto from CoinGecko.
The target of this app is Raspberry Pi with a 800x480 display

Tutorial:

Update the system:
```
sudo apt-get update
sudo apt-get upgrade
```
Install git:
```
sudo apt-get install git
```
Clone and configure autostart:
```
git clone https://github.com/randomdev-work/crypto-clock
mkdir /home/pi/.config/autostart
nano /home/pi/.config/autostart/crypto-clock.desktop
```
Type:

```
[Desktop Entry]

Type= Application
Name= Crypto-clock
Exec= sh /home/pi/crypto-clock/start.sh
```

Install libraries:
```
sudo pip3 install matplotlib
sudo pip3 install pyautogui
sudo pip3 install pygame_gui
sudo pip3 install pycoingecko
sudo apt-get install libatlas-base-dev
sudo apt-get install libsdl2-ttf-2.0-0
sudo apt-get install libsdl2-image-2.0-0
```
