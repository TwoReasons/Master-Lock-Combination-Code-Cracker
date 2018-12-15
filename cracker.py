import time
import sys
import os
import re

print('              ( /      / /             ')
print('            (,.*.(    (.,,*(           ')
print('           ,**/          ,,**          ')
print('           ,,/            ,.,          ')
print('           *,(            /**          ')
print('           //(            (//          ')
print('           /((            (((          ')
print('           ,...(@@@&%@@@*...*          ')
print('         ,...@#@@@@@@@@@&&@...         ')
print('        .,,*@&@@@@@@@@@@@@%@*,,        ')
print('        ***@@@@@@@@@@@@@@@@%@***       ')
print('        //*%@@@@@@@@@@@@@@@@&,//       ')
print('        //.@@@@@&@@@@@@&@@@@@,//       ')
print('        (((@%@%@@@#@@#@@@/@#@(((       ')
print('         ###%#@@%@@@@@@%@@%*###        ')
print('          #%%%@&%@@@@@@%@%%%%(         ')
print('            #%%%%%.  .%%%%%(           ')
print('          ..,,*/%&&&&&&%*,,..          ')
print('                 .....                 ')

print('Master Lock Combination Finder')
print('')

print('Created by TwoReasons')

print('Step 1: Turn your lock around to where the back is facing you.')

print('Step 2: Find the code on the back.')

code = input("Please enter that code > ")

print ("Your number is",code,"correct?")

answer = input("y/n > ")

if answer == "y":
    print("Okay perfect, let us continue!!")
    time.sleep(1)
    print("finding your code...")
    codes = open("codes.txt", "r")

    for line in codes:
        if re.match(code, line):
            print("your code is > ", line)
        
    print("Once you've writen down your combination, press any key to exit...")
    input()
if answer =="n":
    print("Please restart the program. Press any key to exit...")
    input()
