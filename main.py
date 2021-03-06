import pyowm
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QFont
import sys
import os

font = QFont()
font.setBold(True)



owm = pyowm.OWM("99cae5d33c52bee408d9bac48337530b")
sehir = owm.weather_at_place("Istanbul,tr")

sehirdekihava = sehir.get_weather()
print(sehirdekihava)


sicaklikbilgisi = sehirdekihava.get_temperature('celsius')
print(sicaklikbilgisi)
sicaklikfoto = sicaklikbilgisi["temp"]
sicaklik=str(sicaklikbilgisi["temp"])


havadurumu = sehirdekihava.get_status()
print(havadurumu)

sehirbilgisi = sehir.get_location()
sehiradi = sehirbilgisi.get_name()
print(sehiradi)



class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(250,150)
        self.setWindowTitle("ProjectW")
        self.setWindowIcon(QIcon("9601-200.png"))


        sehiradilabel = QLabel(sehiradi,self)
        sehiradilabel.setGeometry(48,18,50,100)
        sehiradilabel.setFont(font)

        sehiradilabel1 = QLabel("City:",self)
        sehiradilabel1.setGeometry(18,18,30,100)
        sehiradilabel1.setFont(font)

        havadurumulabel = QLabel(havadurumu,self)
        havadurumulabel.setGeometry(58, 50, 100, 10)
        havadurumulabel.setFont(font)

        havadurumulabel1 = QLabel("Status:",self)
        havadurumulabel1.setGeometry(18, 50, 100, 10)
        havadurumulabel1.setFont(font)



        sicakliklabel1 = QLabel("Degree:",self)
        sicakliklabel1.setGeometry(18,34,100,15)
        sicakliklabel1.setFont(font)

        sicakliklabel = QLabel(sicaklik,self)
        sicakliklabel.setGeometry(65,34,100,15)
        sicakliklabel.setFont(font)



        if havadurumu==("Clear"):
            durumyolu = ("sun.png")
        elif havadurumu==("Clouds"):
            durumyolu =("b104f5bf21a9dd0a5b074f34b4508f19_download-black-cloud-clipart_512-512.png")
        elif havadurumu==("Rain"):
            durumyolu= ("black-cloud-with-rain_318-44337.jpg")
        havalogo = QLabel(self)
        havalogo.setGeometry(110,5,128,128)
        havalogo.setPixmap(QPixmap(durumyolu))

uygulama = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
uygulama.exec_()



