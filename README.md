

  <br>

<p align=center>
  <a href="https://www.instagram.com/seefu.x"><img title="Made in iraq" src="https://img.shields.io/badge/MADE%20IN-IRAQ-SCRIPT?colorA=black&colorB=red&colorC=black&style=for-the-badge"></a>
  </p>

###### <p align="center"> *Eye Scorpion*

  <br>
<a target="_blank" href="https://www.youtube.com/c/%D8%B3%D9%8A%D9%81%D9%88%D8%A7%D9%84%D8%AC%D9%86%D8%A7%D8%A8%D9%8A0/featured">
<p align="center"><img title="سيفو الجنابي" src="res/iraq.png"  width="10%" height="40%" ></p>
</a>


###### <p align="center"> GPS Location Tracker (Android, IOS, Windows phones.)
<p align=center>
  <a href="https://www.instagram.com/seefu.x"><img title="GitHub version" src="https://d25lcipzij17d.cloudfront.net/badge.svg?id=gh&type=6&v=1.1&x2=1" ></a>
  <a href="#"><img src="https://badges.pufler.dev/visits/seefu-x/EyeScorpion/">

###### <p align="center">*This is official repository maintained by us*
###### <p align="center"> *[**seefu.x**](https://www.instagram.com/seefu.x/) ❤️*
###### <p align="center"> *You can check [youtube](https://www.youtube.com/c/%D8%B3%D9%8A%D9%81%D9%88%D8%A7%D9%84%D8%AC%D9%86%D8%A7%D8%A8%D9%8A0/featured)✌*

## EYE SCORPION

Concept behind scorpion.py is simple, just like we host phishing pages to get credentials why not host a fake page that requests your location like many popular location based websites. Read more on Seefu AL-janabi Blog eyescorpion.py Hosts a fake website which asks for Location Permission and if the target allows it, we can get :

* Longitude
* Latitude
* Accuracy
* Altitude - Not always available
* Direction - Only available if user is moving
* Speed - Only available if user is moving

Along with Location Information we also get **Device Information** without any permissions :

* Unique ID using Canvas Fingerprinting
* Device Model - Not always available
* Operating System
* Platform
* Number of CPU Cores - Approximate Results
* Amount of RAM - Approximate Results
* Screen Resolution
* GPU information
* Browser Name and Version
* Public IP Address
* Local IP Address
* Local Port


Available Templates :

* WhatsApp group
* Telegram

## Tested On :

* Kali Linux
* BlackArch Linux
* Ubuntu
* Kali Nethunter
* Termux
* Parrot OS

## Installation

### Basic For Beginners

```bash
$ git clone https://github.com/bhikandeshmukh/MapEye.git
$ cd EyeScorpion
$ python3 EyeScorpion.py -t manual -k testkml
```

### ngrok setup

```bash
go to ngrok.com (Login)
Download ngrok
$ unzip ngrok.zip
$ ./ngrok authtoken *******
$ ./ngrok http 122
send link to victim
```

### Kali Linux / Ubuntu / Parrot OS

```bash
git clone https://github.com/bhikandeshmukh/MapEye.git
cd EyeScorpion
apt update
apt install python3 python3-pip php
pip3 install requests
```

### BlackArch Linux

```bash
pacman -S eyescorpion.py
```

### Termux

```bash
git clone https://github.com/bhikandeshmukh/MapEye.git
cd EyeScorpion
pkg update
pkg install python php
pip3 install requests
```

## Usage

```bash
python3 eyescorpion.py -h

usage: eyescorpion.py [-h] [-s SUBDOMAIN]

optional arguments:
  -h, --help            show this help message and exit
  -k KML, --kml         Provide KML Filename ( Optional )
  -p PORT, --port       Port for Web Server [ Default : 8080 ]
  -t TUNNEL, --tunnel   Specify Tunnel Mode [ Available : manual ]

##################
# Usage Examples #
##################

# Step 1 : In first terminal
$ python3 eyescorpion.py -t manual

# Step 2 : In second terminal start a tunnel service such as ngrok
$ ./ngrok http 122

###########
# Options #
###########

# Ouput KML File for Google Earth
$ python3 eyescorpion.py -t manual -k <filename>

# Use Custom Port
$ python3 eyescorpion.py -t manual -p 1337
$ ./ngrok http 1337

```

### Legal Disclaimer :

Usage of the tool for attacking targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

-------------------------------------------------------------------------------------

### Development by

Developer / Author: [Seefu AL-janabi ](https://www.instagram.com/seefu.x/)

<p align="center">
<a href="https://www.instagram.com/seefu.x/"><img title="Instagram" src="https://img.shields.io/badge/instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white"></a>
<a href="https://www.facebook.com/seefu.janabi/"><img title="facebook" src="https://img.shields.io/badge/facebook-%231877F2.svg?&style=for-the-badge&logo=facebook&logoColor=white"></a>
<a href="https://www.twitter.com/seefu_x/"><img title="twitter" src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white"></a>
</p>

-------------------------------------------------------------------------------------
