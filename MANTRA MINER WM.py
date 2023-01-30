from bs4 import BeautifulSoup
import requests
import sys
import pandas
from tkinter import *
import tkinter as tk
import os

root = Tk()
root.title("MANTRA MINER")
root['bg']='orange'
root.geometry("700x600")
w = Label(root, text ='SACRED SOUNDS OF SPRITIUAL MANTRAS', fg = "orange", font = "80")
w.pack()

txtarea = Text(root, width=90, height=25)
txtarea.pack(pady=20)

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}


def Ganesha():
    source=requests.get('https://www.drikpanchang.com/vedic-mantra/gods/lord-ganesha/ganesha-mantras.html',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')
    print("ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐLORD GANESHA ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ")

    for t in soup.find_all('h3',class_='dpContentSubTitle'):#Titile
      mn=t.text
      print(mn)
    for r in soup.find_all('p',class_='dpContent dpMantra'):#English
      sans=r.text
      print(sans)
    for s in soup.find_all('p',class_='dpContent dpMantra'):#Sanskrit
      eng=s.text
      print(eng)
    om = "\nॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ LORD GANESHA ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ"+"\n\nMantra Name:"+ mn +"\n\n卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐" +"\n\n" +"Sanskrit:"+ sans +"\n\n卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐"+"  "+ "\n"+"\n"+"English:"+"  "+ eng +"\n\n 卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐"
    with open('C:/Users/DJPatil/Documents/Mantra/LordGanesha.txt', 'w',  encoding='utf-8') as output:
              output.write(om)
    tf=open("C:/Users/DJPatil/Documents/Mantra/LordGanesha.txt",  encoding='utf-8')
    data=tf.read()
    txtarea.delete("1.0","end")
    txtarea.insert(END, data)
    tf.close()




def Vishnu():
    source=requests.get('https://www.drikpanchang.com/vedic-mantra/gods/lord-vishnu/vishnu-mantras.html',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')
    print("ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ LORD VISHNU ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ")

    for t in soup.find_all('h3',class_='dpContentSubTitle'):#Titile
      mn=t.text
      print(mn)
    for r in soup.find_all('p',class_='dpContent dpMantra'):#English
      sans=r.text
      print(sans)
    for s in soup.find_all('p',class_='dpContent dpMantra'):#Sanskrit
      eng=s.text
      print(eng)
    om = "\nॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ LORD VISHNU ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ"+"\n\nMantra Name:"+ mn +"\n\n卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐" +"\n\n" +"Sanskrit:"+ sans +"\n\n卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐"+"  "+ "\n"+"\n"+"English:"+"  "+ eng +"\n\n 卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐"
    with open('C:/Users/DJPatil/Documents/Mantra/LordVishnu.txt', 'w',  encoding='utf-8') as output:
              output.write(om)
    tf=open("C:/Users/DJPatil/Documents/Mantra/LordVishnu.txt",  encoding='utf-8')
    data=tf.read()
    txtarea.delete("1.0","end")
    txtarea.insert(END, data)
    tf.close()





def Rama():
    source=requests.get('https://www.drikpanchang.com/lyrics/ramayana/nama-ramayanam/nama-ramayanam-lyrics.html',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')
    print("ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ LORD RAMA ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ")

    for t in soup.find_all('span',class_='dpTitleHighlighter'):#Titile
      mn=t.text
      print(mn)
    for r in soup.find_all('div',class_='dpLyricsBlock'):#English
      sans=r.text
      print(sans)
  
    om = "\nॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ LORD RAMA ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ"+"\n\nMantra Name:"+ mn +"\n\n卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐" +"\n\n" +"Sanskrit:"+ sans +"\n\n卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐"
    with open('C:/Users/DJPatil/Documents/Mantra/LordRama.txt', 'w',  encoding='utf-8') as output:
              output.write(om)
    tf=open("C:/Users/DJPatil/Documents/Mantra/LordRama.txt",  encoding='utf-8')
    data=tf.read()
    txtarea.delete("1.0","end")
    txtarea.insert(END, data)
    tf.close()




def Shiva():
    source=requests.get('https://www.drikpanchang.com/vedic-mantra/gods/lord-shiva/shiva-mantras.html',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')
    print("ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ LORD SHIVA ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ")

    for t in soup.find_all('h3',class_='dpContentSubTitle'):#Titile
      mn=t.text
      print(mn)
    for r in soup.find_all('p',class_='dpContent dpMantra'):#English
      sans=r.text
      print(sans)
    for s in soup.find_all('p',class_='dpContent dpMantra'):#Sanskrit
      eng=s.text
      print(eng)
    om = "\nॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ LORD SHIVA ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ"+"\n\nMantra Name:"+ mn +"\n\n卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐" +"\n\n" +"Sanskrit:"+ sans +"\n\n卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐"+"  "+ "\n"+"\n"+"English:"+"  "+ eng +"\n\n 卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐"
    with open('C:/Users/DJPatil/Documents/Mantra/LordShiva.txt', 'w',  encoding='utf-8') as output:
              output.write(om)
    tf=open("C:/Users/DJPatil/Documents/Mantra/LordShiva.txt",  encoding='utf-8')
    data=tf.read()
    txtarea.delete("1.0","end")
    txtarea.insert(END, data)
    tf.close()





def Hanuman():
    source=requests.get('https://www.drikpanchang.com/vedic-mantra/gods/lord-hanuman/hanuman-mantras.html',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')
    print("ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ LORD HANUMAN ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ")

    for t in soup.find_all('h3',class_='dpContentSubTitle'):#Titile
      mn=t.text
      print(mn)
    for r in soup.find_all('p',class_='dpContent dpMantra'):#English
      sans=r.text
      print(sans)
    for s in soup.find_all('p',class_='dpContent dpMantra'):#Sanskrit
      eng=s.text
      print(eng)
    om = "\nॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ LORD HANUMAN ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ"+"\n\nMantra Name:"+ mn +"\n\n卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐" +"\n\n" +"Sanskrit:"+ sans +"\n\n卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐"+"  "+ "\n"+"\n"+"English:"+"  "+ eng +"\n\n 卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐"
    with open('C:/Users/DJPatil/Documents/Mantra/LordHanuman.txt', 'w',  encoding='utf-8') as output:
              output.write(om)
    tf=open("C:/Users/DJPatil/Documents/Mantra/LordHanuman.txt",  encoding='utf-8')
    data=tf.read()
    txtarea.delete("1.0","end")
    txtarea.insert(END, data)
    tf.close()





def Kubera():
    source=requests.get('https://www.drikpanchang.com/vedic-mantra/gods/shri-kubera/kubera-mantras.html',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')
    print("ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ LORD KUBERA ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ")

    for t in soup.find_all('h3',class_='dpContentSubTitle'):#Titile
      mn=t.text
      print(mn)
    for r in soup.find_all('p',class_='dpContent dpMantra'):#English
      sans=r.text
      print(sans)
    for s in soup.find_all('p',class_='dpContent dpMantra'):#Sanskrit
      eng=s.text
      print(eng)
    om = "\nॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ LORD KUBERA ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ"+"\n\nMantra Name:"+ mn +"\n\n卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐" +"\n\n" +"Sanskrit:"+ sans +"\n\n卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐"+"  "+ "\n"+"\n"+"English:"+"  "+ eng +"\n\n 卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐"
    with open('C:/Users/DJPatil/Documents/Mantra/LordKubera.txt', 'w',  encoding='utf-8') as output:
              output.write(om)
    tf=open("C:/Users/DJPatil/Documents/Mantra/LordKubera.txt",  encoding='utf-8')
    data=tf.read()
    txtarea.delete("1.0","end")
    txtarea.insert(END, data)
    tf.close()




def Lakshmi():
    source=requests.get('https://www.drikpanchang.com/vedic-mantra/goddesses/lakshmi/lakshmi-mantras.html',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')
    print("ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ GODDESS LAKSHMI ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ")

    for t in soup.find_all('h3',class_='dpContentSubTitle'):#Titile
      mn=t.text
      print(mn)
    for r in soup.find_all('p',class_='dpContent dpMantra'):#English
      sans=r.text
      print(sans)
    for s in soup.find_all('p',class_='dpContent dpMantra'):#Sanskrit
      eng=s.text
      print(eng)
    om = "\nॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ GODDESS LAKSHMI ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ"+"\n\nMantra Name:"+ mn +"\n\n卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐" +"\n\n" +"Sanskrit:"+ sans +"\n\n卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐"+"  "+ "\n"+"\n"+"English:"+"  "+ eng +"\n\n 卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐"
    with open('C:/Users/DJPatil/Documents/Mantra/GoddessLakshmi.txt', 'w',  encoding='utf-8') as output:
              output.write(om)
    tf=open("C:/Users/DJPatil/Documents/Mantra/GoddessLakshmi.txt",  encoding='utf-8')
    data=tf.read()
    txtarea.delete("1.0","end")
    txtarea.insert(END, data)
    tf.close()






def Gayatri():
    source=requests.get('https://www.drikpanchang.com/vedic-mantra/goddesses/gayatri/rigveda-gayatri-mantra.html',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')
    print("ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ GODDESS GAYATRI ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ")

    t= soup.find('h2',class_='dpMiddleTitle')#Titile
    mn=t.text
    print(mn)
    for r in soup.find_all('p',class_='dpContent dpMantra'):#English
      sans=r.text
      print(sans)
    for s in soup.find_all('p',class_='dpContent dpMantra'):#Sanskrit
      eng=s.text
      print(eng)
    om = "\nॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ GODDESS GAYATRI ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ"+"\n\nMantra Name:"+ mn +"\n\n卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐" +"\n\n" +"Sanskrit:"+ sans +"\n\n卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐"+"  "+ "\n"+"\n"+"English:"+"  "+ eng +"\n\n 卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐"
    with open('C:/Users/DJPatil/Documents/Mantra/GoddessGayatri.txt', 'w',  encoding='utf-8') as output:
              output.write(om)
    tf=open("C:/Users/DJPatil/Documents/Mantra/GoddessGayatri.txt",  encoding='utf-8')
    data=tf.read()
    txtarea.delete("1.0","end")
    txtarea.insert(END, data)
    tf.close()






def Saraswati():
    source=requests.get('https://www.drikpanchang.com/vedic-mantra/goddesses/saraswati/saraswati-mantras.html',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')
    print("ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ GODDESS SARASWATI ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ")

    for t in soup.find_all('h3',class_='dpContentSubTitle'):#Titile
      mn=t.text
      print(mn)
    for r in soup.find_all('p',class_='dpContent dpMantra'):#English
      sans=r.text
      print(sans)
    for s in soup.find_all('p',class_='dpContent dpMantra'):#Sanskrit
      eng=s.text
      print(eng)
    om = "\nॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ GODDESS SARASWATI ॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐॐ"+"\n\nMantra Name:"+ mn +"\n\n卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐" +"\n\n" +"Sanskrit:"+ sans +"\n\n卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐"+"  "+ "\n"+"\n"+"English:"+"  "+ eng +"\n\n 卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐"
    with open('C:/Users/DJPatil/Documents/Mantra/GoddessSaraswati.txt', 'w',  encoding='utf-8') as output:
              output.write(om)
    tf=open("C:/Users/DJPatil/Documents/Mantra/GoddessSaraswati.txt",  encoding='utf-8')
    data=tf.read()
    txtarea.delete("1.0","end")
    txtarea.insert(END, data)
    tf.close()















b1_button = Button(root, text ="Lord Ganesha", command= Ganesha,fg ="Red").place(x=100, y=450)


b2_button = Button(root, text ="Lord Vishnu", command=Vishnu, fg ="Red").place(x=200, y=450) 


b3_button = Button(root, text ="Lord Rama", command=Rama, fg ="Red").place(x=300, y=450)


b4_button = Button(root, text ="Lord Shiva", command=Shiva, fg ="Red").place(x=400, y=450)


b5_button = Button(root, text ="Lord Hanuman", command=Hanuman, fg ="Red").place(x=500, y=450)


b6_button = Button(root, text ="Lord Kubera",command=Kubera, fg ="Red").place(x=100, y=500)


b7_button = Button(root, text ="Goddess Lakshmi", command=Lakshmi,  fg ="Red").place(x=200, y=500)

b8_button = Button(root, text ="Goddess Gayatri",command=Gayatri, fg ="Red").place(x=320, y=500)

b9_button = Button(root, text ="Goddess Saraswati", command=Saraswati, fg ="Red").place(x=450, y=500)




root.mainloop()

