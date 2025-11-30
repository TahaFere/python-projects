#+ toplama,- çıkarma, / bölme, * çarpma, // virgülsüz bölme, 
#% bölümden kalanı bulma, ** üs alma buna ondalıklı sayılar yazılırsa kök almak içinde kullanılır
#b değişkenini int(sayısal) değerden str(metin) türüne değiştirilmi\ş oldu
#mantıksal - boolean (true-false)
#sayılar (tam sayılar küsüratlı sayılar)-int
#karakter dizisi -str
#liste-list
#demetler - tuple
#kümeler set
#sözlükler dictionry
#
#----------IMPORT BÖLÜMÜ-------
import math #matematik kütüphanesini eklemiş olduk
import time # zaman modülünü py dosyasına dahil ettik
import os # işletim sistemi modülünü py dosyasına dahil ettik
import random # rastgele sayı modülünü py dosyasına dahil ettik
import sys # sistem modülünü py dosyasına dahil ettik
from os import name #os modülünden sadece name özelliğini dahil ettik
from bs4 import BeautifulSoup
import requests
import re
import urllib.parse
import urllib.request 
import time
import locale
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as nsn

a=int(input("sayı:"))

if(a==1):
    import py1
    py1.bir()#pythona giriş
elif(a==2):
    import py2 
    py2.iki()#print ile yazım çeşitliliği
elif(a==3):
    import py3 
    py3.uc()#aritmetik operatörler
elif(a==4):
    import py4 
    py4.dort()#kullanıcan veri almak
elif(a==5):
    import py5
    py5.bes()#delta hesaplama
elif (a==6):
       import py6
       py6.altı()#if elseif else yapısı 
if(a==7):
    import py7
    py7.yedi()#döngüler
if(a==8):
    import py8
    py8.sekiz()#faktöriyel hesaplama, basamak hesaplama, asal sayı kont, EBOB-EKOK hesaplama
if(a==9):
    import py9
    py9.dokuz()# üçgen kont, şifre kont, mükenmel sayı kont
if(a==10):
    import py10
    py10.on()#armstrong sayı kont
if(a==11):
    import py11
    py11.onbir()#listeler
if(a==12):
    import py12
    py12.oniki()#demetler
if(a==13):
    import py13
    py13.onuc()#sözlükler
if(a==14):
    import py14
    py14.ondort()#kümeler
if(a==15):
    import py15
    py15.onbes()# fonksiyonlar
if(a==16):
    import py16
    py16.onalti()#matematik modülü
if(a==17):
    import py17
    py17.onyedi()#string kokmutları
if(a==18):
    import py18 
    py18.onsekiz()

if(a==19):
    import py19
    py19.ondokuz()#try except 
if(a==20):
    import py20
    py20.yirmi()#dosya klasör işlemleri
if(a==21):
    import py21
    py21.yirmibir()# dosya uygulamarı
if(a==22):
    import py22
    py22.yirmiiki()#dosya uygulamarı
if(a==23):
    import py23
    py23.yirmiüc()#class 
if(a==24):
    import py24
    py24.yirmidort()#class 
if(a==25):
    import py25
    py25.yirmibeş()#class uygulama 
if(a==26):
    import py26
    py26.yirmialtı()#class uygulama
if(a==27):
    import py27
    py27.yirmiyedi()#class uygulama
if(a==28):
    import py28
    py28.yirmisekiz()#class miras
if(a==29):
    import py29
    py29.yirmidokuz()#class miras uygulama
if(a==30):
    import py30
    py30.otuz()#class miras uygulaması insan-ögrenci
if(a==31):
    import py31
    py31.otuzbir()#class miras uygulaması banka
if(a==32): 
    import py32
    py32.otuziki()#class miras uygulaması ücgen kont
if(a==33):
    import py33
    py33.otuzüc()#class miras uygulaması ücgen kont
if(a==35):
    import py35
    py35.otuzbes()#class miras uygulaması iterasyon
if(a==36):
    import py36
    py36.otuzalti()#iterasyon yield iter, next() ve StopIteration
if(a==37):
    import py37
    py37.otuzyedi()#math, time, os, random, sys modülleri tanımı
if(a==38):
    import py38
    py38.otuzsekiz()#kendi modülümüzü oluşturma ve os modülünü inceleme
if(a==39):
    import py39
    py39.otuzdokuz()#sys modülünü inceleme
if(a==40):
    import py40
    py40.kirk()#datetime modülünü inceleme
if(a==41):
    import py41
    py41.kirkbir()#time modülünü inceleme
if(a==42):
    import py42
    py42.kirkiki()#random modülünü inceleme
if(a==43):
    import py43
    py43.kirkuc()#REQUEST MODÜLÜ HTTP İŞLEMLERİ
if(a==44):
    import py44
    py44.kırkdort()#REQUEST modülü get post header text request elapsed
if(a==45):
    import py45
    py45.kirkbes()#BEAUTİFULSOUP MODÜLÜ
if(a==46):
    import py46
    py46.kirkaltı()#BEAUTİFULSOUP MODÜLÜ ile sitelerden veri çekme listeleme
if(a==47):
    import py47
    py47.kirkyedi()#SQLİTE
if(a==48):
    import py48
    py48.kırksekiz()#SQLİTE uygulamaları
if(a==49):
    import py49
    py49.kırkdokuz()#numpy modülü