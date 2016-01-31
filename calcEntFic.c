//Jan 2016
//Baptiste
//
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "calcEntFic.h"

//calculate the entropy of the 'tailleEch' first byte of the 'fic' file
float calcEntFic(char* fic, int tailleEch)
{
	FILE* cible = NULL;
	double *ech = NULL;
	double freq[256] = {0};
	double ent = 0;
	int i;
	
	
	ech = malloc(tailleEch * sizeof(double));

	//if the allocation failed
	if ( ech == NULL )
	{
		fprintf(stderr, "Error while allocating memory");
		return(0);
	}
	
	//initialization of the array to 0
	for(i=0; i<tailleEch; i++)
	{
		ech[i] = 0;
	}
	
	//opening the file
	cible = fopen(fic, "rb");
	
	//if the opening failed
	if ( cible == NULL )
	{
		fprintf(stderr, "Error while opening: %s", fic);
		return(0);
	}

	//reading the 'tailleEch' firt byte of the file
	for (i=0; i< tailleEch; i++)
	{
		ech[i] = (double)fgetc(cible);
	}

	//closing the file
	fclose(cible);

	//counting the number of appearence of each value for a byte (0 to 255)
	for (i=0; i<tailleEch; i++)
	{
		freq[(int)ech[i]] += 1;
	}

	//for each value of a byte
	for (i=0; i< 256; i++)
	{
		//if it appears at least once
		if (freq[i] > 0)
		{
			//calculate the frequency of apparition
			freq[i] = freq[i] / tailleEch;

			//and then adding it to the entropy calculation
			ent += freq[i] * log2f(freq[i]);
		}
	}
	
	//finishing the entropy calculation	
	ent = -ent;

	//freeing the array
	free(ech);

	//returning the entropy of the sample
	return(ent);
}
