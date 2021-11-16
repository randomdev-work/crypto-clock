# crypto-clock
It is a clock with a lot of API stuff for checking crypto from CoinGecko.
The target of this app is Raspberry Pi with a 800x480 display

Tutorial:

Update the system:

1. sudo apt-get update
2. sudo apt-get upgrade

Install packages:

1. sudo apt-get install git

Execute in terminal

1. git clone https://github.com/randomdev-work/crypto-clock
2. nano start.sh (Open nano editor)
3. 
Type:
----------------
#!/bin/sh

cd crypto-clock
python3 main.py
cd ..
----------------

3. Ctrl + O to save
4. sudo crontab -e
5. Select editor (nano is the best)

---------------------------------------------------------
Select an editor.  To change later, run 'select-editor'.
  1. /bin/nano        <---- easiest
  2. /usr/bin/vim.tiny
  3. /bin/ed

Choose 1-3 [1]: 1
---------------------------------------------------------

6. At the end enter this line:

-----------------------------
@reboot sh /home/pi/start.sh
-----------------------------

7. Ctrl + O to save
8. sudo reboot
