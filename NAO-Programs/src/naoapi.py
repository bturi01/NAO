#!/usr/bin/python
#This is a NAO API reference for programming. Each of these functions will help in doing various actions. Putting this together should help create a program to enable the robot to move around, using its sensors to avoid obstacles.
from naoqi i
mport *
IP = '10.26.210.XX' #set your robot's IP here
PORT = 9559
speech = ALProxy("ALTextToSpeech", IP, PORT)
mp = ALProxy("ALMotion", IP, PORT)
b = ALProxy("ALBehaviorManager", IP, PORT)
mp.setStiffnesses('Body', 1)
sonar = ALProxy("ALSonar", IP, PORT)
sonar.subscribe("SonarTest", 500, 1.0)
mem=ALProxy('ALMemory', IP, PORT)
b.stopAllBehaviors()
speech.post.say("Standing Up")
b.runBehavior('standUp')
mp.setWalkArmsEnable(True,True)
sonarLeftDetected = mem.getData('SonarLeftDetected')
sonarRightDetected
= mem.getData('SonarRightDetected')
headMiddle =
mem.getData('Device/SubDeviceList/Head/Touch/Middle/Sensor/Value', 0)
leftBumper = mem.getData('LeftBumperPressed')
rightBumper = mem.getData('RightBumperPressed')
mp.setWalkTargetVelocity(-1,0,0,MAXSPEED)#back up
mp.setWalkTargetVelocity(1,0,0,MAXSPEED) #move forward
mp.setWalkTargetVelocity(0,0,1,MAXSPEED) #move left
mp.setWalkTargetVelocity(0,0,-1,MAXSPEED) #move right
mp.setWalkTargetVelocity(0,0,0,MAXSPEED) #stop
speech.post.say("Sitting Down")
b.runBehavior('sitDown')
mp.setStiffnesses('Body',0)
