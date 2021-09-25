# requests: 從網頁伺服器上取得想要的資料。 r = requests.get('https://www.google.com.tw/')
# BeautifulSoup: 快速解析網頁 HTML 碼
import requests
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
from tkinter import Label, Tk


url = "https://weather.com/zh-TW/weather/today/l/fe7393b7f2c8eed2cf692bd079361df362d9f0c1c0f896e6e46a649295e15c7d"

# get weather from website
# 獲取HTML資料大部分會用兩種型式儲存.content/.text:
# .content: 一般適用於圖片、文件 ex: page.content是一個html/ .text: 一般適用於字串


# 定義一個視窗 名叫 root
window = Tk()
# configure/config:可以更改label元件的文字(text)屬性 / window.configure(bg ="color") 設定背景顏色
window.title("Weather APP")
window.config(bg="white")
window.geometry('300x220') 

# PIL
img = Image.open("weather.jpg")
img = img.resize((120,120))
# 載入預覽圖片
img = ImageTk.PhotoImage(img)

# tkinter
# w = Label ( 父容器視窗, option ex:bg,font,image... )
# grid(row/column , sticky ="N/S/E/W"  對齊位置, padx/pady 外部padding, ipadx/ipady 內部padding)
locationLabel = Label(window,font = ("Calibri bold", 15), bg="white", text="hello") 
locationLabel.grid(row=0, padx = 20, pady = 10, sticky = "W")
TemperatureLabel = Label(window,font = ("Calibri bold", 50), bg="white") 
TemperatureLabel.grid(row=1, padx = 20, sticky = "W")
WeatherLabel = Label(window,font = ("Calibri bold", 15), bg="white") 
WeatherLabel.grid(row=2, padx = 20, sticky = "W")

Weatherimg = Label(window, image = img, bg ="white").grid(row=1,sticky="W",padx = 160)

def getweather():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    location = soup.find("h1", class_="CurrentConditions--location--kyTeL").text
    temperature = soup.find("span", class_="CurrentConditions--tempValue--3a50n").text
    weather = soup.find("div", class_="CurrentConditions--phraseValue--2Z18W").text

    locationLabel.config(text=location)
    TemperatureLabel.config(text=temperature)
    WeatherLabel.config(text=weather)
    # update every 10 minutes
    # Tkinter window 視窗具有專用方法 after，此方法會在給定時間後呼叫函式-
    window.after(10000, getweather)
    
getweather()
window.mainloop()
