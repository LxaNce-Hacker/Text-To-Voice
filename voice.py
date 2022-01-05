# Import the Gtts module for text
# to speech conversion
#LxaNce👸🤴
from gtts import gTTS 

# import Os module to start the audio file
import os 
C=2
while(C!=1) :
    C=C+1
    a=input("Enter Anything : ")
    # Language we want to use 
    language = 'hi'
    myobj = gTTS(text=a, lang=language, slow=False) 
    myobj.save("output.mp3") 
    # Play the converted file 
    os.system("mpv output.mp3")
    #We use can also use 'play' in place of mpv.
