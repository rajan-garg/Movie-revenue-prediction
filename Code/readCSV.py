import csv
import math
import matplotlib.pyplot as plt

numberCritics = []
duration =[]
directorFBLikes = []                #feature variable
actor3FBLikes = []                  #feature variable
actor2FBLikes = []              #feature variable
actor1FBLikes = []              #feature variable
numberVotedUsers = []           #feature variable
castFBLikes = []                #feature variable
numberUserReviews = []          #feature variable
language = []                   #feature variable
country = []                    #feature variable
budget = []                     #feature variable
imdbScore = []                  #feature variable
movieFBLikes = []               #feature variable
gross = []                      #feature variable


def read_data():                                            #creating feature columns by iteartong row in CSV
    with open("movie_metadata.csv", "r") as sentences_file:
        reader = csv.reader(sentences_file, delimiter=',')
        reader.next()
        # i = 1
        # y = []
        # x = []
        # for i in  range(1,5044):
        #     x.append(i)
        
        for row in reader:
            numberCritics.append(float(row[2]))
            duration.append(float(row[3]))
            directorFBLikes.append(float(row[4]))
            actor3FBLikes.append(float(row[5]))
            actor2FBLikes.append(float(row[24]))
            actor1FBLikes.append(float(row[7]))
            castFBLikes.append(float(row[13]))
            #y.append(int(row[8]))
            if int(row[8])>0:
                gross.append(int(math.log(float(row[8]))/math.log(10.0)))       #taking the logarithm of revenue value
            else:
                gross.append(0)
            numberVotedUsers.append(float(row[12]))
            numberUserReviews.append(float(row[18]))
            if row[19] == 'English':
                language.append(1.0)
            else:
                language.append(0.0)
            if row[20] == 'USA':
                country.append(1.0)
            else:
                country.append(0.0)
            budget.append(float(row[22]))            
            imdbScore.append(float(row[25]))
            movieFBLikes.append(float(row[27]))

        # y.sort()
        # plt.xlabel('Movies')
        # plt.ylabel('Revenue in 100 millions')
        # plt.plot(x,y)
        # plt.show()
