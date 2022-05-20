import os
import time
os.system('cls')
while(True):
    print('-------------------------------SRB-----------------------------------'.center(50))
    print('1. Show Hotspot Status\n2. Start Hotspot\n3. Stop Hotspot and Exit\n')
    c = int(input('Enter Your Choice- '))
    os.system('cls')
    if c==1:
        print('------------------------------------------------------------------'.center(50))
        os.system('netsh wlan show hostednetwork')
        time.sleep(1)
    elif c==2:
        print('------------------------------------------------------------------'.center(50))
        os.system('netsh wlan start hostednetwork')
        os.system('netsh wlan show hostednetwork')
        time.sleep(1)
    elif c==3:
        print('------------------------------------------------------------------'.center(50))
        os.system('netsh wlan stop hostednetwork')
        time.sleep(1)
        print('------------------------------------------------------------------'.center(50))
        exit()
    else:
        print('Enter Correct Choice')