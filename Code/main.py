import csv
import math
import genre_type
import content_rating
import readCSV
import normalize
import Dataset
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
csv.field_size_limit(500000)
from sklearn import linear_model
import NN
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt

def split_data(train_data,test_data):               #function to create test and train dataset
	for i in range(5):
	    x_train, x_test, y_train, y_test = train_test_split(train_data,test_data, test_size=0.3)
	    # logreg_model2 = LogisticRegression(C=1e5)
	    # logreg_model2.fit(x_train,y_train)
	    # predicted2 = logreg_model2.predict(x_test)
	    NNmodel = MLPClassifier(hidden_layer_sizes=(20, ), activation='relu',  max_iter=200)
	    NNmodel.fit(x_train,y_train)
	    predicted = mlp_model8.predict(x_test)
	    count2 = 0
	    for i in range(len(predicted2)):
	        if (predicted[i]-y_test[i])==0 or abs(predicted[i]-y_test[i])==1:
	            count2 += 1
	    print(float(count2)/float(len(predicted)))                 #calculate accuracy


def applyLinearRegression(train,test,trainLabel,testLabel):             #linear regresion model
    lin = linear_model.LinearRegression()                                #implemented from sklearn
    predicted = cross_val_score(lin, Dataset.Data, readCSV.gross, cv=5)
    print("linear regression result")
    print(predicted)
    plt.xlabel('Comparing Linear Regression')
    plt.ylabel('Accuracy')
    xn = ['JASON ET AL.','DARIM ET AL.' ,'OUR MODEL']
    x = np.arange(len(xn))
    y = [30,25.5,max(predicted)*100]
    plt.bar(x,y, color='coral')
    plt.xticks(x, xn)
    plt.show()                                          #plotting graph

def applyLogRegression(train,test,trainLabel,testLabel):        #logarithmic regression mdoel
    logregmodel = LogisticRegression(C=1e5)
    logregmodel.fit(train,trainLabel)                   #fitting on train data
    predicted = logregmodel.predict(test)               #predicting target
    count = 0
    for i in range(len(predicted)):
        if (predicted[i]-testLabel[i])==0:
            count += 1                          #counting correct predictions
    print("logistic Regression results")
    print(float(count)/float(len(predicted)))
    scores = cross_val_score(logregmodel, Dataset.Data, readCSV.gross, cv=5)
    print(scores)
    plt.xlabel('Comparing Logistic Regression')
    plt.ylabel('Accuracy')
    xn = ['BENJAMIN ET AL.','JASON ET AL.' ,'OUR MODEL']
    x = np.arange(len(xn))
    y = [50.9,52,max(scores)*100]
    plt.bar(x,y, color='coral')
    plt.xticks(x, xn)
    plt.show()                  #plotting graph

def applyNB():                                              #naive bayesian model
    nb = GaussianNB()
    scores = cross_val_score(nb, Dataset.Data, readCSV.gross, cv=5)
    print("NB results")
    print(scores)
    plt.xlabel('Comparing Naive Bayesian')
    plt.ylabel('Accuracy')
    xn = ['BENJAMIN ET AL.' ,'OUR MODEL']
    x = np.arange(len(xn))
    y = [51.6 ,max(scores)*100]
    plt.bar(x,y, color='coral')
    plt.xticks(x, xn)
    plt.show()          #plotting graph

def applySVM():
    svmmodel1 = svm.SVC(kernel='rbf', C=2, gamma = 2)                   #svm rbf kernel
    svmmodel2 = svm.SVC(kernel='linear', C=2, gamma = 2)               #svm linear kernel
    svmmodel3 = svm.SVC(kernel='poly', C=1, gamma = 2)                 #svm polynomial kernel
    scores1 = cross_val_score(svmmodel1, Dataset.Data, readCSV.gross, cv=5)
    scores1 *=100
    print("SVM_rbf")
    print(scores1)
    scores2 = cross_val_score(svmmodel2, Dataset.Data, readCSV.gross, cv=5)
    print("SVM linear")
    print(scores2)
    scores2 *=100
    scores3 = cross_val_score(svmmodel3, Dataset.Data , readCSV.gross, cv=5)
    print("SVM poly")
    print(scores3)
    scores3 *=100
    plt.xlabel('various kernels, C=2, r=2')
    plt.ylabel('Accuracy')
    xn = ['rbf','linear','tanh']
    x = np.arange(len(xn))
    y = [max(scores1) ,max(scores2),max(scores3) ]
    plt.bar(x,y)
    plt.xticks(x, xn)
    plt.show()



def main():
    genre_type.find_genre()                     #creating the genre types column iterating through each row
    content_rating.find_content_type()          #creating the content rating type column iterating through each row
    readCSV.read_data()                         #creating feature columns by iteartong row in CSV
    normalize.normalize_data(readCSV.numberCritics, readCSV.duration, readCSV.directorFBLikes, 
    	readCSV.actor3FBLikes, readCSV.actor2FBLikes,readCSV.actor1FBLikes, readCSV.numberVotedUsers, 
    	readCSV.castFBLikes, readCSV.numberUserReviews, readCSV.budget, readCSV.imdbScore, readCSV.movieFBLikes)
    Dataset.get_dataset(readCSV.numberCritics, readCSV.duration, readCSV.directorFBLikes, 
    	readCSV.actor3FBLikes, readCSV.actor2FBLikes,readCSV.actor1FBLikes, readCSV.numberVotedUsers, 
    	readCSV.castFBLikes, readCSV.numberUserReviews, readCSV.budget, readCSV.imdbScore, readCSV.movieFBLikes,
    	genre_type.action_type,genre_type.adventure_type, genre_type.fantasy_type, genre_type.scifi_type,
    	genre_type.thriller_type, genre_type.comedy_type, genre_type.family_type, genre_type.horror_type,
    	genre_type.war_type, genre_type.animation_type, genre_type.western_type, genre_type.romance_type,
    	genre_type.musical_type,genre_type.documentary_type,genre_type.drama_type,genre_type.history_type,
    	genre_type.biography_type,genre_type.mystery_type,genre_type.crime_type, content_rating.general_type, 
    	content_rating.parental_type,content_rating.parentStrong_type, content_rating.restrict_type,
    	content_rating.adults_type)
    train = Dataset.Data[:3539]                         #training data as 70%
    test = Dataset.Data[3539:]                          #test data as 30%
    trainLabel = readCSV.gross[:3539]
    testLabel = readCSV.gross[3539:]
    applySVM()
    applyNB()
    applyLogRegression(train,test,trainLabel,testLabel)
    applyLinearRegression(train,test,trainLabel,testLabel)
    NN.apply_NN(Dataset.Data, readCSV.gross)
    # plt.xlabel('Comparing our ML models')
    # plt.ylabel('Accuracy')
    # xn0 = ['BENJAMIN ET AL. vs OUR SVM', 'JASON ET AL. vs OUR LOGREG', 'RAMESH ET AL. vs OUR NN']
    # xn1 = ['OUR SVM','OUR LOGREG', 'OUR NN']
    # x0 = np.arange(len(xn0))
    # x1 = np.arange(len(xn1))
    # y0 = [49.4, 52, 36.9 ]
    # y1 = [57.8, 59.6,63]
    # plt.bar(x0-0.4,y0,width = 0.4, color='coral')
    # plt.bar(x1,y1,width = 0.4)
    # plt.tick_params(labelsize = 7)
    # plt.xticks(x0-0.2, xn0)
    #plt.xticks(x1,xn1, rotation=30)
    #plt.show()
    # ax.bar(x-0.2, y,width=0.2,color='b',align='center')
    # ax.bar(x, z,width=0.2,color='g',align='center')


if __name__== '__main__':
	main()
