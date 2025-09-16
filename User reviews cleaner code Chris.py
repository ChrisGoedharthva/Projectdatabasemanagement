# %%
import pandas as pd
import numpy as np
# to import the tools I need to clean the file

# %%
import pandas as pd
file_location = 'C:\\Users\\chris\\Downloads\\UserReviewsClean43LIWC.xlsx' #To define and show the location of the file
user = pd.read_excel(file_location) #Import the file

# %%
user = user.drop(columns=["dateP", "thumbsUp", "thumbsTot", "Analytic", "Clout", "Authentic", "Tone", "Sixltr", "Dic", 
                      "function", "ppron", "i",	"we", "you", "shehe", "they", "ipron", "article", "prep", "auxverb", 
                      "adverb", "conj", "negate", "verb", "adj", "compare", "interrog", "number", "quant", "affect", 
                      "family", "friend", "female", "male", "insight", "cause", "discrep", "tentat", "certain", "differ", 
                      "percept", "see", "hear", "feel", "bio", "body", "health", "sexual", "ingest", "drives", "affiliation", 
                      "achieve", "power", "focuspast", "focuspresent", "focusfuture",	"relativ", "motion", "space", "time", 
                      "work", "leisure", "home", "relig", "death", "informal", "swear", "netspeak", "assent", "nonflu", "filler", 
                      "AllPunc", "Period", "Comma", "Colon", "SemiC", "QMark", "Exclam", "Dash", "Quote", "Apostro", "Parenth", "OtherP"])
#Here I delete the colomns I don't need. The rest of the columns I need I got from the ERD


# %%
user.columns = [c.lower() for c in user.columns] #to normalize the column names
user = user.drop_duplicates() #to drop duplicates in the file, because somethimes the same review is twice in the file

# %%
user["movie name"] = user["url"].str.split("/").str[-1].str.replace("-", "", regex=False)
#This is to split the URL and take the last part of the URL (the movie name), and put the movie name into a new column called 'movie name'

# %%
user = user.dropna(thresh=3)
#Here it will drop the row if there are more then 3 missing values in the row. Because we want trustworthy data.

# %%
user = user.replace({'':np.nan}) #Replaces the empty values with NAN 

# %%
user = user[user["wc"] >= 5]                                   #Drops the reviews that have less than 5 words
user = user[~user["rev"].astype(str).str.match(r'^\d+$')]      #Drops the reviews that only have numbers in it

# %%
unique_movies = user["movie name"].dropna().unique()  #shows all the unique movies
movie_id_map = {name: i+1 for i, name in enumerate(sorted(unique_movies))}  #gives per unique movie an ID

user["movie_id"] = user["movie name"].map(movie_id_map) #will add a new column called 'movie-id'

# %%
user["user_id"] = user["reviewer"].astype(str).factorize()[0] + 1 #to create a user ID per unique user that left a review
user["reviewer"] = user["reviewer"].astype(str).str.replace("'", "", regex=False) #to remove the apostrophes in the reviewers names

# %%
output_file = 'C:\\Users\\chris\\Downloads\\UserReviewsCleanedfirst.xlsx'
user.to_excel(output_file, index=False)


