import sys,os,time
def basix():
    os.system('pip install requests')
    time.sleep(1)
    os.system('pip install rich')
    time.sleep(1)
    os.system('pip install stdiomask')
    time.sleep(1)
    os.system('pip install colorama')
    time.sleep(1)
    os.system('pip install mechanize')
    time.sleep(1)
    os.system('pip install lolcat')
    time.sleep(1)
    os.system('pip install licensing')
    time.sleep(1)
    os.system('pip install pystyle')
    time.sleep(1)
    os.system('pip install bs4')

def form():
 note = """╔═╗╦  ╔═╗╔╗╔╔═╗╔╗╔╦ ╦
╠═╣║  ╠═╣║║║╠═╣║║║╚╦╝
╩ ╩╩═╝╩ ╩╝╚╝╩ ╩╝╚╝ ╩ 
   ┌─┐┌─┐┬ ┬┌─┐┌┬┐
┌─┘├┤ └┬┘├─┤ ││
└─┘└─┘ ┴ ┴ ┴─┴┘  ﻦﻴﻌﺑﺎﺘﻤﻟﺍ ﻞﻜﻟ ﺀﺍﺪﻫﺍ ﺕﺎﻴﺳﺎﺳﺍ ﺖﻴﺒﺜﺗ ﺓﺍﺩﺍ
ﻲﻧﺎﻨﻌﻟﺍ ﻭ ﻲﻧﺎﺒﻌﻟﺍ ﺩﺎﻳﺯ ﻪﻄﺳﺍﻮﺑ ﻩﺍﺩﻻﺍ ﻩﺬﻫ ﻞﻳﺪﻌﺗ ﻢﺗ\n \n """
 for letter in note:
    time.sleep(0.04)
    sys.stdout.write(letter)
    sys.stdout.flush()
def tele():
 os.system('am start https://t.me/Anany_1_hak')
error = "\033[1;31mERROR \033[1;30m"
ok = "\033[1;32m DONE \033[1;30m"
try:
    from licensing.models import *
    from licensing.methods import Key, Helpers
    print("Licensing "+ok)
except ImportError:
       print("Licesing "+error)
try:
    import bs4
    print('bs4'+ok)
except ModuleNotFoundError:
    print('bs4'+error)
try:
 import rich
 print("rich "+ok)
except ModuleNotFoundError:
    print("rich "+error)
try:
    import colorama
    print("COLORAMA "+ok)
except ModuleNotFoundError:
    print("Colorana "+error)
try:
    import pystyle
    print("PYSTYLE "+ok)
except ModuleNotFoundError:
    print("PYSTYLE "+error)
try:
    import requests
    print("REQUESTS "+ok)
except ModuleNotFoundError:
    print("REQUESTS "+error)
try:
    import stdiomask
    print("STDIOMASK "+ok)
except ModuleNotFoundError:
    print("STRDIOMASK "+error)
try:
    import requests
    import rich
    import pystyle
    import stdiomask
    import colorama
    import bs4
    print("ﻡﺎﻤﺗ ﻲﺷ ﻞﻛ ﺺﻗﺍﻮﻧ ﺪﺟﻮﻳ ﻻ")
    time.sleep(4)
    os.system('clear')
except ModuleNotFoundError:
    input("PRESS ENTER")
    basix()
def check():
    try:
        import rich
        import requests
        import colorama
        import stdiomask
        import pystyle
        import bs4
        print("1000000000000000000% ")
    except ModuleNotFoundError:
        print("ﻚﺑ ﻪﺻﺎﺨﻟﺍ ﺲﻜﻣﺮﻴﺗ ﻪﺨﺴﻧ ﻲﻓ ﻩﺬﻬﻓ ﻪﻠﻜﺸﻤﻟﺍ ﻞﺤﺗ ﻢﻟ ﺍﺫﺍ ﻩﺍﺩﻻﺍ ﻞﻴﻐﺸﺗ ﺪﻋﺍ ﻭ ﻪﻠﻜﺸﻤﻟﺍ ﺺﺤﻓ ﻪﻟﻭﺎﺤﻣ ﻢﺘﻴﺳ ﺎﻣ ﻪﻠﻜﺸﻣ ﻙﺎﻨﻫ")
        print("PRESS Y")
        time.sleep(1)
        os.system('clear')
        time.sleep(2)
        os.system("pkg upgrade")
        print("ﻪﻴﻠﺻﺍ ﺲﻜﻤﻳﺮﺗ ﻪﺨﺴﻧ ﻞﻳﺰﻨﺗ ﻚﻴﻠﻋ ﺐﺠﻴﻓ ﻪﻴﻠﻤﻌﻟﺍ ﺢﺠﻨﺗ ﻢﻟ ﺍﺫﺍ ﻩﺍﺩﻻﺍ ﻞﻴﻐﺸﺗ ﺪﻋﺍ")
        sys.exit()
def banner():

    form()
    print("[1] ﻞﻛﺎﺸﻣ ﻦﻣ ﺲﻜﻣﺮﻴﺘﻟﺍ ﺺﺤﻓ")
    print("[2] TELEGRAM ZEYAD ALABANY")
    print("[3] TELEGRAM ALANANY")
    zx = input("CHOOSE : ")
    if zx in ["1","01"]:
        check()
    if zx in ["02","2"]:
        os.system('am start https://t.me/srtly')
    if zx in ["03","3"]:
        os.system('am start https://t.me/Anany_1_hak')
    else:
        form()
        sys.exit()
banner()
