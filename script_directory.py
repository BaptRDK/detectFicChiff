#! /usr/bin/python2.7
import sys
import math
import os 

#encrypted = False
#mettre en deuxieme parametre sys.argv[2] la taille min pour restreindre la boucle d'iteration 

if len(sys.argv) != 4:
    print "Usage: script_directory_new.py [path]directory min_size[MO] N-first_Bytes_to_be_read"
    sys.exit()

print 'taille minimum des fichiers a tester :', sys.argv[2], 'Mo'
print 'Recherche de fichiers chiffres...'
n = 1


for dirname, dirnames, filenames in os.walk(sys.argv[1]):
    for filename in filenames:
	entropies = []
	fileSizes = []
	sizeFilter = sys.arg[2] * 1000000
	statinfo = os.stat(filename)
	i = 0
	j = 0

	if os.path.isfile(filename):
		if int(sizeFilter) <= statinfo.st_size: 
			#print 'le fichier', filename, 'est de taille :', statinfo.st_size
			f = open(filename, "rb")
			byteArr = map(ord, f.read(int(sys.argv[3])))
			f.close()
			fileSizes.append(len(byteArr))
		#if fileSize
			#print 'fileSize :', fileSizes[0]
			j+=1

			freqList = []
			for b in range(256):
			    ctr = 0
			    for byte in byteArr:
				if byte == b:
				    ctr += 1
				    #print ctr
			    freqList.append(float(ctr) / fileSizes[i])


			# Shannon entropy
			ent = 0.0
			for freq in freqList:
			    if freq > 0:
				ent = ent + freq * math.log(freq, 2)
			entropies.append(-ent)
			#print 'Shannon entropy (min bits per byte-character):'
			#print filename 
			#print entropies[i]
			if entropies[i] > 7:
				print 'fichier chiffre', n,':', filename
				encrypted = True 
				n=n+1
			else:
				encrypted = False 
			i+=1


#if encrypted == False:
#	print 'il n\'y a pas de fichier chiffre'
#print entropies(2)

