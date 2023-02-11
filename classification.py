import json
import operator
import sys
from sklearn.metrics import classification_report
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier

def ouvrirjson(chemin):
	f = open(chemin, encoding="utf-8")
	fic = json.load(f)
	f.close()
	return fic

def ecrirejson(chemin, contenu):
	w = open(chemin, "w", encoding="utf-8")
	w.write(json.dumps(contenu, indent=2, ensure_ascii=False))
	w.close()

# calcul du pourcentage pour calculer la précision
def Calcul_pourcentage(y_prediction, y_test):
	correct = 0
	for i in range(len(y_test)):
		if y_prediction[i] == y_test[i]:
			correct +=1
	return correct / len(y_test)

# genère les X et y Test et les X et y Train
def generate_X_Y_train_test(instances_train,instances_test,FIRST):
	X_test = []
	y_test = []
	X_train = []
	y_train = []

	orderedKeys = []

	b = True
	for instance in instances_train:

		xcode = []
		for word in instances_train[instance][0]:

			if b == True:
				orderedKeys.append(word)
				
			xcode.append(instances_train[instance][0][word])

		b = False

		X_train.append(xcode)
		y_train.append(instances_train[instance][1])


	for instance in instances_test:

		xcode = []

		for word in orderedKeys:

			xcode.append(instances_test[instance][0][word])

		X_test.append(xcode)
		y_test.append(instances_test[instance][1])

	return [X_train,X_test,y_train,y_test]

# Changer les json selon les caractéristiques que l'on veut utiliser : 
instances_train = 'json/instances_train-POStag.json'
instances_test = 'json/instances_test-POStag.json'

# Attention ! : ici aussi !
X_train,X_test,y_train,y_test = generate_X_Y_train_test(ouvrirjson('json/instances_train-POStag.json'),ouvrirjson('json/instances_test-POStag.json'), True)

print('\n voici les résultats avec le modèle donnée basé sur les caractéristiques nb_mots, etc. \n ') #à changer en fonction du json !!

# classification avec le bayésien naïf :
gnb = GaussianNB()
y_prediction1 = gnb.fit(X_train, y_train).predict(X_test)
precision = Calcul_pourcentage(y_prediction1, y_test)
target_names = ['news', 'science', 'literature']
print("La précision du modèle sur le set de test en naïve bayes est : " + str(precision) + " %")
print(classification_report(y_prediction1, y_test, target_names=target_names))
print(confusion_matrix(y_prediction1, y_test, labels=["news", "science", "literature"]))

# classification avec le perceptron multicouche :
mlpc = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
y_pred_v4 = mlpc.fit(X_train, y_train).predict(X_test)
precision = Calcul_pourcentage(y_pred_v4, y_test)
target_names = ['news', 'science', 'literature']
print("La précision du modèle sur le set de test avec le perceptron multicouche est : " + str(precision) + "%")
print(classification_report(y_pred_v4, y_test, target_names=target_names))
print(confusion_matrix(y_pred_v4, y_test, labels=["news", "science", "literature"]))

# classification avec l'arbre de décision :
dtree = tree.DecisionTreeClassifier()
y_pred1 = dtree.fit(X_train, y_train).predict(X_test)
precision = Calcul_pourcentage(y_pred1, y_test)
target_names = ['news', 'science', 'literature']
print("La précision du modèle sur le set de test avec l'arbre de décision est : " + str(precision) + "%")
print(classification_report(y_pred1, y_test, target_names=target_names))
print(confusion_matrix(y_pred1, y_test, labels=["news", "science", "literature"]))

# classification avec la forêt d’arbres décisionnels :
rforest = RandomForestClassifier(max_depth=2, random_state=0)
y_pred_v5 = rforest.fit(X_train, y_train).predict(X_test)
precision = Calcul_pourcentage(y_pred_v5, y_test)
target_names = ['news', 'science', 'literature']
print("La précision du modèle sur le set de test avec la forêt d’arbres décisionnels   est : " + str(precision) + "%")
print(classification_report(y_pred_v5, y_test, target_names=target_names))
print(confusion_matrix(y_pred_v5, y_test, labels=["news", "science", "literature"]))	

