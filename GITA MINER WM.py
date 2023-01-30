from bs4 import BeautifulSoup
import requests
import sys

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

def Anger():
    
    source=requests.get('https://vedabase.io/en/library/bg/16/1-3/',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')

    i=soup.find('div',id='bb3626',class_='r r-title r-verse')#Sloka
    sn=i.text
    print("  \n " + sn)

    print('***************************************************************')

    s=soup.find('div', id ="bb568422", class_='r r-devanagari')#Sanskrit
    sans=s.text
    print("  \n" + sans)

    print('***************************************************************')


    e=soup.find('div',id=('bb3627','bb3628','bb3629'),class_='r r-lang-en r-verse-text')#English
    eng=e.text
    print("  \n " + eng)


    print('***************************************************************')


    t=soup.find('div',id='bb3631',class_='r r-lang-en r-translation')#Translation
    trans=t.text
    print("  \n" +trans)


    print('***************************************************************')


    p=soup.find('div',id=('bb3632','bb3633','bb3634','bb3635','bb3636','bb3637','bb3638','bb3639','bb3640','bb3641','bb3642','bb3643','bb3644','bb3645','bb3646','bb3647','bb3648','bb3649'),class_='r r-lang-en r-paragraph')#Purport
    pur=p.text
    print("  \n" + pur)


    print('***************************************************************')
    om = "BG Chapter.verse:"+sn+ "\n" +"Sanskrit:"+ sans +"  "+ "\n"+"\n"+"English:"+"  "+ eng + "  " +"\n"+"\n"+"\n" + "Translation:"+"  "+ trans + "  " +"\n"+"\n"+"\n"+ "Purport:"+"  "+ pur +"  "
    with open('C:/Users/DJPatil/Documents/Gita/Anger.txt', 'w',  encoding='utf-8') as output:
              output.write(om)



Anger()

def Fear():
    source=requests.get('https://vedabase.io/en/library/bg/18/61/',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')

    i=soup.find('div',id='bb4189',class_='r r-title r-verse')#Sloka
    sn=i.text
    print("  \n " + sn)

    print('***************************************************************')

    s=soup.find('div', id ="bb568525", class_='r r-devanagari')#Sanskrit
    sans=s.text
    print("  \n" + sans)

    print('***************************************************************')


    e=soup.find('div',id='bb4190',class_='r r-lang-en r-verse-text')#English
    eng=e.text
    print("  \n " + eng)


    print('***************************************************************')


    t=soup.find('div',id='bb4192',class_='r r-lang-en r-translation')#Translation
    trans=t.text
    print("  \n" +trans)


    print('***************************************************************')


    p=soup.find('div',id='bb4193',class_='r r-lang-en r-paragraph')#Purport
    pur=p.text
    print("  \n" + pur)


    print('***************************************************************')
    om = "BG Chapter.verse:"+sn+ "\n" +"Sanskrit:"+ sans +"  "+ "\n"+"\n"+"English:"+"  "+ eng + "  " +"\n"+"\n"+"\n" + "Translation:"+"  "+ trans + "  " +"\n"+"\n"+"\n"+ "Purport:"+"  "+ pur +"  "
    with open('C:/Users/DJPatil/Documents/Gita/Fear.txt', 'w',  encoding='utf-8') as output:
              output.write(om)

Fear()


def Lust():
    source=requests.get('https://vedabase.io/en/library/bg/5/22/',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')

    i=soup.find('div',id='bb1496',class_='r r-title r-verse')#Sloka
    sn =i.text
    print("  \n " + sn)

    print('***************************************************************')

    s=soup.find('div', id ="bb568101", class_='r r-devanagari')#Sanskrit
    sans=s.text
    print("  \n" + sans)

    print('***************************************************************')


    e=soup.find('div',id='bb1497',class_='r r-lang-en r-verse-text')#English
    eng=e.text
    print("  \n " + eng)


    print('***************************************************************')


    t=soup.find('div',id='bb1499',class_='r r-lang-en r-translation')#Translation
    trans=t.text
    print("  \n" +trans)


    print('***************************************************************')


    p=soup.find('div',id=('bb1500','bb1501','bb1502','bb1503','bb1504','bb1505','bb1506' ),class_='r r-lang-en r-paragraph')#Purport
    pur=p.text
    print("  \n" + pur)


    print('***************************************************************')
    om = "BG Chapter.verse:"+sn+ "\n" +"Sanskrit:"+ sans +"  "+ "\n"+"\n"+"English:"+"  "+ eng + "  " +"\n"+"\n"+"\n" + "Translation:"+"  "+ trans + "  " +"\n"+"\n"+"\n"+ "Purport:"+"  "+ pur +"  "
    with open('C:/Users/DJPatil/Documents/Gita/Lust.txt', 'w',  encoding='utf-8') as output:
              output.write(om)

Lust()

def Confusion():
    source=requests.get('https://vedabase.io/en/library/bg/2/7/',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')

    i=soup.find('div',id='bb440',class_='r r-title r-verse')#Sloka
    sn =i.text
    print("  \n " + sn)

    print('***************************************************************')

    s=soup.find('div', id ="bb567931", class_='r r-devanagari')#Sanskrit
    sans=s.text
    print("  \n" + sans)

    print('***************************************************************')


    e=soup.find('div',id='bb441',class_='r r-lang-en r-verse-text')#English
    eng=e.text
    print("  \n " + eng)


    print('***************************************************************')


    t=soup.find('div',id='bb443',class_='r r-lang-en r-translation')#Translation
    trans=t.text
    print("  \n" +trans)


    print('***************************************************************')


    p=soup.find('div',id=('bb444','bb445','bb446'),class_='r r-lang-en r-paragraph')#Purport
    pur=p.text
    print("  \n" + pur)


    print('***************************************************************')
    om = "BG Chapter.verse:"+sn+ "\n" +"Sanskrit:"+ sans +"  "+ "\n"+"\n"+"English:"+"  "+ eng + "  " +"\n"+"\n"+"\n" + "Translation:"+"  "+ trans + "  " +"\n"+"\n"+"\n"+ "Purport:"+"  "+ pur +"  "
    with open('C:/Users/DJPatil/Documents/Gita/Confusion.txt', 'w',  encoding='utf-8') as output:
              output.write(om)

Confusion()


def Envy():
    source=requests.get('https://vedabase.io/en/library/bg/16/19/',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')

    i=soup.find('div',id='bb3716',class_='r r-title r-verse')#Sloka
    sn = i.text
    print("  \n " + sn)

    print('***************************************************************')

    s=soup.find('div', id ="bb568435", class_='r r-devanagari')#Sanskrit
    sans=s.text
    print("  \n" + sans)

    print('***************************************************************')


    e=soup.find('div',id='bb3717',class_='r r-lang-en r-verse-text')#English
    eng=e.text
    print("  \n " + eng)


    print('***************************************************************')


    t=soup.find('div',id='bb3719',class_='r r-lang-en r-translation')#Translation
    trans=t.text
    print("  \n" +trans)


    print('***************************************************************')


    p=soup.find('div',id='bb3720',class_='r r-lang-en r-paragraph')#Purport
    pur=p.text
    print("  \n" + pur)


    print('***************************************************************')
    om = "BG Chapter.verse:"+sn+ "\n" +"Sanskrit:"+ sans +"  "+ "\n"+"\n"+"English:"+"  "+ eng + "  " +"\n"+"\n"+"\n" + "Translation:"+"  "+ trans + "  " +"\n"+"\n"+"\n"+ "Purport:"+"  "+ pur +"  "
    with open('C:/Users/DJPatil/Documents/Gita/Sinful.txt', 'w',  encoding='utf-8') as output:
              output.write(om)

Envy()


def Greed():
    source=requests.get('https://vedabase.io/en/library/bg/17/25/',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')

    i=soup.find('div',id='bb3872',class_='r r-title r-verse')#Sloka
    sn =i.text
    print("  \n " + sn)

    print('***************************************************************')

    s=soup.find('div', id ="bb568464", class_='r r-devanagari')#Sanskrit
    sans=s.text
    print("  \n" + sans)

    print('***************************************************************')


    e=soup.find('div',id='bb3873',class_='r r-lang-en r-verse-text')#English
    eng=e.text
    print("  \n " + eng)


    print('***************************************************************')


    t=soup.find('div',id='bb3875',class_='r r-lang-en r-translation')#Translation
    trans=t.text
    print("  \n" +trans)


    print('***************************************************************')


    p=soup.find('div',id='bb3876',class_='r r-lang-en r-paragraph')#Purport
    pur=p.text
    print("  \n" + pur)


    print('***************************************************************')
    om = "BG Chapter.verse:"+sn+ "\n" +"Sanskrit:"+ sans +"  "+ "\n"+"\n"+"English:"+"  "+ eng + "  " +"\n"+"\n"+"\n" + "Translation:"+"  "+ trans + "  " +"\n"+"\n"+"\n"+ "Purport:"+"  "+ pur +"  "
    with open('C:/Users/DJPatil/Documents/Gita/Forgive.txt', 'w',  encoding='utf-8') as output:
              output.write(om)
              
Greed()


def Peace():
    source=requests.get('https://vedabase.io/en/library/bg/8/28/',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')

    i=soup.find('div',id='bb2240',class_='r r-title r-verse')#Sloka
    sn =i.text
    print("  \n " + sn)

    print('***************************************************************')

    s=soup.find('div', id ="bb568207", class_='r r-devanagari')#Sanskrit
    sans=s.text
    print("  \n" + sans)

    print('***************************************************************')


    e=soup.find('div',id='bb2241',class_='r r-lang-en r-verse-text')#English
    eng=e.text
    print("  \n " + eng)


    print('***************************************************************')


    t=soup.find('div',id='bb2243',class_='r r-lang-en r-translation')#Translation
    trans=t.text
    print("  \n" +trans)


    print('***************************************************************')


    p=soup.find('div',id='bb2244',class_='r r-lang-en r-paragraph')#Purport
    pur=p.text
    print("  \n" + pur)


    print('***************************************************************')
    om = "BG Chapter.verse:"+sn+ "\n" +"Sanskrit:"+ sans +"  "+ "\n"+"\n"+"English:"+"  "+ eng + "  " +"\n"+"\n"+"\n" + "Translation:"+"  "+ trans + "  " +"\n"+"\n"+"\n"+ "Purport:"+"  "+ pur +"  "
    with open('C:/Users/DJPatil/Documents/Gita/Envy.txt', 'w',  encoding='utf-8') as output:
              output.write(om)

Peace()


def Demotivated():
    source=requests.get('https://vedabase.io/en/library/bg/11/33/',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')

    i=soup.find('div',id='bb2914',class_='r r-title r-verse')#Sloka
    sn =i.text
    print("  \n " + sn)

    print('***************************************************************')

    s=soup.find('div', id ="bb568312", class_='r r-devanagari')#Sanskrit
    sans=s.text
    print("  \n" + sans)

    print('***************************************************************')


    e=soup.find('div',id ='bb2915',class_='r r-lang-en r-verse-text')#English
    eng=e.text
    print("  \n " + eng)


    print('***************************************************************')


    t=soup.find('div',id='bb2917',class_='r r-lang-en r-translation')#Translation
    trans=t.text
    print("  \n" +trans)


    print('***************************************************************')


    p=soup.find('div',id='bb2918',class_='r r-lang-en r-paragraph')#Purport
    pur=p.text
    print("  \n" + pur)


    print('***************************************************************')
    om = "BG Chapter.verse:"+sn+ "\n" +"Sanskrit:"+ sans +"  "+ "\n"+"\n"+"English:"+"  "+ eng + "  " +"\n"+"\n"+"\n" + "Translation:"+"  "+ trans + "  " +"\n"+"\n"+"\n"+ "Purport:"+"  "+ pur +"  "
    with open('C:/Users/DJPatil/Documents/Gita/Forgetful.txt', 'w',  encoding='utf-8') as output:
              output.write(om)
Demotivated()


def Lazy():
    source=requests.get('https://vedabase.io/en/library/bg/18/39/',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')

    i=soup.find('div',id ='bb4083',class_='r r-title r-verse')#Sloka
    sn =i.text
    print("  \n " + sn)

    print('***************************************************************')

    s=soup.find('div', id ="bb568505", class_='r r-devanagari')#Sanskrit
    sans=s.text
    print("  \n" + sans)

    print('***************************************************************')


    e=soup.find('div', id='bb4084',class_='r r-lang-en r-verse-text')#English
    eng=e.text
    print("  \n " + eng)


    print('***************************************************************')


    t=soup.find('div',id='bb4086',class_='r r-lang-en r-translation')#Translation
    trans=t.text
    print("  \n" +trans)


    print('***************************************************************')


    p=soup.find('div',id='bb4087',class_='r r-lang-en r-paragraph')#Purport
    pur=p.text
    print("  \n" + pur)


    print('***************************************************************')
    om = "BG Chapter.verse:"+sn+ "\n" +"Sanskrit:"+ sans +"  "+ "\n"+"\n"+"English:"+"  "+ eng + "  " +"\n"+"\n"+"\n" + "Translation:"+"  "+ trans + "  " +"\n"+"\n"+"\n"+ "Purport:"+"  "+ pur +"  "
    with open('C:/Users/DJPatil/Documents/Gita/Pride.txt', 'w',  encoding='utf-8') as output:
              output.write(om)

Lazy()

def Depression():
    source=requests.get('https://vedabase.io/en/library/bg/5/21/',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')

    i=soup.find('div',id='bb1489',class_='r r-title r-verse')#Sloka
    sn =i.text
    print("  \n " + sn)

    print('***************************************************************')

    s=soup.find('div', id ="bb568100", class_='r r-devanagari')#Sanskrit
    sans=s.text
    print("  \n" + sans)

    print('***************************************************************')


    e=soup.find('div',id ='bb1490',class_='r r-lang-en r-verse-text')#English
    eng=e.text
    print("  \n " + eng)


    print('***************************************************************')


    t=soup.find('div',id ='bb1492',class_='r r-lang-en r-translation')#Translation
    trans=t.text
    print("  \n" +trans)


    print('***************************************************************')


    p=soup.find('div',id=('bb1493','bb1494','bb149'),class_='r r-lang-en r-paragraph')#Purport
    pur=p.text
    print("  \n" + pur)


    print('***************************************************************')
    om = "BG Chapter.verse:"+sn+ "\n" +"Sanskrit:"+ sans +"  "+ "\n"+"\n"+"English:"+"  "+ eng + "  " +"\n"+"\n"+"\n" + "Translation:"+"  "+ trans + "  " +"\n"+"\n"+"\n"+ "Purport:"+"  "+ pur +"  "
    with open('C:/Users/DJPatil/Documents/Gita/Pride.txt', 'w',  encoding='utf-8') as output:
              output.write(om)
Depression()


def Loneliness():
    source=requests.get('https://vedabase.io/en/library/bg/13/16/',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')

    i=soup.find('div',id ='bb3256',class_='r r-title r-verse')#Sloka
    sn =i.text
    print("  \n " + sn)

    print('***************************************************************')

    s=soup.find('div', id ="bb568359", class_='r r-devanagari')#Sanskrit
    sans=s.text
    print("  \n" + sans)

    print('***************************************************************')


    e=soup.find('div',id='bb3257',class_='r r-lang-en r-verse-text')#English
    eng=e.text
    print("  \n " + eng)


    print('***************************************************************')


    t=soup.find('div', id='bb3259',class_='r r-lang-en r-translation')#Translation
    trans=t.text
    print("  \n" +trans)


    print('***************************************************************')


    p=soup.find('div', id='bb3260',class_='r r-lang-en r-paragraph')#Purport
    pur=p.text
    print("  \n" + pur)


    print('***************************************************************')
    om = "BG Chapter.verse:"+sn+ "\n" +"Sanskrit:"+ sans +"  "+ "\n"+"\n"+"English:"+"  "+ eng + "  " +"\n"+"\n"+"\n" + "Translation:"+"  "+ trans + "  " +"\n"+"\n"+"\n"+ "Purport:"+"  "+ pur +"  "
    with open('C:/Users/DJPatil/Documents/Gita/Pride.txt', 'w',  encoding='utf-8') as output:
              output.write(om)

Loneliness()

def Mind():
    source=requests.get('https://vedabase.io/en/library/bg/6/26/',headers=headers).text
    soup=BeautifulSoup(source,'html.parser')

    i=soup.find('div',id='bb1695',class_='r r-title r-verse')#Sloka
    sn =i.text
    print("  \n " + sn)

    print('***************************************************************')

    s=soup.find('div', id ="bb568128", class_='r r-devanagari')#Sanskrit
    sans=s.text
    print("  \n" + sans)

    print('***************************************************************')


    e=soup.find('div',id = 'bb1696',class_='r r-lang-en r-verse-text')#English
    eng=e.text
    print("  \n " + eng)


    print('***************************************************************')


    t=soup.find('div', id='bb1698',class_='r r-lang-en r-translation')#Translation
    trans=t.text
    print("  \n" +trans)


    print('***************************************************************')


    p=soup.find('div',id='bb1699',class_='r r-lang-en r-paragraph')#Purport
    pur=p.text
    print("  \n" + pur)


    print('***************************************************************')
    om = "BG Chapter.verse:"+sn+ "\n" +"Sanskrit:"+ sans +"  "+ "\n"+"\n"+"English:"+"  "+ eng + "  " +"\n"+"\n"+"\n" + "Translation:"+"  "+ trans + "  " +"\n"+"\n"+"\n"+ "Purport:"+"  "+ pur +"  "
    with open('C:/Users/DJPatil/Documents/Gita/Pride.txt', 'w',  encoding='utf-8') as output:
              output.write(om)

Mind()


from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog as fd
import os
root = Tk()
root.title("GITA MINER")
root['bg'] = 'orange'
root.geometry("800x800")

w = Label(root, text ='Spiritual Solutions for your Material Problems', fg = "orange", font = "80")
w.pack()

frame = tk.LabelFrame(root,text ='*******Spiritual Solutions for your Material Problems*********',font ='250', fg='Brown',background='Yellow', padx=50, pady =30)
frame.place(height=850,width=750)
frame.configure(padx=50, pady=390)


#text = tk.Text(root, width = 10, height=12)
#text.grid(column=0, row=0, sticky='nsew')


def openf():
    # show the open file dialog
    f = fd.askopenfile('C:/Users/DJPatil/Documents/Gita/Anger.txt')
    # read the text file and show its content on the Text
    text.insert('1.0', f.readlines())

#img =Image.open("C:/Users/DJPatil/Pictures/BG.jpg")
#bg = ImageTk.PhotoImage(img)
#bottomframe = Frame(root)
#bottomframe.pack( side = BOTTOM )

b1_button = Button(frame,command = 'openf', text ="Anger" ,font='150', fg ="red", padx = 15, pady = 5).grid(row= 0,column=0,padx=20,pady=10)


b2_button = Button(frame, text ="Fear",font='150', fg ="brown", padx = 15, pady = 5).grid(row= 0,column=1,padx=20,pady=10)


b3_button = Button(frame, text ="Lust",font='150', fg ="blue", padx = 15, pady = 5).grid(row= 0,column=2,padx=20,pady=10)


b4_button = Button(frame, text ="Confusion",font='150', fg ="green", padx = 15, pady = 5).grid(row= 1,column=0,padx=20,pady=10)


b5_button = Button(frame, text ="Envy", font='150',fg ="green", padx = 15, pady = 10).grid(row= 1,column=1,padx=20,pady=10)


b6_button = Button(frame, text ="Greed", font='150',fg ="green", padx =15, pady = 10).grid(row= 1,column=2,padx=20,pady=10)


b7_button = Button(frame, text ="Seeking Peace",font='150', fg ="green", padx = 15, pady = 10).grid(row= 2,column=0,padx=20,pady=10)


b8_button = Button(frame, text ="Demotivated",font='150', fg ="green", padx = 15, pady = 10).grid(row= 2,column=1,padx=20,pady=10)


b9_button = Button(frame, text ="Laziness", font='150', fg ="green", padx = 15, pady = 10).grid(row= 2,column=2,padx=20,pady=10)


b10_button = Button(frame, text ="Depression",font='150', fg ="green", padx = 15, pady = 10).grid(row= 3,column=0,padx=20,pady=10)



b12_button = Button(frame, text ="Loneliness", font='150',fg ="green", padx = 15, pady = 10).grid(row= 3,column=1,padx=20,pady=10)



b13_button = Button(frame, text ="Uncontrolled Mind",font='150', fg ="green", padx = 15, pady = 10).grid(row= 3,column=2,padx=20,pady=10)

root.mainloop()

