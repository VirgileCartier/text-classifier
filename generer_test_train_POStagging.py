import json
import nltk
from nltk.corpus import brown
import operator
import sys
from collections import OrderedDict
import collections

# json généré dans genere_jsondata.py
def ouvrirjson(chemin):
	f = open(chemin, encoding="utf-8")
	toto = json.load(f)
	f.close()
	return toto

def ecrirejson(chemin, contenu):
	w = open(chemin, "w", encoding="utf-8")
	w.write(json.dumps(contenu, indent=2, ensure_ascii=False))
	w.close()

# compte des TAG
def generateModel(data):
	instances = {}

	for cat in corpus[data]:
		for text in corpus[data][cat]:

			instances[text] = [{},cat]

			tags1 = brown.tagged_words(fileids=[text])
			alltags = []

			try:
				for tag in allTagsSorted:
					instances[text][0][tag] = 0

				for tag in tags1:
					instances[text][0][tag[1]]+=1
			except:
				continue

	return instances

corpus = ouvrirjson('json/jsondata.json')
posTags= {}

# Compte des TAG et classification selon la fréquence d'occurences 
for cat in corpus['train']:
	for text in corpus['train'][cat]:
		tags1 = brown.tagged_words(fileids=[text])

		for couples in tags1:

			if couples[1] not in posTags:
				posTags[couples[1]] = 0
			else:
				posTags[couples[1]] += 1

#Sorted permet d'avoir les mots classés de la même façon
sorted_posTags = sorted(posTags.items(), key=operator.itemgetter(1))
print(sorted_posTags)

allTagsSorted= []

for tag in sorted_posTags:
	allTagsSorted.append(tag[0])

ecrirejson('json/instances_train-POStag.json' , generateModel('train'))
ecrirejson('json/instances_test-POStag.json' , generateModel('test'))



















		