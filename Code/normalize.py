import readCSV

def normalize_data(numberCritics, duration, directorFBLikes, actor3FBLikes,
    actor2FBLikes,actor1FBLikes, numberVotedUsers, castFBLikes, numberUserReviews,
    budget, imdbScore, movieFBLikes):                       #normalize the feature variables value
    numberCriticsM = max(numberCritics)             #finding max of column
    durationM = max(duration)                       #finding max of column
    directorFBLikesM = max(directorFBLikes)         #finding max of column 
    actor3FBLikesM = max(actor3FBLikes)                #finding max of column
    actor2FBLikesM = max(actor2FBLikes)             #finding max of column
    actor1FBLikesM = max(actor1FBLikes)             #finding max of column
    numberVotedUsersM = max(numberVotedUsers)       #finding max of column
    castFBLikesM = max(castFBLikes)                 #finding max of column
    numberUserReviewsM = max(numberUserReviews)         #finding max of column
    budgetM = max(budget)                       #finding max of column
    imdbScoreM = max(imdbScore)                 #finding max of column
    movieFBLikesM = max(movieFBLikes)               #finding max of column
    for i in range(0,5043):
        numberCritics[i] /= numberCriticsM          #normalize column
        duration[i] /= durationM                    #normalize column
        directorFBLikes[i] /= directorFBLikesM          #normalize column
        actor3FBLikes[i] /= actor3FBLikesM              #normalize column
        actor2FBLikes[i] /= actor2FBLikesM              #normalize column
        actor1FBLikes[i] /= actor1FBLikesM                  #normalize column
        numberVotedUsers[i] /= numberVotedUsersM                #normalize column
        castFBLikes[i] /= castFBLikesM                  #normalize column
        numberUserReviews[i] /= numberUserReviewsM          #normalize column
        budget[i] /= budgetM                            #normalize column
        imdbScore[i] /= imdbScoreM                      #normalize column
        movieFBLikes[i] /= movieFBLikesM            #normalize column