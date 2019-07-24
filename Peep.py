from collections import Counter
import pandas as pd
import seaborn as sns
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import matplotlib.pyplot as plt
from pathlib import Path

FOLDER_DATA = Path(r'C:\Users\vanes\Data')
data_set = open("Topicsemob.txt" , "w")


def barplot_df_words(df_words):

    fig, ax = plt.subplots(figsize=(7,10))
    g = sns.barplot(x='words', y='number', data=df_words)
    # for tick in ax.get_xticklables():
    #     tick.set_rotation(45)

    g.set_xticklabels(g.get_xticklabels(), rotation=45)

    plt.show()
    plt.interactive(False)
    name = 'fig_most_frequent_words.png'
    plt.savefig(FOLDER_DATA/name, dpi=300)



    return


path = r'C:\Users\vanes'

#data_set = "Welcome to the world of Geeks " \
          # "This portal has been created to provide well written well" \
           #"thought and well explained solutions for selected questions " \
           #"If you like Geeks for Geeks and would like to contribute " \
           #"here is your chance You can write article and mail your article " \
           #" to contribute at geeksforgeeks org See your article appearing on " \
           #"the Geeks for Geeks main page and help thousands of other Geeks. " \

# split() returns list of all the words in the string
list_words = data_set.split()

# define list with stopwords provided by nltk package
list_stopwords = set(stopwords.words('german'))


# list_words_no_stopwords = []
# for word in list_words:
#     if word not in list_stopwords:
#         list_words_no_stopwords.append(word)


list_words_no_stopwords = [word for word in list_words if word not in list_stopwords]
counter_words = Counter(list_words_no_stopwords)
# save data in dataframe for better visualisation
df_words = pd.DataFrame.from_dict(counter_words, orient='index', columns=['number'])
df_words.reset_index(inplace=True)
df_words.rename(columns={'index':'words'}, inplace=True)
# sort dataframe by occurance of words
df_words.sort_values(by='number', inplace=True, ascending=False)

file.close()

barplot_df_words(df_words)



# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(4)

print(most_occur)



