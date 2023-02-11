# Classifieur de texte via la librairie ScikitLearn codé en Python

## run python generer_jsondata.py dans le terminal :
- crée un jeu de données json de pré-traitement à partir du corpus Brown (importé directement dans le code)

## run python generer_test_train_Caracs.py dans le terminal :
- crée un jeu de données json des caractéristiques textométriques du corpus séparé dans un corpus d'entraînement et de test

## run python generer_test_train_occ.py dans le terminal :
- crée un jeu de données json des 2000 mots les plus occurents selon les catégories séparé dans un corpus d'entraînement et de test

## run python genrer_test_train_POSTagging.py :
- crée un jeu de données json à partir des POStagging du corpus Brown, séparé dans un corpus d'entraînement et de test

## classification.py : 
classification des textes test avec plusieurs méthodes : Bayésien naïf, perceptron multicouche, arbre de décision, forêts d'arbre décisionnels