# LTP305-LED-Matrix
# Pre-requisites

1/ Install the following dependencies :
sudo apt-get install -y i2c-tools &&
sudo apt-get install -y python-smbus &&
sudo apt-get install python3-pip &&

2/ Enable i2c :
sudo raspi-config nonint do_i2c 0

# Installing
Stable library from PyPi:
sudo pip3 install ltp305
