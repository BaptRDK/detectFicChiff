#! /usr/bin/python2.7
import sys
import math
import os
import calcEntFic

#02 novembre 9h

try:
        thresEnt = 7.999
	cible = str(sys.argv[1])
	seuil = int(sys.argv[2]) * 1000000
	ech = int(sys.argv[3]) * 1000000
        resultats = []
except:
	print "argument invalides"
        print "Usage: " + sys.argv[0] + " [path]directory min_size[Mo] N-first_Bytes_to_be_read[Mo]"
	sys.exit()
#Check the usage, 4 arguments are expected
if len(sys.argv) <> 4 or seuil <= 0:
	print "Usage: " + sys.argv[0] + " [path]directory min_size[Mo] N-first_Bytes_to_be_read[Mo]"
	sys.exit()
	
#check if the given directory exists
elif not os.path.isdir(cible):
	print "Le dossier " + cible + " n\'existe pas."
	sys.exit()

print "Detection de fichiers chiffres"
print "Exploration de " + cible
print "Seuls les fichiers de plus de " + str(seuil / 1000000) + " Mo seront testes"

print " Fichiers chiffres detectes: "
#for each file in the target and its sub directories
for path, dir, fic in os.walk(cible):
        #for each file
	for afic in fic:
            tmpPath = os.path.join(path, afic)
            if os.path.exists(tmpPath):
                ficInfo = os.stat(tmpPath)
                #if the file is bigger than our threshold (third argument)
                if (seuil) <= ficInfo.st_size:
                    #and if its entropy is greater than our decision threshold
                    if float(calcEntFic.calcEnt(str(tmpPath), ech)) > float(thresEnt):
                        #we add the file in our results array
                        resultats.append(tmpPath)
                        print str(tmpPath) + " " + str(calcEntFic.calcEnt(os.path.join(path, afic), ech))

if len(resultats) < 1:
    print "Aucun fichier detecte."
    sys.exit()

print str(len(resultats)) + " fichier(s) detecte(s).\nAffiner?"
choix = raw_input()
i = 1
thresEnt = 7.9999
#we ask if the user wants to sharpen the result in order to eliminate false positives
while str(choix.lower()) == "yes" or str(choix.lower()) == "y" or str(choix.lower()) == "oui" or str(choix.lower()) == "o":
    i = i + 1
    print "Fichier(s) detecte(s) a l'iteration " + str(i) + " :"
    for fic in resultats:
        if float(calcEntFic.calcEnt(fic, ech * int(i))) > float(thresEnt):
            print fic + " " + str(calcEntFic.calcEnt(fic, ech * int(i)))

    choix = raw_input("Affiner a nouveau ?")
    

print "Fin."


