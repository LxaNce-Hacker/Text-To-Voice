# Import the Gtts module for text
# to speech conversion
#LxaNce👸🤴
from gtts import gTTS 

import sys
N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '√' + G + '] '
eror = R + '[' + W + '!' + R + ']'


banner = """
{}         _nnnn_{}        _________________
{}        dGGGGMMb{}      |                 |
{}       @p~qp~~qMb{}   ._| {} Text-To-voice  {}|
{}       M{}({}@{})({}@{}) {}M|{}  /  |_________________|
{}       @,{}----.{}JM|{}_/
{}      JS^{}\__/{}  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM    {}Coded by {}: {}Prince Katiyar
{}   FqM            MMMM    {}Github ID {}: {}github.com/LxaNce-Hacker
{} __|'\ .        |\{}dS qML
{} |    `.       | `' \{}Zq
{}_)      \.{}___.{},|     .'
\____   ){}MMMMMP{}|   .'
     `-'       `--'
""".format(D,W,D,W,D,W,Y,W,D,W,D,W,D,W,D,W,D,Y,D,W,D,Y,D,G,W,G,D,G,W,G,Y,D,Y,D,Y,D,Y,D,Y)

banner2 = """
   {}[{}1{}]{} English      {}[{}2{}]{} Hindi
""".format(G,W,G,W,G,W,G,W)

print banner
print banner2
# import Os module to start the audio file
import os 

#For Hindi
def hindi():
   try:
       C=2
        while(C!=1) :
            C=C+1
            a=input(ask + W + "Enter Anything "+ G + "> " + W)
            # Language to use 
            # language = input("For English Enter = en \nFor Hindi Enter = hi \nEnter : ")
            myobj = gTTS(text=a, lang=hi, slow=False) 
            myobj.save("output.mp3") 
            # Play the converted file 
            os.system("mpv output.mp3")
            #We can also use 'play' in place of mpv.
#For English
def english():
   try:
        C=2
        while(C!=1) :
            C=C+1
            a=input(ask + W + "Enter Anything "+ G + "> " + W)
            # Language to use 
            # language = input("For English Enter = en \nFor Hindi Enter = hi \nEnter : ")
            myobj = gTTS(text=a, lang=en, slow=False) 
            myobj.save("output.mp3") 
            # Play the converted file 
            os.system("mpv output.mp3")
            #We can also use 'play' in place of mpv.
            
# Choose language            
takok = raw_input(W + "Choose" + G + " > ")

if takok == "1" or takok == "01":
   english()
elif takok == "2" or takok == "02":
   hindi()
else:
   print (eror + " Wrong input")
