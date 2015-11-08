#! /usr/bin/python2.7
import sys
import math

def calcEnt(file, tailleEch):
	
	# read the whole file into a byte array
	f = open(file, "rb")
	byteArr = map(ord, f.read(int(tailleEch)))
	f.close()


	fileSize = len(byteArr)
	
	#create an array to store each byte (0-255) frequency
	freqTab= [0]*256

	#count each appearance of every byte in the file
	for byte in byteArr:
		freqTab[byte] += 1

	#calculate frequency fron count
	for i in range(0, len(freqTab)):
		freqTab[i] = float(freqTab[i]) / fileSize

	#calculate Shannon entropy
	ent = 0.0

	for freq in freqTab:
	    if freq > 0:
        	ent += freq * math.log(freq, 2)
	ent = -ent
	
	return ent
