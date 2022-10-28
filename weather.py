from bs4 import BeautifulSoup
from requests import get
import requests,sys,time

def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.009)

ip=requests.get('https://api.ipify.org').text
localtime=time.asctime(time.localtime(time.time()))

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
 
 

def weather(city):

    city = city.replace(" ", "+")

    res = requests.get(

        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

    print("Searching...\n")

    soup = BeautifulSoup(res.text, 'html.parser')

    location = soup.select('#wob_loc')[0].getText().strip()

    time = soup.select('#wob_dts')[0].getText().strip()

    weather = soup.select('#wob_dc')[0].getText().strip()

    temp = soup.select('#wob_tm')[0].getText().strip()
    print(40*"=")
    autoketik(f"""
    Your IP    : {ip}
    Today      : {localtime}
    Location   : {location}
    Timezone   : {time}
    Weather    : {weather}
    Temperatur : {temp}°C""")


city = input("Enter City Name : ")
city = city+" weather"
weather(city)
