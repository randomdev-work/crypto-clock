# crypto-clock
It is a clock with a lot of API stuff for checking crypto from CoinGecko.
The target of this app is Raspberry Pi with a 800x480 display

Tutorial:

Update the system:

1. sudo apt-get update
2. sudo apt-get upgrade

Install git:

1. sudo apt-get install git-all

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

Install python libraries:

