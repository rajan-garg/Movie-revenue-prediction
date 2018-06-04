import csv

general_type = [0 for x in range(5043)]             #content type
parental_type = [0 for x in range(5043)]            #content type
parentStrong_type = [0 for x in range(5043)]        #content type
restrict_type = [0 for x in range(5043)]            #content type
adults_type = [0 for x in range(5043)]              #content type

def find_content_type():                            #creating the content rating type column iterating through each row
    with open("movie_metadata.csv", "r") as sentences_file:
        reader = csv.reader(sentences_file, delimiter=',')
        reader.next()
        i = 0
        for row in reader:
            content_rating = ""
            content_rating = str(row[21])
            if 'G' in content_rating:
                general_type[i] = 1
            if 'PG' in content_rating:
                parental_type[i] = 1
            if 'PG-13' in content_rating:
                parentStrong_type[i] = 1
            if 'R' in content_rating:
                restrict_type[i] = 1
            if 'NC-17' in content_rating:
                adults_type[i] = 1
            i+=1