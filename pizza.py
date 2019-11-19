#!/bin/bash

import random

activity = ["Playing backgammon","Carving a turkey","Smashing avocados","Tossing a salad","Polishing the bishop","Pressing my pants","Decanting a fine malbec","Shooting a pigeon","Stalking a grouse",
"Battering a mars bar","Cleaning the gutter","Washing the dishes","Playing bridge","Getting brexit done"]

location = ["Pho","Wetherspoons","Pret-a-manger","Greggs","Tesco Express","Aldi","Lidl","Franco Manca","Nandos","Cafe Nero","Starbucks","Tk Maxx","Tesco Metro","William Hill"]

print ("It couldn't of been me I was %s at %s" % (random.choice(activity), random.choice(location)))
