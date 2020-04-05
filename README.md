# Links shortening with bit.ly service 

Program allows you to create short links from long links
using [bitly](bit.ly) service. 
Also it allows to monitor the quantity of clicks for your 
short bitly links.

### How to install

Python3 should be already installed. Then use pip 
(or pip3, if there is a conflict with Python2) to 
install dependencies:
```
pip install -r requirements.txt
```
Bitly uses OAuth access token for authentication for many
API methods. After registering in Bitly go to your profile 
settings and chose Generic Access Token. Create an **.env** file
in the same directory with **main.py** file. Now add copied 
Access Token to **.env** file in the following format:
```
ACCESS_TOKEN = "here should be your token"
```

### An example of usage

```
>python main.py -l https://guides.github.com
Generated bitlink: bit.ly/2JHUYWm

>python main.py -l bit.ly/33J9g26
Clicks count for bit.ly/33J9g26: 5
```

### Project goals

The code is written for educational purposes on online-course 
for web-developers [devman](dvmn.org).