import json
from nltk.corpus import brown
import statistics
import io

def ouvrirjson(chemin):
	f = open(chemin, encoding="utf−8")
	fic = json.load(f)
	f.close()
	return fic

def ecrirejson(chemin, contenu):
	w = open(chemin, "w", encoding="utf-8")
	w.write(json.dumps(contenu, indent=2, ensure_ascii=False))
	w.close()

# json généré dans genere_jsondata.py
donnees = ouvrirjson("json/jsondata.json")

# caractéristiques simples, taille min, max, moyenne mot, nombre phrase, taille min, max, moyenne etc...
def get_basic_caracteristics(liste_items):
    L = [len(liste_items)]
    len_items = [len(item) for item in liste_items] 
    L.append(min(len_items))
    L.append(max(len_items)) 
    L.append(statistics.mean(len_items))
    return L

for sub_corpus, sub_corpus_files in donnees.items(): 

	if sub_corpus == 'test': #changer test / train pour générer les json de test / train

		instance = {}

		for classe, liste_IDS in sub_corpus_files.items():
			
			for file_ID in liste_IDS: 
				print(file_ID)
				carac = []
				instance[file_ID] = [{"NB_mots" : 0, "Taille_min_mots":0, "Taille_max_mots": 0, "Taille_moy_mots":0, "NB_phrs" : 0, "Taille_min_phrs" : 0, "Taille_max_phrs" : 0 , "Taille_moy_phrs" : 0},classe]  
				mots = brown.words(file_ID)
				carac += get_basic_caracteristics(mots) 
				phrases = brown.sents(file_ID)
				carac += get_basic_caracteristics(phrases)

				instance[file_ID][0]['NB_mots'] = carac[0]
				instance[file_ID][0]['Taille_min_mots'] = carac[1]
				instance[file_ID][0]['Taille_max_mots'] = carac[2]
				instance[file_ID][0]['Taille_moy_mots'] = carac[3]
				instance[file_ID][0]['NB_phrs'] = carac[4]
				instance[file_ID][0]['Taille_min_phrs'] = carac[5]
				instance[file_ID][0]['Taille_max_phrs'] = carac[6]
				instance[file_ID][0]['Taille_moy_phrs'] = carac[7]

ecrirejson('json/instances_caracs_test.json', instance) # changer test / train pour générer les json de test / train


  


	       
	           


