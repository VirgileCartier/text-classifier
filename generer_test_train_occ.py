import json
import nltk
from nltk.corpus import brown
import operator
import sys

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

# génération des 2000 mots les plus récurrents dans chaque document pour chaque genre :
def generation_modele_donnee(data):
	i=0
	instances = {}

	for cat in donnees[data]:
		
		i += 1

		sys.stdout.write("\r %s /%s)" %( i, len(donnees[data])))
		sys.stdout.flush()
		print("\n")
		
		j =0
		for text in donnees[data][cat]:
			wordsInText = brown.words(fileids=[text])
			
			instances[text] = [{},cat]
			
			j += 1
			
			sys.stdout.write("\r %s /%s) " %( j, len(donnees[data][cat]) ))
			sys.stdout.flush()
			print("\n")
			
			k=0

			wordsInText = list(set(wordsInText) & set(top2000w))
			
		
			for word in top2000w:
			
				k+=1
			
				sys.stdout.write("\r (%s) /%s))" %( k, len(top2000w)))
				sys.stdout.flush()
				
				if word in wordsInText:
					instances[text][0][word] = 1
				else:
					instances[text][0][word] = 0
	return instances
	
donnees = ouvrirjson("json/jsondata.json")

# mots les plus réccurents :
allWords = []
for cat in donnees['test']:
	for text in donnees['test'][cat]:
		for word in brown.words(fileids=[text]):
			allWords.append(word)

			
allWordsDist = nltk.FreqDist(w.lower() for w in allWords)

sorted_allWordsDist = sorted(allWordsDist.items(), key=operator.itemgetter(1)) #sorted permet d'avoir les mots classés de la même façon en train et test
top2000w = []

for w in sorted_allWordsDist[-2001:-1]:
	top2000w.append(w[0])


# construction des modèles de données : 
instances_test = generation_modele_donnee('test')
instances_train = generation_modele_donnee('train')

ecrirejson('json/instances_test_deuxkocc.json', instances_test)
ecrirejson('json/instances_train_deuxkocc.json', instances_train)