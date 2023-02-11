import nltk
from nltk.corpus import brown
import random
import json

#Ce script permet un pré-traitement de nos données qui seront enregistrées dans un json

def ecrirejson(chemin, contenu):
	w = open(chemin, "w", encoding="utf-8")
	w.write(json.dumps(contenu, indent=2, ensure_ascii=False))
	w.close()

# séparation du corpus en train et test 
def train_test_distrubution(corpus):
	train = {}
	test = {}
	
	for category in corpus:
	
		cpt1 = 0 
		train[category] = []
		complete1 = False 
		randints = []
		
		while not complete1:
		
			newrand = False
			while  not newrand:
				randx = random.randint(0,len(corpus[category])-1)
				if randx not in randints:
					newrand = True
			
			
			
			if corpus[category][randx] not in train[category]:
				train[category].append(corpus[category][randx])
				cpt1 += 1
				
			
			if cpt1 > 0.8 * len(corpus[category]): # 80% de la taille du corpus pour le corpus d'entraînement
				complete1 = True 
	
	for category in corpus:
	
		test[category] = []
		
		for txt in corpus[category]:
		
			if txt not in train[category]:
				test[category].append(txt)
	
	return [train, test]
	

# Corpus classé par catégories		
themes = {}
themes["news"]= ["news", "reviews", "editorial"]
themes["science"]= ["learned"]
themes["literature"]= ["romance", "science_fiction", "fiction","mystery"]
corpus = {}

for category in themes:
	corpus[category] = brown.fileids(categories = themes[category])
	

crp_size = 0

for category in themes:
	crp_size += len(corpus[category])
	

# séparation corpus en test / train
val = train_test_distrubution(corpus)

traintest = {'train': val[0], 'test': val[1]}

# Json ouvert dans les solutions de traitement
ecrirejson('json/jsondata.json', traintest)