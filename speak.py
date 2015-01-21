
from naoqi import ALProxy #imports to get the NAO library
tts = ALProxy("ALTextToSpeech","<IP of robot>", 9559) #initialize text to speech
tts.say("Hellow World!") #method to make NAO speak

