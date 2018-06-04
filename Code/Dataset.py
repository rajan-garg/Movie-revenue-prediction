rowCount = 5043
colCount = 36
Data = [[0 for x in range(colCount)] for y in range(rowCount)]


def get_dataset(numberCritics, duration, directorFBLikes, actor3FBLikes,actor2FBLikes,actor1FBLikes,
    numberVotedUsers, castFBLikes, numberUserReviews,budget, imdbScore, movieFBLikes, action_type,
    adventure_type, fantasy_type,scifi_type,thriller_type, comedy_type, family_type, horror_type,
    war_type, animation_type, western_type, romance_type,musical_type,documentary_type,drama_type,
    history_type,biography_type,mystery_type,crime_type, general_type,parental_type,parentStrong_type,
    restrict_type,adults_type ):                            #creating the dataset matrix
    for i in range(0,rowCount):
        for j in range(0,colCount):
            if j==0:
                Data[i][j] = numberCritics[i]               #list item assigned as row element
            elif j==1:
                Data[i][j] = duration[i]                #list item assigned as row element
            elif j==2:
                Data[i][j] = directorFBLikes[i]         #list item assigned as row element
            elif j==3:
                Data[i][j] = actor3FBLikes[i]           #list item assigned as row element
            elif j==4:
                Data[i][j] = actor2FBLikes[i]           #list item assigned as row element
            elif j==5:
                Data[i][j] = actor1FBLikes[i]           #list item assigned as row element
            elif j==6:
                Data[i][j] = numberVotedUsers[i]            #list item assigned as row element
            elif j==7:
                Data[i][j] = castFBLikes[i]                 #list item assigned as row element
            elif j==8:
                Data[i][j] = numberUserReviews[i]           #list item assigned as row element
            elif j==9:
                Data[i][j] = budget[i]                      #list item assigned as row element
            elif j==10:
                Data[i][j] = imdbScore[i]                   #list item assigned as row element
            elif j==11:
                Data[i][j] = movieFBLikes[i]                #list item assigned as row element
            elif j==12:
                Data[i][j] = action_type[i]                 #list item assigned as row element
            elif j==13:
                Data[i][j] = adventure_type[i]              #list item assigned as row element
            elif j==14:
                Data[i][j] = fantasy_type[i]                #list item assigned as row element
            elif j==15:
                Data[i][j] = scifi_type[i]                  #list item assigned as row element
            elif j==16:
                Data[i][j] = thriller_type[i]               #list item assigned as row element
            elif j==17:
                Data[i][j] = comedy_type[i]                 #list item assigned as row element
            elif j==18:
                Data[i][j] = family_type[i]                 #list item assigned as row element
            elif j==19:
                Data[i][j] = horror_type[i]                 #list item assigned as row element
            elif j==20:
                Data[i][j] = war_type[i]                    #list item assigned as row element
            elif j==21:
                Data[i][j] = animation_type[i]              #list item assigned as row element
            elif j==22:
                Data[i][j] = western_type[i]                #list item assigned as row element
            elif j==23:
                Data[i][j] = romance_type[i]                #list item assigned as row element
            elif j==24:
                Data[i][j] = musical_type[i]                #list item assigned as row element
            elif j==25:
                Data[i][j] = documentary_type[i]                #list item assigned as row element
            elif j==26:
                Data[i][j] = drama_type[i]                #list item assigned as row element
            elif j==27:
                Data[i][j] = history_type[i]                #list item assigned as row element
            elif j==28:
                Data[i][j] = biography_type[i]                #list item assigned as row element
            elif j==29:
                Data[i][j] = mystery_type[i]                #list item assigned as row element
            elif j==30:
                Data[i][j] = crime_type[i]                #list item assigned as row element
            elif j==31:
                Data[i][j] = general_type[i]                #list item assigned as row element
            elif j==32:
                Data[i][j] = parental_type[i]                #list item assigned as row element
            elif j==33:
                Data[i][j] = parentStrong_type[i]                #list item assigned as row element
            elif j==34:
                Data[i][j] = restrict_type[i]                #list item assigned as row element
            elif j==35:
                Data[i][j] = adults_type[i]                #list item assigned as row element