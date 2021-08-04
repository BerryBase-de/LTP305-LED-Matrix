# LTP305-LED-Matrix
# Pre-requisites
Enable i2c :
```sh
sudo raspi-config nonint do_i2c 0
```
# Installing
1/ The following dependencies :
```sh
sudo apt-get install -y i2c-tools &&
sudo apt-get install -y python-smbus &&
sudo apt-get install python3-pip &&
sudo apt-get install git &&
```
2/ The Stable library from PyPi:
```sh
sudo pip3 install ltp305
```

