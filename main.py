import pyttsx3


#  Program initiation
engine = pyttsx3.init()


rate = engine.getProperty('rate')

engine.setProperty('rate', 200)  # setting up new voice rate

# pyttsx3.speak("At the speed of 200")
print (rate)


volume = engine.getProperty('volume')
print (volume)

engine.setProperty('volume', 0.8)

