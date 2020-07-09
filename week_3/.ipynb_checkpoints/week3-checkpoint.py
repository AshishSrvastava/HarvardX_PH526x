#3.2: LANGUAGE PROCESSING

#small test string, to see whether the function works or not
text = "This is my test text. We're keeping this text short to keep things manageable."

def count_words(text):
    '''
    Counts the number of times each word occurs in the text (str). Returns dictionary where keys are
    unique words and values are word counts. Skip punctuation. 
    '''
    
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"', "!", "?"]
    for ch in skips:
        text = text.replace(ch, "")

    word_counts= {}
    #break down the text into words
    for word in text.split(' '):
        # known word: increase the counter for that word
        if word in word_counts:
            word_counts[word] += 1
        # unknown word: establish the entry and initialize the counter
        else: 
            word_counts[word] = 1
    return word_counts


# using counter instead
from collections import Counter
def count_words_fast(text):
    '''
    Counts the number of times each word occurs in the text (str). Returns dictionary where keys are
    unique words and values are word counts. Skip punctuation. 
    '''
    
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"', "!", "?"]
    for ch in skips:
        text = text.replace(ch, "")

    word_counts = Counter(text.split(' '))
    return word_counts


def read_book(title_path):
    '''
    The function will read a book and return it as a string 
    '''
    with open(title_path, 'r', encoding='utf8') as current_file:
        text = current_file.read()
        text = text.replace('\n','').replace('\r','')
    return text

ind = text.find("What's in a name")
ind
# 42757

sample_text = text[ind : ind+1000]
sample_text
#"What's in a name? That which we call a rose    By any other name would smell as sweet.    So Romeo would, were he not Romeo call'd,    Retain that dear perfection which he owes    Without that title. Romeo, doff thy name;    And for that name, which is no part of thee,    Take all myself.  Rom. I take thee at thy word.    Call me but love, and I'll be new baptiz'd;    Henceforth I never will be Romeo.  Jul. What man art thou that, thus bescreen'd in night,    So stumblest on my counsel?  Rom. By a name    I know not how to tell thee who I am.    My name, dear saint, is hateful to myself,    Because it is an enemy to thee.    Had I it written, I would tear the word.  Jul. My ears have yet not drunk a hundred words    Of that tongue's utterance, yet I know the sound.    Art thou not Romeo, and a Montague?  Rom. Neither, fair saint, if either thee dislike.  Jul. How cam'st thou hither, tell me, and wherefore?    The orchard walls are high and hard to climb,    And the place death, conside"

#find the # of unique words, and the frequency of words in a given book
def word_stats(word_counts):
    '''Return number of unique words and word frequencies'''
    #count the number of unique words
    num_unique = len(word_counts)
    #word counts (frequencies) for each unique word
    counts = word_counts.values()
    return (num_unique, counts)

#English
text = read_book('/Users/ashishsrivastava/Desktop/Central/Python/HarvardX_PH526x/week_3/python_case_studies/language_processing/Books/English/shakespeare/Romeo and Juliet.txt')   
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)
print(num_unique, sum(counts))
#German
text = read_book('/Users/ashishsrivastava/Desktop/Central/Python/HarvardX_PH526x/week_3/python_case_studies/language_processing/Books/German/shakespeare/Romeo und Julia.txt')   
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)
print(num_unique, sum(counts))


#read all books in all subdirectories of the book folder
import os
book_dir = '/Users/ashishsrivastava/Desktop/Central/Python/HarvardX_PH526x/week_3/python_case_studies/language_processing/Books'
os.listdir(book_dir)

#read all directories in the book directory, this is a list
for language in os.listdir(book_dir):
    #loops over authors
    for author in os.listdir(book_dir + '/' + language):
        #loops over titles
        for title in os.listdir(book_dir + '/' + language + '/' + author):
            inputfile = book_dir + '/' + language + '/' + author + '/' + title
            #to test that it's working correctly
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))

#Note you may have to delete .DS_store files, just navigate to the directory you want in terminal, type in 
# find . -name ‘*.DS_Store’ -type f -delete
# and it will clear .DS_Store files from all children directories as well

#simple table using pandas
import pandas as pd
table = pd.DataFrame(columns = ('name', 'age'))
table.loc[1] = 'James', 22
table.loc[2] = 'Jess', 32

#using pandas dataframe to keep track of book statistics
import pandas as pd
stats = pd.DataFrame(columns = ('language', 'author', 'title', 'length', 'unique'))
#to add data to this table, we need to keep track of the rows of the table
title_num = 1

for language in os.listdir(book_dir):
    #loops over authors
    for author in os.listdir(book_dir + '/' + language):
        #loops over titles
        for title in os.listdir(book_dir + '/' + language + '/' + author):
            inputfile = book_dir + '/' + language + '/' + author + '/' + title
            #to test that it's working correctly
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num] = language, author, title, sum(counts), num_unique
            title_num +=1