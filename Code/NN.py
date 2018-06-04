from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import numpy as np

def apply_NN(totalMatrix, gross):
	NNmodel = MLPClassifier(hidden_layer_sizes=(15, ), activation='identity',  max_iter=200)		#NN with 15 layers
	scores1 = cross_val_score(NNmodel, totalMatrix, gross, cv=5)
	print(scores1)
	NNmodel2 = MLPClassifier(hidden_layer_sizes=(15, ), activation='logistic',  max_iter=200)		#NN with 15 layers
	scores2 = cross_val_score(NNmodel2, totalMatrix, gross, cv=5)
	print(scores2)
	NNmodel3 = MLPClassifier(hidden_layer_sizes=(15, ), activation='tanh',  max_iter=200)			#NN with 15 layers
	scores3 = cross_val_score(NNmodel3, totalMatrix, gross, cv=5)
	print(scores3)
	NNmodel4 = MLPClassifier(hidden_layer_sizes=(15, ), activation='relu',  max_iter=200)			#NN with 15 layers
	scores4 = cross_val_score(NNmodel4, totalMatrix, gross, cv=5)
	print(scores4)
	plt.xlabel('Activation functions for NN with h=15')
	plt.ylabel('Accuracy')
	xn = ['identity', 'logistic','tanh','relu']
	x = np.arange(len(xn))
	y = [max(scores1)*100 ,max(scores2)*100,max(scores3)*100, max(scores4)*100 ]		#graph for 15 layers
	plt.bar(x,y)
	plt.xticks(x, xn)
	plt.show()
	NNmodel5 = MLPClassifier(hidden_layer_sizes=(20, ), activation='identity',  max_iter=200)		#NN with 20 layers
	scores5 = cross_val_score(NNmodel5, totalMatrix, gross, cv=5)
	print(scores5)
	NNmodel6 = MLPClassifier(hidden_layer_sizes=(20, ), activation='logistic',  max_iter=200)		#NN with 20 layers
	scores6 = cross_val_score(NNmodel6, totalMatrix, gross, cv=5)
	print(scores6)
	NNmodel7 = MLPClassifier(hidden_layer_sizes=(20, ), activation='tanh',  max_iter=200)			#NN with 20 layers
	scores7 = cross_val_score(NNmodel7, totalMatrix, gross, cv=5)
	print(scores7)
	NNmodel8 = MLPClassifier(hidden_layer_sizes=(20, ), activation='relu',  max_iter=200)			#NN with 20 layers
	scores8 = cross_val_score(NNmodel8, totalMatrix, gross, cv=5)
	print(scores8)
	plt.xlabel('Activation functions for NN with h=20')
	plt.ylabel('Accuracy')
	xn = ['identity', 'logistic','tanh','relu']
	x = np.arange(len(xn))
	y = [max(scores5)*100 ,max(scores6)*100,max(scores7)*100, max(scores8)*100 ]
	plt.bar(x,y)
	plt.xticks(x, xn)
	plt.show()																#graph with 20 layers
	
# ax.bar(x-0.2, y,width=0.2,color='b',align='center')
# ax.bar(x, z,width=0.2,color='g',align='center')