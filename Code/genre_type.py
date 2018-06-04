import csv

action_type = [0 for x in range(5043)]              #genre type
adventure_type = [0 for x in range(5043)]           #genre type
fantasy_type = [0 for x in range(5043)]             #genre type
scifi_type = [0 for x in range(5043)]               #genre type
thriller_type = [0 for x in range(5043)]            #genre type
comedy_type = [0 for x in range(5043)]              #genre type
family_type = [0 for x in range(5043)]              #genre type
horror_type = [0 for x in range(5043)]              #genre type
war_type = [0 for x in range(5043)]                 #genre type
animation_type = [0 for x in range(5043)]           #genre type
western_type = [0 for x in range(5043)]             #genre type
romance_type = [0 for x in range(5043)]             #genre type
musical_type = [0 for x in range(5043)]             #genre type
documentary_type = [0 for x in range(5043)]         #genre type
drama_type = [0 for x in range(5043)]               #genre type
history_type = [0 for x in range(5043)]             #genre type
biography_type = [0 for x in range(5043)]           #genre type
mystery_type = [0 for x in range(5043)]             #genre type
crime_type = [0 for x in range(5043)]               #genre type

def find_genre():                                   #creatig the column iterating through each row
    with open("movie_metadata.csv", "r") as sentences_file:
        reader = csv.reader(sentences_file, delimiter=',')
        reader.next()
        i = 0
        for row in reader:
            genre_type = ""
            genre_type = str(row[9])
            if 'Action' in genre_type:
                action_type[i] = 1
            if 'Adventure' in genre_type:
                adventure_type[i] = 1
            if 'Fantasy' in genre_type:
                fantasy_type[i] = 1
            if 'Sci-Fi' in genre_type:
                scifi_type[i] = 1
            if 'Thriller' in genre_type:
                thriller_type[i] = 1
            if 'Comedy' in genre_type:
                comedy_type[i] = 1
            if 'Family' in genre_type:
                family_type[i] = 1
            if 'Horror' in genre_type:
                horror_type[i] = 1
            if 'War' in genre_type:
                war_type[i] = 1
            if 'Animation' in genre_type:
                animation_type[i] = 1
            if 'Western' in genre_type:
                western_type[i] = 1
            if 'Romance' in genre_type:
                romance_type[i] = 1
            if 'Musical' in genre_type:
                musical_type[i] = 1
            if 'Documentary' in genre_type:
                documentary_type[i] = 1
            if 'Drama' in genre_type:
                drama_type[i] = 1
            if 'History' in genre_type:
                history_type[i] = 1
            if 'Biography' in genre_type:
                biography_type[i] = 1
            if 'Mystery' in genre_type:
                mystery_type[i] = 1
            if 'Crime' in genre_type:
                crime_type[i] = 1
            i+=1