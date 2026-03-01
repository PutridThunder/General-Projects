import os #clearing the terminal
import time #keeping track of time elapsed and to time how long each tree itteration remains on screen for
import pygame #how we are going to play the music
import random #randomise character colours
from termcolor import colored #how we are going to colour the text

pygame.mixer.init() #initialises the mixer, prep for audio
pygame.mixer.music.load("Wham! - Last Christmas (Official Video) 4.mp3") #loads the music, ready to play
pygame.mixer.music.play() #plays the music, will continue to play as long as code is still running

colours = [
    colored("*","red",attrs=["bold"]),
    colored("*","cyan",attrs=["bold"]),
    colored("*","white",attrs=["bold"]),
    colored("*","green",attrs=["bold"]),
    colored("*","magenta",attrs=["bold"]),
    colored("*","yellow",attrs=["bold"]),
    ] #random colours for tree

Tree = [
"             *",
"            ***",
"           *****",
"          *******",
"         *********",
"        ***********",
"       *************",
"      ***************",
"            | |"
] #tree array

Lyrics =[
    "Last Christmas I gave you my heart...",
    "But the very next day you gave it away...",
    "This year to save me from tears",
    "I'll give it to someone special",
    "Last Christmas I gave you my heart",
    "But the very next day you gave it away",
    "This year to save me from tears",
    "I'll give it to someone special",

    "Last Christmas I gave you my heart...",
    "But the very next day you gave it away...",
    "This year to save me from tears",
    "I'll give it to someone special",
] #lyrics array

currentlyric ="" #remembers what lyric we are on to reprint when everything dissapears

starttime = time.time() #time code starts

TS =[18, 22, 27, 31] #timestamps,when to play lyrics index (18 maps to Lyrics[0], 22 to Lyrics[1], etx)

printed = [False] * len(TS) #array as long as TS

duration =34 #how long the code will play for

while True:
    elapsedtime = time.time() - starttime #elapsed time since starting the code
    
    for L,S in enumerate(TS): #L is the index, S is the value of the index in TS
        if elapsedtime >= S and not printed[L]:
            currentlyric = Lyrics[L]
            printed[L] = True

    chance = 1 #chance for each green leaf to turn into a bulb colour, out of 0-1

    for i,section in enumerate(Tree): #i is the index, section is the string of that index in tree
        newsection =""
        for char in section:
            if char =="*": #skip whitespace only focus on the leaves
                if random.random() < chance:
                    newsection +=random.choice(colours) #if it wins the lottery, it turns into a lightbulb
            elif char =="|":
                newsection +=colored("|","red", attrs=["dark"])
            else:
                newsection +=char

        if i == 3:
            print(f"{newsection}    {colored(currentlyric,"cyan", attrs=["bold"])}")
        else:
            print(newsection)

    time.sleep(0.5) #without this, the tree will keep changing instantly
    os.system("cls") #clears the terminal so we dont have multiple trees playing continuously
    
    if elapsedtime >= duration:

        break
      
